import os
import sys
import json
import difflib
import subprocess
from pathlib import Path
import yaml

ROOT_DIR = Path(r"C:\code\BrightTools")
PULL_DIR = ROOT_DIR / "worktrees" / "pull"
OUT_DIR = ROOT_DIR / "work"

THEME_DIRS = ["assets", "blocks", "config", "layout", "locales", "sections", "snippets", "templates"]

CUSTOM_KEYWORDS = [
    "mar26", "bt-", "jdgm", "judgeme", "brighttools", "short-description",
    "bundle", "brooms", "squeegee", "fresh home", "floor wipes", "window cleaners"
]

def is_binary(path):
    try:
        with open(path, "rb") as f:
            chunk = f.read(1024)
            return b"\0" in chunk
    except Exception:
        return True

def read_text(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read().replace("\r\n", "\n")
    except UnicodeDecodeError:
        with open(path, "r", encoding="latin-1") as f:
            return f.read().replace("\r\n", "\n")

def get_git_custom_commits(rel_path):
    try:
        cmd = ["git", "-C", str(ROOT_DIR), "log", "--oneline", "-n", "10", "--", rel_path]
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        lines = [l.strip() for l in res.stdout.strip().split("\n") if l.strip()]
        # filter out pure sync/pull/merge commits if possible
        custom = [l for l in lines if not any(k in l.lower() for k in ["chore(sync)", "merge:", "snapshot:"])]
        return custom
    except Exception:
        return []

def analyze():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Collect all theme relative paths
    all_rel_paths = set()
    for td in THEME_DIRS:
        main_td = ROOT_DIR / td
        pull_td = PULL_DIR / td
        if main_td.exists():
            for p in main_td.rglob("*"):
                if p.is_file():
                    all_rel_paths.add(p.relative_to(ROOT_DIR).as_posix())
        if pull_td.exists():
            for p in pull_td.rglob("*"):
                if p.is_file():
                    all_rel_paths.add(p.relative_to(PULL_DIR).as_posix())

    sorted_paths = sorted(list(all_rel_paths))

    identical = []
    line_endings_only = []
    new_in_upstream = []
    local_only = []
    fork_collisions = []
    template_config_drift = []
    pure_vendor_upgrades = []

    for rel in sorted_paths:
        main_path = ROOT_DIR / rel
        pull_path = PULL_DIR / rel

        if not main_path.exists():
            new_in_upstream.append(rel)
            continue
        if not pull_path.exists():
            local_only.append(rel)
            continue

        if is_binary(main_path) or is_binary(pull_path):
            with open(main_path, "rb") as f1, open(pull_path, "rb") as f2:
                if f1.read() == f2.read():
                    identical.append(rel)
                else:
                    fork_collisions.append({
                        "file": rel,
                        "reason": "Binary file differs",
                        "custom_indicators": [],
                        "custom_commits": []
                    })
            continue

        raw_main = main_path.read_bytes()
        raw_pull = pull_path.read_bytes()
        if raw_main == raw_pull:
            identical.append(rel)
            continue

        norm_main = read_text(main_path)
        norm_pull = read_text(pull_path)

        if norm_main == norm_pull:
            line_endings_only.append(rel)
            continue

        # Substantive content difference
        top_dir = rel.split("/")[0]

        # Check templates & config separately
        if top_dir in ["templates", "config"]:
            template_config_drift.append({
                "file": rel,
                "lines_main": len(norm_main.splitlines()),
                "lines_pull": len(norm_pull.splitlines()),
            })
            continue

        # Analyze diff: lines in main that are NOT in pull (i.e. removed in 7.2.0)
        lines_m = norm_main.splitlines(keepends=True)
        lines_p = norm_pull.splitlines(keepends=True)
        diff = list(difflib.unified_diff(lines_p, lines_m, fromfile="pull_7.2.0", tofile="main_custom", n=2))

        # Check for custom lines in main
        added_in_main = [l[1:].strip() for l in diff if l.startswith("+") and not l.startswith("+++")]
        
        found_keywords = set()
        for line in added_in_main:
            line_lower = line.lower()
            for kw in CUSTOM_KEYWORDS:
                if kw in line_lower:
                    found_keywords.add(kw)

        # Check git commit history on main
        custom_commits = get_git_custom_commits(rel)

        # Check if the file name itself is custom
        is_custom_filename = any(k in rel.lower() for k in ["mar26", "bt-"])

        if found_keywords or custom_commits or is_custom_filename:
            # Extract sample removed lines
            sample_custom_lines = []
            for l in added_in_main:
                if any(k in l.lower() for k in CUSTOM_KEYWORDS) or "style" in l.lower() or "sections '" in l.lower():
                    if len(sample_custom_lines) < 8:
                        sample_custom_lines.append(l)

            fork_collisions.append({
                "file": rel,
                "custom_indicators": sorted(list(found_keywords)),
                "custom_filename": is_custom_filename,
                "custom_commits": custom_commits[:3],
                "sample_removed_in_pull": sample_custom_lines,
                "diff_summary": f"+{len(added_in_main)} lines unique to main"
            })
        else:
            pure_vendor_upgrades.append({
                "file": rel,
                "diff_summary": f"Standard vendor upgrade (Impact 6.12.0 -> 7.2.0)"
            })

    report = {
        "summary": {
            "total_theme_files": len(sorted_paths),
            "identical": len(identical),
            "line_endings_only": len(line_endings_only),
            "fork_collisions_count": len(fork_collisions),
            "template_config_drift_count": len(template_config_drift),
            "pure_vendor_upgrades_count": len(pure_vendor_upgrades),
            "new_in_upstream_count": len(new_in_upstream),
            "local_only_count": len(local_only),
        },
        "fork_collisions": fork_collisions,
        "template_config_drift": template_config_drift,
        "new_in_upstream": new_in_upstream,
        "local_only": local_only,
        "pure_vendor_upgrades": [item["file"] for item in pure_vendor_upgrades]
    }

    # Write JSON
    json_path = OUT_DIR / "theme-upgrade-7.2.0-audit.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    # Write YAML
    yaml_path = OUT_DIR / "theme-upgrade-7.2.0-audit.yaml"
    with open(yaml_path, "w", encoding="utf-8") as f:
        yaml.dump(report, f, sort_keys=False)

    # Write Markdown
    md_path = OUT_DIR / "theme-upgrade-7.2.0-audit.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# Impact 7.2.0 Upgrade Conflict & Focus Audit\n\n")
        f.write("## Overview\n\n")
        f.write(f"- **Total Theme Files Scanned**: {len(sorted_paths)}\n")
        f.write(f"- **Identical Content**: {len(identical)}\n")
        f.write(f"- **Line Endings Only (Ignorable)**: {len(line_endings_only)}\n")
        f.write(f"- **Fork Collisions (CRITICAL - Your custom code was removed)**: {len(fork_collisions)}\n")
        f.write(f"- **Template & Config Drift (`templates/`, `config/`)**: {len(template_config_drift)}\n")
        f.write(f"- **Pure Vendor Upgrades (Accept cleanly from 7.2.0)**: {len(pure_vendor_upgrades)}\n")
        f.write(f"- **New in Upstream 7.2.0**: {len(new_in_upstream)}\n")
        f.write(f"- **Local Only in Main**: {len(local_only)}\n\n")

        f.write("## 1. Critical Fork Collisions (Where to Focus First)\n\n")
        f.write("These core vendor files contain BrightTools customizations on `main` that Shopify's 7.2.0 update stripped out:\n\n")
        for item in fork_collisions:
            f.write(f"### `{item['file']}`\n")
            if item.get("custom_indicators"):
                f.write(f"- **Custom Tokens Found**: `{', '.join(item['custom_indicators'])}`\n")
            if item.get("custom_commits"):
                f.write(f"- **Related Git Commits**: {'; '.join(item['custom_commits'])}\n")
            if item.get("sample_removed_in_pull"):
                f.write("- **Custom Code Stripped in 7.2.0 (Sample)**:\n```liquid\n")
                for s in item["sample_removed_in_pull"]:
                    f.write(f"{s}\n")
                f.write("```\n")
            f.write("\n")

        f.write("## 2. New in Upstream 7.2.0\n\n")
        for n in new_in_upstream:
            f.write(f"- `{n}`\n")
        f.write("\n")

        f.write("## 3. Local Only in Main\n\n")
        for l in local_only:
            f.write(f"- `{l}`\n")
        f.write("\n")

        f.write("## 4. Template & Config Drift\n\n")
        f.write("JSON templates and settings where custom section blocks or presets changed:\n\n")
        for t in template_config_drift:
            f.write(f"- `{t['file']}`\n")
        f.write("\n")

        f.write("## 5. Pure Vendor Upgrades (Safe to accept)\n\n")
        f.write(f"Total {len(pure_vendor_upgrades)} standard Impact files (locales, blocks, untouched vendor sections/snippets).\n")

    print(f"Audit completed successfully!")
    print(f"- Fork collisions: {len(fork_collisions)}")
    print(f"- Template/config drift: {len(template_config_drift)}")
    print(f"- Pure vendor upgrades: {len(pure_vendor_upgrades)}")
    print(f"Outputs written to {OUT_DIR}")

if __name__ == "__main__":
    analyze()
