# AI Object Detection System

## Project Overview

The AI Object Detection System is a machine learning and computer vision project that uses the YOLO (You Only Look Once) object detection model to identify objects in images, including people.

The project includes image preparation, annotation, model training, testing, and a web-based application that allows users to upload images and view detection results.

## Objectives

- Learn the fundamentals of artificial intelligence and computer vision.
- Prepare and annotate images for object detection.
- Train and test a custom YOLO model.
- Develop a working web application for person detection.
- Allow users to upload images for detection.
- Display bounding boxes, the number of people detected, and confidence scores.

## Tools and Technologies

- Python
- Ultralytics YOLO
- Flask
- OpenCV
- Jupyter Notebook
- Visual Studio Code
- HTML and CSS
- MakeSense.ai for image annotation

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
├── notebooks/
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/giftybalbinaapordire-ui/AI-Object-Detection-System.git
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

### 5. Open the application

Visit the following address in your browser:

```text
http://127.0.0.1:5000
```

## How to Use the Web Application

1. Open the application in a web browser.
2. Select an image containing people.
3. Click the Detect People button.
4. Wait for the model to process the image.
5. View the detected people, bounding boxes, and confidence scores.

## Features

- Image upload
- AI-powered person detection
- Bounding box visualization
- Automatic people counting
- Detection confidence scores
- Web-based user interface

## Model Information

- Model type: YOLO object detection
- Detection class: Person
- Model weights: `best.pt`
- Framework: Ultralytics

The trained model detects people in images and displays bounding boxes around detected individuals.

## Latest YOLO11n Practical Results

### Training Configuration

- Model: YOLO11n
- Target class: Person
- Training images: 4
- Validation images: 1
- Epochs: 10
- Image size: 640
- Batch size: 2

### Detection Tests

| Test Image | Detections | Confidence |
|---|---:|---:|
| IMG_20260419_173858_181.jpg | 1 person | 89.6% |
| IMG_20260911_122545_411.jpg | 1 person | 91.8% |

Both detection results were visually checked, and the bounding boxes correctly surrounded the detected people.

### Validation Metrics

- Precision: 97.3%
- Recall: 100%
- mAP50: 99.5%
- mAP50-95: 89.5%

**Limitation:** These metrics are based on only one validation image containing one labelled person. A larger labelled dataset and validation set are needed to evaluate performance on unseen images.

## Current Project Status

The project includes image preparation, annotation, model training, testing, and a working Flask web application connected to the trained model.

## Learning Outcomes

This project provides practical experience in computer vision, image annotation, machine learning, model training, and web application development.

## Project Author

AI Object Detection Practical Project

## Disclaimer

This application detects people in images. It does not identify individuals by name or perform facial recognition.
