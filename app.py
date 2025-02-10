import json
from doctr.io import DocumentFile
from doctr.models import ocr_predictor

# Load model
model = ocr_predictor(pretrained=True)

# Load image (ensure the file exists)
image_path = "images/APAR_Form_I_14.png"
single_img_doc = DocumentFile.from_images(image_path)

# Perform OCR
result = model(single_img_doc)

# Debug output
print("OCR Output:", result.export())
json_output = result.export()

# Show result (optional, may fail in some environments)
try:
    result.show()
except Exception as e:
    print(f"Error showing result: {e}")

#Save JSON file
json_file_path = "ocr_output1.json"
with open(json_file_path, "w", encoding="utf-8") as f:
    json.dump(json_output, f, indent=4)

print(f"JSON saved to {json_file_path}")



