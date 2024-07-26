# Wrong-Rote-Vehicle-Detection-with-Security-Alert

Wrong-way driving is one of the primary causes of traffic jams and road accidents. The accurate detection of wrong routes in real-time, combined with prompt security alerts, can significantly enhance safety measures.
Our research introduces a solution leveraging You Only Look Once version 8 (YOLOv8) and centroid tracking algorithm, along with Optical Character Recognition (OCR) techniques, for real-time identification of wrong-way vehicles and generation of security alerts.

## Overview

This project aims to enhance road safety by detecting vehicles taking wrong routes. It utilizes YOLO v8 for real-time vehicle detection and Optical Character Recognition (OCR) to read number plates. When a violation is detected, alerts are sent to the nearby traffic control room and the vehicle owner.

## Features
- Real-Time Vehicle Detection: Utilizes YOLO v8 for accurate and efficient vehicle detection.
- Number Plate Recognition: Uses OCR to extract the number plate information from detected vehicles.
- Alert System: Sends alerts to nearby traffic control rooms and the vehicle owner in case of a violation.
## Installation
### Prerequisites
- Python 3.7 or higher
- pip
- CUDA (if using GPU)

### Clone the Repository

1. git clone https://github.com/Antarip1047/Wrong-Rote-Vehicle-Detection-with-Security-Alert
- cd wrong-route-vehicle-detection-with-Security-Alert

### Install Dependencies

pip install -r requirements.txt
YOLO v8 Setup

Follow the instructions to set up YOLO v8 from the [official repository](https://github.com/ultralytics).

## Project Structure

wrong-route-vehicle-detection/
- Video files/       - All datasets for testing
- yolo/              - Pre-trained YOLO v8 models
- ocr/               - OCR-related scripts and models
- requirements.txt   - List of dependencies
- README.md          - Project documentation

## Future Scope
- Application of system in rural areas
- Application of system in too busy area with too much traffic
- Application of gaze estimation and emotion analysis to predict accidents and cause of wrong route movements

## Acknowledgments
- YOLO v8

- Tesseract OCR