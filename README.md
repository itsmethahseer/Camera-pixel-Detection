# Camera Detection Mini-Project

This mini-project implements a basic motion detection system using a webcam feed. When significant motion is detected, it draws bounding boxes around the moving objects and plays an alert sound.

## Requirements

- Python 3.x
- OpenCV (`pip install opencv-python`)
- `winsound` (already included in standard Python libraries)

## Usage

1. Clone or download the project repository to your local machine.

2. Install the required dependencies:

   ```bash
   pip install opencv-python
   ```

3. Run the `main.py` script:

   ```bash
   python main.py
   ```

4. The webcam feed window will open. Any motion detected will be indicated by bounding boxes and an alert sound.

5. Press `q` to quit the program.

## Explanation

- The program captures frames from the webcam and compares consecutive frames to detect areas with motion.

- It converts the color frames to grayscale, applies Gaussian blur and thresholding, and then performs contour detection.

- Contours with an area less than 5000 pixels are ignored (you can adjust this threshold in the code).

- Significant motion triggers a bounding box and an alert sound.

## Files

- `main.py`: The main Python script for motion detection.

- `alert.wav`: Alert sound file played when motion is detected.

## Acknowledgements

- The project uses the `OpenCV` library for computer vision tasks.
