# AI Person Detection System

## Project Overview
The AI Person Detection System is a web-based application that uses a trained YOLO (You Only Look Once) deep learning model to detect people in uploaded images. The application allows users to upload an image and receive visual detection results, including bounding boxes, the number of people detected, and confidence scores.

This project was developed as part of an Artificial Intelligence practical project.

## Objectives
- Develop a working web application for person detection.
- Integrate a custom-trained YOLO model.
- Allow users to upload images for detection.
- Display bounding boxes around detected people.
- Show the number of detections and confidence scores.

## Technologies Used
- Python
- Flask
- Ultralytics YOLO
- OpenCV
- HTML
- CSS

## Features
- Image upload
- AI-powered person detection
- Bounding box visualization
- People count
- Detection confidence scores
- Web-based user interface

## Project Structure
```text
AI-Object-Detection-System/
├── web_app/
│   ├── app.py
│   ├── model/
│   │   └── best.pt
│   ├── templates/
│   │   └── index.html
│   └── static/
│       ├── style.css
│       ├── uploads/
│       └── results/
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the repository
```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate into the project directory
```bash
cd AI-Object-Detection-System
```

### 3. Install dependencies
```bash
python -m pip install -r requirements.txt
```

### 4. Run the application
```bash
python web_app/app.py
```

### 5. Open in a browser
Visit:
```text
http://127.0.0.1:5000
```

## How to Use
1. Open the application in a browser.
2. Select an image containing people.
3. Click the **Detect People** button.
4. View the processed image and detection results.

## Model Information
- Model type: YOLO object detection
- Detection class: Person
- Model weights: `best.pt`

The model identifies people in images and displays bounding boxes with confidence scores.

## Project Author
AI Object Detection Practical Project

## Disclaimer
This application detects people in images. It does not identify individuals by name or perform facial recognition.
