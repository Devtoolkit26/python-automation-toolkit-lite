"""
CSV / Excel merger.
Combines multiple spreadsheets into one — handles mismatched column orders
and gaps automatically.
"""
import glob
import pandas as pd
import argparse
from pathlib import Path


def merge_spreadsheets(directory, output_file, pattern="*"):
    """
    Merge all CSV and Excel files matching `pattern` in `directory` into one CSV.

    Args:
        directory:   Folder containing the spreadsheets.
        output_file: Path to write the merged CSV.
        pattern:     Glob pattern for filenames (default "*" = all).

    Returns:
        (row_count, file_count): number of total rows written and source files.
    """
    p = Path(directory)
    files = (list(p.glob(f"{pattern}.csv")) +
             list(p.glob(f"{pattern}.xlsx")) +
             list(p.glob(f"{pattern}.xls")))
    if not files:
        raise FileNotFoundError(f"No CSV/Excel files in {directory} matching {pattern}")

    dfs = []
    for f in files:
        if f.suffix.lower() == ".csv":
            df = pd.read_csv(f)
        else:
            df = pd.read_excel(f)
        df["__source_file"] = f.name
        dfs.append(df)

    merged = pd.concat(dfs, ignore_index=True, sort=False)
    merged.to_csv(output_file, index=False)
    return len(merged), len(files)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Merge CSV/Excel files")
    ap.add_argument("directory", help="Folder containing files")
    ap.add_argument("output", help="Merged output CSV path")
    ap.add_argument("--pattern", default="*", help="Filename glob pattern (default: *)")
    args = ap.parse_args()

    rows, count = merge_spreadsheets(args.directory, args.output, args.pattern)
    print(f"Merged {rows} rows from {count} files -> {args.output}")
