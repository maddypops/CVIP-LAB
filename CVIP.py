import cv2
import numpy as np

input_image_path = 'test.jpg'
image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE) 

if image is None:
    print("Error: Could not open or read the image.")
else:
    
    edges = cv2.Canny(image, 300, 300)  
    output_image_path = 'edges_output.jpg'
    cv2.imwrite(output_image_path, edges)
  
    cv2.imshow('Original Image', image)
    cv2.imshow('Edge Detection', edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
