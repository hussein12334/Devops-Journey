# Store the filename in a variable so it's easy to change later
filename = "test.log"
# A dictionary to keep track of how many times we see each log level.
# Starts empty -- we'll add keys as we find them.
counts = {}

with open(filename, "r") as f:
	for line in f:
		line = line.strip()

		# Check each possible log level and bump its count if found.
		for level in ["ERROR", "WARNING", "INFO"]:
			if level in line:
				# .get(level, 0) returns the current count for this level,
                # or 0 if it's not in the dictionary yet -- avoids a KeyError
                # on the first time we see a given level.
				counts[level] = counts.get(level, 0) + 1

# Once we've gone through every line, print the totals.
print("Log level summary:")
for level, count in counts.items():
    print(f"{level}: {count}")