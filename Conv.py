import json
import pandas as pd

# Load JSON file
json_file_path = "ocr_output.json"
with open(json_file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Extract text data from JSON
extracted_data = []
for page in data.get("pages", []):
    for block in page.get("blocks", []):
        for line in block.get("lines", []):
            for word in line.get("words", []):
                xmin, ymin = word["geometry"][0]  # Top-left corner
                xmax, ymax = word["geometry"][1]  # Bottom-right corner
                
                extracted_data.append({
                    "word": word["value"],
                    "confidence": word.get("confidence", "N/A"),
                    "xmin": xmin,
                    "ymin": ymin,
                    "xmax": xmax,
                    "ymax": ymax
                })

# Convert to DataFrame
df = pd.DataFrame(extracted_data)

# Save as CSV
csv_file_path = "ocr_output.csv"
df.to_csv(csv_file_path, index=False, encoding="utf-8")

print(f"CSV saved to {csv_file_path}")
