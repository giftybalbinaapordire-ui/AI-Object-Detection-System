# AI Object Detection System

## Project Overview
The AI Object Detection System is a machine learning project that uses computer vision to identify objects in images. The project uses the YOLO object detection model to detect objects, including people, in images.

## Objectives
- Learn the fundamentals of AI and computer vision.
- Prepare and annotate images for object detection.
- Train and test an object detection model.
- Detect objects in images and review the results.

## Tools and Technologies
- Python
- YOLO and Ultralytics
- Jupyter Notebook
- Visual Studio Code
- MakeSense.ai for image annotation

## Project Structure
- `dataset/` – Contains the image dataset and annotations.
- `notebooks/` – Contains notebooks used for experiments and testing.
- `README.md` – Provides information about the project.
- `requirements.txt` – Lists the project's Python dependencies.

## Current Status
The project includes image preparation, object annotation, model training, and testing with sample images.

## Learning Outcome
This project provides practical experience in computer vision, image annotation, machine learning, and object detection.
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

### Results and Model Files
Training weights and annotated detection results are saved locally. Personal photographs and model-weight files are not included in this public repository.
