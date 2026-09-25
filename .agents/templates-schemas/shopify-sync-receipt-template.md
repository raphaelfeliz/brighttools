# Shopify Sync Receipt

- **Timestamp**: <YYYY-MM-DDTHH:MM:SSZ>
- **Store**: brighttools-au.myshopify.com
- **Theme ID**: <numeric-id> (<Theme Name>)
- **Theme Status**: <unpublished | live>
- **Operation**: <pull | push | verify>
- **Outcome-Status**: <completed | failed | reconciliation-pending | discrepancy>
- **Snapshot Commit**: <shopify-pulls SHA, when applicable>
- **File Count**: <number of files in full pull, when applicable>

## Synchronized Files
- For a full pull, record `all theme files` and the count. For a selective operation, list each `--only <file_path>` flag separately.

## Verification Results
- **Pull / Push CLI Output**: <result or error>
- **Local Comparison**: <identical / content differences / line-ending-only differences / pending>
- **Verification Pull Match**: <exact byte match / discrepancies / not applicable>
- **Main Commit**: <main SHA, when applicable>
