import numpy as np
import cv2

def mask(img):
    ''' Function humidite_relative.mask.

    Detects regions of a picture whose relative humidity rate is less than 50%.
    
    Parameters:
        img (array_of_int): Picture from where low relative humidity rates are extracted.

    Returns:
        OutputArray (array_of_int): Mask of low relative humidity rates.
    '''
    # Variables declaration
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_pourcent_max_relat_humidite = 90
    # Color range of relative humidity between 0% and 50%
    lower_relat_humidity = (0, 0, 0)
    upper_relat_humidity = (h_pourcent_max_relat_humidite, 255, 255)
    # Mask (to select colors)
    mask = cv2.inRange(img_hsv, lower_relat_humidity, upper_relat_humidity)
    # Opening (to reduce noise)
    kernel = np.ones((3, 3), np.uint8)   # structural element
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    return opening
    
def test():
    # Get the image
    img = cv2.imread('./data/humidite-relative.jpg')
    # Deal with the situation when the file is not found
    if type(img) == type(None):
        raise FileNotFoundError("<humidite-relative> file was not found.")
    # Apply the function "mask" on the image to create a mask
    result = mask(img)
    # Apply the mask obtained on the image and display the result
    cv2.imshow('Result', cv2.bitwise_and(img, img, mask=result))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    test()