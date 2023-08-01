import cv2
import datetime

frameWidth = 640
frameHeight = 480
nplateCascade = cv2.CascadeClassifier("Resources/haarcascade_russian_plate_number.xml")
minArea = 500
color = (0, 0, 255)
count = 1

# Replace the IP address and port with the ones provided by the IP camera app on your phone
phone_ip_address = "your_phone_ip_address"
port = "your_port_number"

phone_camera_url = f"http://{phone_ip_address}:{port}/video"

cap = cv2.VideoCapture(phone_camera_url)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

while True:
    success, img = cap.read()
    if not success:
        break

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    numberPlates = nplateCascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in numberPlates:
        area = w * h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, "Number Plate", (x, y - 5),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
            imgROI = img[y:y+h, x:x+w]
            cv2.imshow("ROI", imgROI)

            # Get current date and time
            current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

            # Save the detected number plate image with timestamp on your local PC
            save_path = f"detected_number_plates/NoPlate_{current_time}.jpg"
            cv2.imwrite(save_path, imgROI)
            count += 1

    cv2.imshow("Phone Camera", img)

    # Press 'q' to exit the loop and close the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
