import json, sys, glob
from collections import Counter
import os

c = Counter()

print("Started counting...")


folder = sys.argv[1]
pattern = os.path.join(folder, "*.json")
files = sorted(glob.glob(pattern))

print("Current directory:", os.getcwd())
print("Searching folder:", os.path.abspath(folder))
print("Folder exists:", os.path.isdir(folder))
print("Matching files:", files)

for file in files:
    r = json.load(open(file))
    c[(r["utility"], r["security"])] += 1
    print(file, r["utility"], r["security"])

#print result
print("\nutility, security -> count")
for k, v in sorted(c.items()): 
    print(k, v)