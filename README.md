# Python Automation Toolkit — Free Preview

Three standalone Python automation scripts I reach for constantly. Each under 100 lines, commented, and ready to drop into a project.

## What's here

| Script | What it does |
|--------|--------------|
| [`bulk_rename.py`](bulk_rename.py) | Rename files in bulk using regex patterns |
| [`csv_merge.py`](csv_merge.py) | Combine multiple CSV/Excel files with smart column matching |
| [`api_cache.py`](api_cache.py) | Decorator that caches API responses to disk (TTL configurable) |

## Usage

```bash
git clone https://github.com/Devtoolkit26/python-automation-toolkit-lite.git
cd python-automation-toolkit-lite
pip install -r requirements.txt
```

Then import whichever you need:

```python
from bulk_rename import bulk_rename
from csv_merge import merge_spreadsheets
from api_cache import cache_api
```

## The full pack

This is a 3-script preview of a larger 10-script automation toolkit I've been using in real projects. The full pack adds:

- Email sender with attachments (Gmail SMTP)
- PDF text extractor
- Directory watcher (watchdog-based)
- JSON/CSV converter with nested flattening
- Duplicate file finder (MD5)
- Scheduled task runner
- Web scraper template with rate limiting

Each in the full pack also ships with docs + example usage. If the three scripts here save you time, the full pack is at **[payhip.com/b/Zm4lG](https://payhip.com/b/Zm4lG)** ($12).

## License

MIT — do whatever you want with the 3 scripts here.

## Questions / feedback

Open an issue if you hit anything or have suggestions.
