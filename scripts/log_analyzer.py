# argparse lets us accept command-line arguments,
# so we can run this on ANY log file, not just "test.log"
import argparse

# Set up the argument parser with a short description
parser = argparse.ArgumentParser(description="Count log levels in a log file.")

# Define one required argument: the path to the log file
parser.add_argument("filename", help="Path to the log file to analyze")

# Parse the arguments the user actually typed in the terminal
args = parser.parse_args()

# Use the filename they gave us, instead of a hardcoded string
counts = {}

with open(args.filename, "r") as f:
    for line in f:
        line = line.strip()
        for level in ["ERROR", "WARNING", "INFO"]:
            if level in line:
                counts[level] = counts.get(level, 0) + 1

print(f"Log level summary for {args.filename}:")
for level, count in counts.items():
    print(f"{level}: {count}")