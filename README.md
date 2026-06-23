# Face Recognition System

## Description
A Python-based face recognition system that detects, encodes, and identifies faces using the Face Recognition library. The application compares facial features against a stored dataset to accurately recognize individuals in images or real-time video streams.

## Features
- Face detection from images and webcam feed
- Facial encoding and matching
- Real-time face recognition
- Multiple face support
- Easy dataset management
- High recognition accuracy

## Technologies Used
- Python
- Face Recognition Library
- OpenCV
- NumPy

## Prerequisites
Make sure you have the following installed:

- Python 3.x
- pip

## Installation

1. Clone the repository:

```bash
git clone https://github.com/gudapati-manasa/face-recognition.git
```

2. Navigate to the project directory:

```bash
cd face-recognition-system
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. create folder with following name: trained_images
2.Add known face images to the trained_images folder.
3. Run the application:

```bash
python main.py
```

3. The system will detect and identify faces from the webcam feed or input images.

## Project Structure

```text
face-recognition-system/
│
├── trained_images/
│   └── Known face images
├── main.py
├── requirements.txt
└── README.md
```

## Future Enhancements
- Attendance management integration
- Face recognition with cloud database
- User registration interface
- Improved recognition performance

## Author
Maanasa Gudapati
