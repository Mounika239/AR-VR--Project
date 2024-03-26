import cv2
import numpy as np

def create_birds_eye_view(image_path):
    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Unable to read the image.")
        return

    # Display original image
    cv2.imshow('Original Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Rotate the image 90 degrees counter-clockwise to get the bird's-eye view
    rotated_image = np.rot90(image)

    # Display the bird's-eye view
    cv2.imshow("Bird's Eye View", rotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Path to the JPG image
image_path = r'C:\Users\k\PycharmProjects\pythonProject\image_4.jpg'

# Create bird's-eye view for the JPG image
create_birds_eye_view(image_path)



