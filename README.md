# OpenCV Project - Number Plate Detection

This repository contains Python code for real-time number plate detection using OpenCV. The code utilizes the Haar Cascade Classifier, specifically trained for detecting Russian license plates. When a license plate is detected, it is highlighted with a rectangle, and its region of interest (ROI) is shown in a separate window. The user can also save the detected license plates by pressing 'p' on the keyboard.

## Usage :

### Prerequisites:
- Python 3.x
- OpenCV
- Webcam or an external camera
- IP camera app (for phone camera setup)

### Webcam Setup:

1. Download the "haarcascade_russian_plate_number.xml" Haar Cascade classifier file and place it in the "Resources" folder of the project.

2. Connect your webcam to your computer or use an external camera.

3. Open a terminal or command prompt and navigate to the project directory.

4. Run the Python script: `python NumberPlate_detection.py`

5. The webcam feed will open, and the number plate detection will start in real-time.

6. When a license plate is detected, it will be highlighted with a green rectangle, and its ROI will be displayed in a separate window.

7. Press 'p' on your keyboard to save the detected license plate image. The saved images will be stored in the "Resources/Scanned_Number_Plates" folder.

8. Press 's' on your keyboard to stop the detection and exit the program.

### Phone Camera Setup:

1. Download the "haarcascade_russian_plate_number.xml" Haar Cascade classifier file and place it in the "Resources" folder of the project.

2. Install an IP camera app (e.g., IP Webcam for Android) on your phone.

3. Open the IP camera app on your phone and configure the settings. Note down the IP address and port number provided by the app.

4. Ensure that your phone and laptop are connected to the same local Wi-Fi network.

5. Update the Python script with the IP address and port number obtained from the IP camera app:

   ```python
   phone_ip_address = "your_phone_ip_address"
   port = "your_port_number"
   phone_camera_url = f"http://{phone_ip_address}:{port}/video"
   ```

6. Open a terminal or command prompt and navigate to the project directory.

7. Run the Python script: `python NumberPlate_detection.py`

8. The phone camera feed will open, and the number plate detection will start in real-time.

9. When a license plate is detected, it will be highlighted with a green rectangle, and its ROI will be displayed in a separate window.

10. Press 'p' on your keyboard to save the detected license plate image. The saved images will be stored in the "Resources/Scanned_Number_Plates" folder.

11. Press 's' on your keyboard to stop the detection and exit the program.

Please note that using the phone camera requires an IP camera app on your phone to stream the camera feed over the local network. Ensure that both your phone and laptop are connected to the same Wi-Fi network for successful communication between the devices.