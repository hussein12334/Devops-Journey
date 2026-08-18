#!/usr/bin/env python3
"""
dir_scanner.py - Scans a directory and reports file counts and total size by extension.
Usage: python3 dir_scanner.py <path>
"""

import os
import sys
from collections import defaultdict

def scan_directory(path):
    stats = defaultdict(lambda: {"count": 0, "size": 0})

    for root, dirs, files in os.walk(path):
        for filename in files:
            filepath = os.path.join(root, filename)
            ext = os.path.splitext(filename)[1].lower() or "(no extension)"
            try:
                size = os.path.getsize(filepath)
            except OSError:
                continue  # skip files we can't read (broken symlinks etc.)
            stats[ext]["count"] += 1
            stats[ext]["size"] += size

    return stats

def format_size(bytes_size):
    for unit in ["B", "KB", "MB", "GB"]:
        if bytes_size < 1024:
            return f"{bytes_size:.1f}{unit}"
        bytes_size /= 1024
    return f"{bytes_size:.1f}TB"

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 dir_scanner.py <path>")
        sys.exit(1)

    target_path = sys.argv[1]

    if not os.path.isdir(target_path):
        print(f"Error: '{target_path}' is not a valid directory.")
        sys.exit(1)

    stats = scan_directory(target_path)

    print(f"\nScan results for: {target_path}\n")
    print(f"{'Extension':<20}{'Count':<10}{'Total Size':<12}")
    print("-" * 42)

    for ext, data in sorted(stats.items(), key=lambda x: x[1]["size"], reverse=True):
        print(f"{ext:<20}{data['count']:<10}{format_size(data['size']):<12}")

if __name__ == "__main__":
    main()
