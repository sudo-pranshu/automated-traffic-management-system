import cv2
import pytesseract

def detect_plate_number(image):
    try:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        plate = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
        _, thresh = cv2.threshold(plate, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        config = r'--oem 3 --psm 7 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        text = pytesseract.image_to_string(thresh, config=config)
        return text.strip()
    except:
        return ""
