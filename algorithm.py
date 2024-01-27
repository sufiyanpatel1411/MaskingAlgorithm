import cv2
import numpy as np

# Load the cartridge case image
image = cv2.imread('cartridge_case.png', cv2.IMREAD_COLOR)

# Define the colors for masking
breech_face_color = (0, 0, 255)
aperture_shear_color = (0, 255, 0)
firing_pin_impression_color = (128, 0, 128)
firing_pin_drag_color = (173, 216, 230)
firing_pin_drag_direction_color = (255, 0, 0)

# Define the regions of interest for masking
breech_face_roi = (100, 100, 100, 50)
aperture_shear_roi = (200, 200, 50, 50) 
firing_pin_impression_roi = (300, 300, 50, 50)
firing_pin_drag_roi = (400, 400, 50, 50) 
firing_pin_drag_direction_roi = (450, 450, 20, 20)

# Create a copy of the image to apply masks
masked_image = image.copy()

# Mask the breech-face impression
cv2.rectangle(masked_image, (breech_face_roi[0], breech_face_roi[1]), (breech_face_roi[0] + breech_face_roi[2], breech_face_roi[1] + breech_face_roi[3]), breech_face_color, -1)

# Mask the aperture shear
cv2.rectangle(masked_image, (aperture_shear_roi[0], aperture_shear_roi[1]), (aperture_shear_roi[0] + aperture_shear_roi[2], aperture_shear_roi[1] + aperture_shear_roi[3]), aperture_shear_color, -1)

# Mask the firing pin impression
cv2.rectangle(masked_image, (firing_pin_impression_roi[0], firing_pin_impression_roi[1]), (firing_pin_impression_roi[0] + firing_pin_impression_roi[2], firing_pin_impression_roi[1] + firing_pin_impression_roi[3]), firing_pin_impression_color, -1)

# Mask the firing pin drag
cv2.rectangle(masked_image, (firing_pin_drag_roi[0], firing_pin_drag_roi[1]), (firing_pin_drag_roi[0] + firing_pin_drag_roi[2], firing_pin_drag_roi[1] + firing_pin_drag_roi[3]), firing_pin_drag_color, -1)

# Mask the direction of firing pin drag
cv2.arrowedLine(masked_image, (firing_pin_drag_direction_roi[0], firing_pin_drag_direction_roi[1]), (firing_pin_drag_direction_roi[0] + firing_pin_drag_direction_roi[2], firing_pin_drag_direction_roi[1] + firing_pin_drag_direction_roi[3]), firing_pin_drag_direction_color, 2, tipLength=0.1)

# Show the masked image
cv2.imshow('Masked Image', masked_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
