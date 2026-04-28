# 🧾 OCR Text Extractor (Python + OpenCV + Tesseract)

## 📌 Overview

This project implements a basic Optical Character Recognition (OCR) system using Python. It extracts text from both printed and handwritten images using OpenCV for preprocessing and Tesseract OCR engine.

---

## ⚙️ Technologies Used

* Python
* OpenCV
* pytesseract (Tesseract OCR)

---

## 🚀 How to Run

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Install Tesseract OCR

Download and install Tesseract, then update path in code:

```
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

### 3. Run the program

```
python main.py
```

---

## 🖼️ Input Images

* sample1.jpg → handwritten text
* sample2.jpg → printed text

---

## 📤 Output

* Extracted text is displayed in terminal
* Saved in `ocr_output.txt`

---

## ⚠️ Limitations

* Works best on printed text
* Limited accuracy for handwritten text

---

## 📊 Results

* Printed text → High accuracy
* Handwritten text → Moderate/Low accuracy

---

## 📸 Screenshots

<img width="955" height="504" alt="image" src="https://github.com/user-attachments/assets/2b6b9d5e-bd5d-4203-b6a2-359c4a422b03" />
<img width="953" height="502" alt="image" src="https://github.com/user-attachments/assets/759e86e2-d639-4f02-8864-6b9406b82a68" />

---

## 📌 Future Improvements

* GUI interface
* Deep learning OCR (CRNN)
* IAM dataset integration

---
