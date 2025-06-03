import cv2
import time
import pytesseract
import pandas as pd
from ultralytics import YOLO
from number_plate import detect_plate_number

# Load YOLOv8 model (auto-downloads yolov8n.pt if not present)
model = YOLO("yolov8n.pt")

# Set tesseract path (adjust if needed)
pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"

# CSV log
log_file = "traffic_log.csv"
columns = ['timestamp', 'vehicle_count', 'plate_numbers']
df = pd.DataFrame(columns=columns)

cap = cv2.VideoCapture(0)

print("🔴 Press 'q' to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Inference
    results = model(frame)
    boxes = results[0].boxes
    labels = results[0].names
    vehicle_count = 0
    detected_plates = []

    for box in boxes:
        cls = int(box.cls[0])
        label = labels[cls]
        if label in ['car', 'bus', 'truck', 'motorbike']:
            vehicle_count += 1
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            roi = frame[y1:y2, x1:x2]

            plate = detect_plate_number(roi)
            if plate:
                detected_plates.append(plate)
                cv2.putText(frame, plate, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label, (x1, y2 + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Log data
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    df = pd.concat([df, pd.DataFrame([[now, vehicle_count, ','.join(detected_plates)]], columns=columns)], ignore_index=True)
    df.to_csv(log_file, index=False)

    cv2.putText(frame, f"Vehicles: {vehicle_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (36, 255, 12), 2)
    cv2.imshow("Traffic Management System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
