import cv2
import numpy as np

def process_image(input_image_path):
    # Step 1: Read and resize the input image to 1900x1425
    input_image = cv2.imread(input_image_path)
    resized_image = cv2.resize(input_image, (1900, 1425))

    # Step 2: Perform edge detection
    gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    _, thresholded_image = cv2.threshold(blurred_image, 50, 255, cv2.THRESH_BINARY)

    # Step 3: Apply exposure adjustment (1.5x) to pixels related to the product
    output_image = resized_image.copy()
    # Adjust exposure for non-white pixels
    output_image[thresholded_image != 0] = np.clip(output_image[thresholded_image != 0] * 1.5, 0, 255).astype(np.uint8)

    # Step 4: Crop the image from the center to make it 1200x800
    height, width = output_image.shape[:2]
    crop_width, crop_height = 1200, 800
    start_x = max(0, width // 2 - crop_width // 2)
    start_y = max(0, height // 2 - crop_height // 2)
    cropped_image = output_image[start_y:start_y + crop_height, start_x:start_x + crop_width]

    return cropped_image

# Example usage:
input_image_path = "D:\\modelcarshop\\20230125_151835.jpg"
processed_image = process_image(input_image_path)

# Display or save the processed image
cv2.imshow('Processed Image', processed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
