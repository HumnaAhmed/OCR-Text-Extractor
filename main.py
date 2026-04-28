import cv2
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

print("Current Folder:", os.getcwd())

def resize_for_display(image, max_width=800, max_height=600):
    h, w = image.shape[:2]
    scale = min(max_width / w, max_height / h)

    if scale < 1:
        image = cv2.resize(image, (int(w * scale), int(h * scale)))

    return image

# Output file
output_file = "ocr_output.txt"

with open(output_file, "w", encoding="utf-8") as f:
    f.write("OCR Results:\n\n")

for file in os.listdir():

    if file.lower().endswith((".png", ".jpg", ".jpeg")):

        print(f"\nProcessing: {file}")

        img = cv2.imread(file)

        if img is None:
            print("Image load nahi hui!")
            continue

        # Grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Resize (OCR accuracy improve)
        gray = cv2.resize(gray, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)

        # Blur
        blur = cv2.GaussianBlur(gray, (5, 5), 0)

        # Adaptive Threshold
        thresh = cv2.adaptiveThreshold(
            blur,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            11,
            2
        )

        # Morphological cleaning
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
        processed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

        # Optional: invert (sometimes improves OCR)
        processed = cv2.bitwise_not(processed)

        # =========================
        # 🔥 OCR
        # =========================
        custom_config = r'--oem 3 --psm 11'
        text = pytesseract.image_to_string(processed, config=custom_config)

        print("Extracted Text:\n", text)

        # Save to file
        with open(output_file, "a", encoding="utf-8") as f:
            f.write(f"File: {file}\n")
            f.write(text)
            f.write("\n" + "="*50 + "\n")

        display_original = resize_for_display(img)
        display_processed = resize_for_display(processed)

        cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
        cv2.namedWindow("Processed", cv2.WINDOW_NORMAL)

        cv2.imshow("Original", display_original)
        cv2.imshow("Processed", display_processed)

        cv2.waitKey(0)

cv2.destroyAllWindows()

print("\n✅ All results saved in:", output_file)