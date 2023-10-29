
import cv2
import winsound
cam = cv2.VideoCapture(0)

# Read the first frame
ret, frame1 = cam.read()

while cam.isOpened():
    # Read the next frame
    ret, frame2 = cam.read()

    # Handle the case where the camera feed ends
    if not ret:
        break

    # Calculate the absolute difference between frames
    diff = cv2.absdiff(frame1, frame2)

    # Convert the difference to grayscale
    grey = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)  # Use BGR2GRAY instead of RGB2BGR

    # Apply Gaussian blur to the grayscale image
    blur = cv2.GaussianBlur(grey, (5, 5), 0)

    # Apply thresholding to create a binary image
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)

    # Apply dilation to enhance the edges
    dilated = cv2.dilate(thresh, None, iterations=3)

    # Find contours
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Draw the contours on the original frame
    # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
    for c in contours:
        if cv2.contourArea(c)<5000:
            continue
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
        winsound.PlaySound('alert.wav',winsound.SND_ASYNC)
        
    # Show the resulting frame
    cv2.imshow('Thahseer Cam', frame1)

    # Update frame1 with frame2 for the next iteration
    frame1 = frame2

    # Break the loop if 'q' is pressed
    if cv2.waitKey(10) == ord('q'):
        break

# Release the camera and destroy all OpenCV windows
cam.release()
cv2.destroyAllWindows()
