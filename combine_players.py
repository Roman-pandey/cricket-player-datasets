import pandas as pd
import os

PLAYERS_FOLDER = "players"
OUTPUT_FOLDER = "combined"
OUTPUT_FILE = "all_players_combined.xlsx"

all_dfs = []

for file in os.listdir(PLAYERS_FOLDER):
    if file.endswith(".xlsx"):
        path = os.path.join(PLAYERS_FOLDER, file)
        df = pd.read_excel(path)

        if "Player_Name" not in df.columns:
            print(f"Skipping {file} (Player_Name missing)")
            continue

        all_dfs.append(df)

combined_df = pd.concat(all_dfs, ignore_index=True)

os.makedirs(OUTPUT_FOLDER, exist_ok=True)
output_path = os.path.join(OUTPUT_FOLDER, OUTPUT_FILE)
combined_df.to_excel(output_path, index=False)

print("✅ Combined file created:", output_path)
print("📊 Total rows:", combined_df.shape[0])

