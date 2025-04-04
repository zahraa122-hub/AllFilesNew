import pandas as pd

# List of CSV files to merge
csv_files = ["file.csv", "file2.csv"]

# Read and concatenate all files
df = pd.concat([pd.read_csv(f) for f in csv_files])

# Save to a new CSV file
df.to_csv("test.csv", index=False)

print("CSV files merged successfully into merged_file.csv")
