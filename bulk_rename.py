"""
Bulk file renamer using regex patterns.
Rename hundreds of files in one shot without a GUI.
"""
import re
import pathlib
import argparse


def bulk_rename(directory, pattern, replacement, dry_run=True):
    """
    Rename files matching `pattern` to `replacement`.

    Args:
        directory: Path to the folder of files to rename.
        pattern:   Regex pattern to match (e.g., r"IMG_(\d+)\.jpg").
        replacement: Replacement pattern (can reference groups, e.g., r"photo_\1.jpg").
        dry_run:   If True, only print what would be renamed. Default True for safety.

    Returns:
        List of (old_name, new_name) tuples.
    """
    path = pathlib.Path(directory)
    if not path.exists():
        raise FileNotFoundError(f"{directory} does not exist")

    renamed = []
    for f in sorted(path.iterdir()):
        if not f.is_file():
            continue
        new_name = re.sub(pattern, replacement, f.name)
        if new_name == f.name:
            continue
        if dry_run:
            print(f"  [dry-run] {f.name} -> {new_name}")
        else:
            f.rename(f.parent / new_name)
            print(f"  {f.name} -> {new_name}")
        renamed.append((f.name, new_name))

    return renamed


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Bulk file renamer")
    ap.add_argument("directory", help="Folder to process")
    ap.add_argument("pattern", help="Regex to match filenames")
    ap.add_argument("replacement", help="Replacement (can use \\1, \\2 for groups)")
    ap.add_argument("--execute", action="store_true",
                    help="Actually rename (default is dry-run)")
    args = ap.parse_args()

    bulk_rename(args.directory, args.pattern, args.replacement, dry_run=not args.execute)
