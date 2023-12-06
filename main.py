import cv2
import numpy as np

import bitwise
import temperature
import humidite_sol
import humidite_relative
import precipitation
import precipitation_nuage

def dipslay_result(img, mask):
    ''' Function display_result.

    Displays the result with red area for potential fires.

    Parameters:
        img (array_of_int): Base image.
        mask (array_of_int): Mask gathering all criterias for potential fires.
    '''
    red_mask = np.zeros(img.shape, np.uint8)
    red_mask[:,:,0] = 255
    red_mask[:,:,1] = 255
    result_mask = ~cv2.bitwise_or(red_mask, red_mask, mask=mask)
    cv2.imshow('Result', cv2.bitwise_and(img, result_mask))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#===========================================================
# MAIN
#===========================================================

datapath = './data/'
img_humidite_sol = cv2.imread(datapath + 'humidite-sol.jpg')
img_humidite_relative = cv2.imread(datapath + 'humidite-relative.jpg')
img_precipitation = cv2.imread(datapath + 'precipitation.jpg')
img_precipitation_nuage = cv2.imread(datapath + 'precipitation-nuage.jpg')
img_temperature = cv2.imread(datapath + 'temperature.jpg')
img = cv2.imread(datapath + 'satellite.jpg')

result_mask = bitwise.and_n([
    humidite_sol.mask(img_humidite_sol),
    humidite_relative.mask(img_humidite_relative),
    precipitation.mask(img_precipitation),
    precipitation_nuage.mask(img_precipitation_nuage),
    temperature.mask(img_temperature)])

dipslay_result(img, result_mask)