# Wrong-Rote-Vehicle-Detection-with-Security-Alert

## Overview

This project aims to enhance road safety by detecting vehicles taking wrong routes. It utilizes YOLO v8 for real-time vehicle detection and Optical Character Recognition (OCR) to read number plates. When a violation is detected, alerts are sent to the nearby traffic control room and the vehicle owner.

Features
Real-Time Vehicle Detection: Utilizes YOLO v8 for accurate and efficient vehicle detection.
Number Plate Recognition: Uses OCR to extract the number plate information from detected vehicles.
Alert System: Sends alerts to nearby traffic control rooms and the vehicle owner in case of a violation.
Installation
Prerequisites
Python 3.7 or higher
pip
CUDA (if using GPU)

### Clone the Repository

git clone https://github.com/Antarip1047/wrong-route-vehicle-detection-with-Security-Alert.git
cd wrong-route-vehicle-detection-with-Security-Alert

### Install Dependencies

pip install -r requirements.txt
YOLO v8 Setup
Follow the instructions to set up YOLO v8 from the official repository.

Usage
Running the Detection System
Start the detection script:


python detect_wrong_route.py
View results:

Detected violations will be logged in violations.log.
Alerts will be sent to the traffic control room and vehicle owner.
Configuration
Edit the config.json file to customize the alert system and detection parameters.

### Project Structure

wrong-route-vehicle-detection/
- config.json        # Configuration file for system parameters
- detect_wrong_route.py  # Main script for running the detection system
- models/            # Pre-trained YOLO v8 models
- ocr/               # OCR-related scripts and models
- utils/             # Utility scripts
- requirements.txt   # List of dependencies
- README.md          # Project documentation


### Acknowledgments
>YOLO v8
>Tesseract OCR