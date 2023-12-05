import cv2
import pytesseract

def image_scanner_to_text(image_path):
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Tidak ada foto terdeteksi.")
        return
        
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, threshold_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)
    text = pytesseract.image_to_string(threshold_image)

    print("Scanned Text:")
    print(text)

image_scanner_to_text('user_in_img')
