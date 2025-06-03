# 🚦 Automated Traffic Management System

A real-time, AI-powered traffic monitoring and management system using **YOLOv8**, **OpenCV**, **Tesseract OCR**, and **Streamlit**. This project simulates intelligent traffic control by detecting vehicles and number plates from live video feeds, logging traffic data, and displaying analytics on a live dashboard.

---

## 🔧 Features

- 📷 Real-time **vehicle detection** from webcam
- 🚗 Supports cars, trucks, buses, motorcycles (COCO dataset)
- 🔢 **Number plate recognition** with Tesseract OCR
- 📝 **CSV logging** of vehicle count and plates
- 📊 **Interactive dashboard** using Streamlit
- 🧠 **YOLOv8 integration** for high-performance detection
- 🛡️ Basic deadlock prevention logic for traffic signal fairness

---

## 📂 Folder Structure

```
automated_traffic_system/
├── main.py              # Real-time vehicle + plate detection & logging
├── number_plate.py      # OCR logic for number plate recognition
├── dashboard.py         # Live Streamlit dashboard
├── setup.sh             # Shell script to create venv and install dependencies
├── traffic_log.csv      # Auto-generated log of traffic data
├── requirements.txt     # Python dependencies (optional)
├── .gitignore           # Ignores venv, __pycache__, logs, etc.
└── README.md
```

---

## 🛠️ Setup Instructions

### 🔁 Clone the Repo

```bash
git clone https://github.com/sudo-pranshu/automated-traffic-management-system.git
cd automated-traffic-management-system
```

### 🧪 Set Up Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

_Or simply run the auto-setup script:_

```bash
bash setup.sh
```

---

## ▶️ Run the System

### Start Real-Time Detection

```bash
python3 main.py
```

### Open Live Dashboard (in a new terminal)

```bash
streamlit run dashboard.py
```

> Dashboard URL: http://localhost:8501

---

## 📊 Output Example

```
timestamp,vehicle_count,plate_numbers
2025-06-03 14:00:00,3,MH12AB1234
2025-06-03 14:00:01,2,
2025-06-03 14:00:02,4,GJ01CD0001,MH01DE2222
```

Detected vehicles are shown with bounding boxes and overlayed number plates.

---

## 📚 Libraries Used

- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- [OpenCV](https://opencv.org/)
- [pytesseract](https://github.com/madmaze/pytesseract)
- [Streamlit](https://streamlit.io/)
- [pandas](https://pandas.pydata.org/)

---

## 🚀 Future Scope

- 🚑 Emergency vehicle override logic
- 🔥 Frame snapshot on plate detection
- ☁️ Web-deployable dashboard
- 📲 IoT traffic light control via NodeMCU/ESP32
- 🕵️‍♂️ Rule violation tracking and alert system

---
> 👨‍💻 Built by [sudo-pranshu](https://github.com/sudo-pranshu)
---
> 💡 Want to contribute? Feel free to open issues or submit a pull request!
