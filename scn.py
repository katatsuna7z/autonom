import cv2
import pytesseract

def image_scanner_to_text(image_path):
    # Read the image using OpenCV
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Could not read the image.")
        return

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to highlight text
    _, threshold_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)

    # Use pytesseract to perform OCR
    text = pytesseract.image_to_string(threshold_image)

    # Print the extracted text
    print("Scanned Text:")
    print(text)

# Replace 'your_image_path.jpg' with the actual path to your image
image_scanner_to_text('your_image_path.jpg')
