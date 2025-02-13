# 📝 OCR Application

This is an **OCR (Optical Character Recognition) application** that extracts text from images using `doctr`.  
The application processes images and saves the extracted text as JSON.

## 📂 Project Structure

- `images/` - Folder for input images  
- `__pycache__/` - Python cache files (ignored in Git)  
- `app.py` - Main script to run the OCR  
- `Conv.py` - Supporting script (if needed)  
- `ocr_output1.json` - Sample OCR output  
- `requirements.txt` - Python dependencies  
- `.gitignore` - Git ignore file  
- `README.md` - Project documentation  

## 🚀 How to Run the Application

### 1️⃣ Clone the Repository
Clone the repository from GitHub and navigate into the project directory.  

`git clone https://github.com/sakshiagarwala0206/docTr__.git`  
`cd doctr-ocr-project`  

### 2️⃣ Create and Activate a Virtual Environment (Recommended)

#### For Windows  
`python -m venv venv`  
`venv\Scripts\activate`  

#### For macOS/Linux  
`python3 -m venv venv`  
`source venv/bin/activate`  

### 3️⃣ Install Dependencies
Run the following command to install all dependencies:  

`pip install -r requirements.txt`  


### 4️⃣ Run the OCR Application
Run the main script:  

`python app.py`  
 

## 🛠 Troubleshooting

### 🔹 "ModuleNotFoundError: No module named 'doctr'"
`pip install doctr`  

### 🔹 "No module named 'cv2'"
`pip install opencv-python`  

### 🔹 "Torch not found or incorrect version"
`pip install torch torchvision`  


