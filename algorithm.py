import cv2
import numpy as np

# Color constants
BREECH_FACE_COLOR = (0, 0, 255)
APERTURE_SHEAR_COLOR = (0, 255, 0)
FIRING_PIN_IMPRESSION_COLOR = (255, 0, 255)
FIRING_PIN_DRAG_COLOR = (255, 255, 0)
DIRECTION_OF_DRAG_COLOR = (255, 0, 0)

def apply_mask(image, mask, color):
    colored_mask = cv2.merge((mask, mask, mask))
    return cv2.bitwise_and(image, colored_mask)

def find_and_draw_contours(image, mask, color):
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contour_mask = np.zeros_like(image)
    cv2.drawContours(contour_mask, contours, -1, color, 2)
    return contour_mask

def main():
    # Load the original image
    original_image = cv2.imread('cartridge_case.png')

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

    # Define the thresholds for creating masks
    threshold_values = [200, 100, 50, 25]

    # Generate masks using different thresholds
    masks = [cv2.threshold(gray_image, thresh, 255, cv2.THRESH_BINARY)[1] for thresh in threshold_values]

    # Apply masks and draw contours
    masked_image = original_image.copy()

    for mask, color in zip(masks, [BREECH_FACE_COLOR, APERTURE_SHEAR_COLOR, FIRING_PIN_IMPRESSION_COLOR, FIRING_PIN_DRAG_COLOR]):
        masked_image = apply_mask(masked_image, mask, color)

    # Draw contours for the direction of firing pin drag
    masked_image = cv2.add(masked_image, find_and_draw_contours(original_image, masks[-1], DIRECTION_OF_DRAG_COLOR))

    # Display the masked image
    cv2.imshow('Masked Image', masked_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
