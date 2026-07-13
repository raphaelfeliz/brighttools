---
wp_id: {01-wp-slug}
parent_id: {01-incr-slug}
status: completed
timestamp: {YYYY-MM-DDTHH:MM:SS-TZ}

files_changed:
  - path: {relative/path/to/file}
    type: {new|modify|delete}

commands_run:
  - command: {command_string}
    status: {success|failure}
    output_ref: {evidence/file.log}

behavioral_change: |
  {Concise description of code behavior change}

evidence_links:
  - path: {evidence/file}
    type: {image|text|log}
---
