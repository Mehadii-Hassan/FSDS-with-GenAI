import cv2

# Read the image
image = cv2.imread('C:\\Users\\Mehedi\\Desktop\\FSDS with Gen AI\\FSDS-with-GenAI\\11. Deep Learning\\2. CNN\\Computer Vision\\resources\\lena.png')

#print(image) #output will be a numpy array representing the image
#print(image.shape) #output will be the dimensions of the image (height, width, channels)

#cv2.imshow('Lena Image', image) # Display the image in a window
#cv2.waitKey(0) # Wait for a key press to close the window
#cv2.destroyAllWindows() # Close all OpenCV windows


# Read the video
video = cv2.VideoCapture("C:\\Users\\Mehedi\\Desktop\\FSDS with Gen AI\\FSDS-with-GenAI\\11. Deep Learning\\2. CNN\\Computer Vision\\resources\\elon.mp4")

while True:
    success, img = video.read() # Read a frame from the video
    cv2.imshow("Video", img) # Display the frame in a window

    if cv2.waitKey(1) & 0xFF == ord('q'): # Wait for 'q' key to exit
        break



# Read the webcam
webcam = cv2.VideoCapture(0)

webcam.set(3, 640) # Set the width of the webcam frame
webcam.set(4, 480) # Set the height of the webcam frame

while True:
    success, img = webcam.read() # Read a frame from the webcam
    cv2.imshow("Webcam", img) # Display the frame in a window

    if cv2.waitKey(1) & 0xFF == ord('q'): # Wait for 'q' key to exit
        break