import os
import pandas as pd

new_data_dir = os.path.expanduser("~/Downloads/csv_incremental/data/new")
processed_file_path = os.path.expanduser("~/Downloads/csv_incremental/data/processed/processed_dimen_lookup.csv")

if os.path.exists(processed_file_path):
    processed_df = pd.read_csv(processed_file_path, dtype=str)
    print(f"[INFO] Loaded existing processed file with {len(processed_df)} rows.")
else:
    processed_df = pd.DataFrame(columns=["Code", "Description", "SortOrder"])
    print(f"[INFO] No processed file found. Starting fresh.")

for filename in os.listdir(new_data_dir):
    if filename.endswith(".csv"):
        file_path = os.path.join(new_data_dir, filename)
        print(f"[INFO] Processing {filename}...")

        new_df = pd.read_csv(file_path, dtype=str)
        new_df = new_df.dropna(subset=["Code"])
        new_rows = new_df[~new_df["Code"].isin(processed_df["Code"])]

        print(f"[INFO] Found {len(new_rows)} new rows.")

                if not new_rows.empty:
            processed_df = pd.concat([processed_df, new_rows], ignore_index=True)

processed_df.to_csv(processed_file_path, index=False)
print(f"[INFO] Updated processed file saved with {len(processed_df)} total rows.")
