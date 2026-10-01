# AI-Based Hand Gesture Recognition System

## Project Overview

The **AI-Based Hand Gesture Recognition System** is a real-time Computer Vision application developed using **Python, OpenCV, and MediaPipe**. The system uses a webcam to detect a user's hand and identify different hand gestures based on hand landmarks and finger positions.

The project demonstrates how Computer Vision can be used to create a simple human-computer interaction system where users can interact with an application using hand gestures.

## Features

* Real-time hand detection using a webcam
* Hand landmark detection using MediaPipe
* Real-time gesture recognition
* Detection of multiple hand gestures
* Visual display of hand landmarks
* Gesture name displayed on the camera screen
* Simple and interactive interface

## Gestures

The system is designed to recognize the following gestures:

* **Open Palm** ✋
* **Fist** ✊
* **One Finger** ☝️
* **Peace** ✌️
* **Thumbs Up** 👍

## Technologies Used

* **Python**
* **OpenCV**
* **MediaPipe**
* **Computer Vision**
* **VS Code**
* **Webcam**

## How the System Works

1. The webcam captures the user's hand in real time.
2. OpenCV reads the video frames from the webcam.
3. Each frame is converted into an appropriate image format for processing.
4. MediaPipe Hand Landmarker detects the hand and identifies its key landmarks.
5. The detected landmarks provide the positions of different hand joints and fingers.
6. The system analyzes the positions of the fingers to determine the gesture.
7. The recognized gesture is displayed on the camera screen along with the hand landmarks.

## Project Structure

```text
AI_Hand_Gesture_Recognition/
│
├── venv/
├── hand_landmarker.task
├── gesture_detection.py
└── README.md
```

## Installation

### 1. Create the Project Folder

Create a folder named:

```text
AI_Hand_Gesture_Recognition
```

Open the folder in **VS Code**.

### 2. Create a Virtual Environment

Use Python 3.12 and create a virtual environment:

```bash
py -3.12 -m venv venv
```

Activate the environment:

```bash
.\venv\Scripts\Activate.ps1
```

### 3. Install Required Libraries

Install the required Python libraries:

```bash
pip install opencv-python mediapipe
```

### 4. Add the MediaPipe Model

Download the **MediaPipe Hand Landmarker model** and place the file:

```text
hand_landmarker.task
```

inside the main project folder.

The structure should look like:

```text
AI_Hand_Gesture_Recognition/
│
├── venv/
├── hand_landmarker.task
└── gesture_detection.py
```

## Running the Project

After installing the required libraries and adding the model file, run:

```bash
python gesture_detection.py
```

The webcam will open and the system will start detecting the user's hand.

Move your hand in front of the webcam and show different gestures. The detected hand landmarks will appear as points, and the recognized gesture will be displayed on the screen.

To stop the camera, press **Q**. If the camera window does not respond to the keyboard, press **Ctrl + C** in the VS Code terminal.

## Example

When the user shows:

```text
✋  →  OPEN PALM
✊  →  FIST
☝️  →  ONE
✌️  →  PEACE
👍  →  THUMBS UP
```

the system displays the corresponding gesture name on the camera screen.

## Learning Outcomes

Through this project, practical experience was gained in:

* Computer Vision
* Real-time video processing
* Hand landmark detection
* MediaPipe
* OpenCV
* Gesture recognition
* Python programming
* Debugging and testing
* Real-time AI application development

## Future Improvements

The system can be further improved by:

* Supporting more hand gestures
* Improving recognition accuracy
* Supporting both hands simultaneously
* Adding voice output for detected gestures
* Developing a graphical user interface
* Training a Machine Learning classifier using hand landmark data
* Using gestures to control other applications or devices

## Conclusion

The **AI-Based Hand Gesture Recognition System** demonstrates the practical use of Computer Vision and hand landmark detection for real-time gesture recognition. It provides a foundation for developing gesture-based human-computer interaction applications.
