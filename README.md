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

(Add your screenshots in screenshots folder)

---

## 📌 Future Improvements

* GUI interface
* Deep learning OCR (CRNN)
* IAM dataset integration

---
