import cv2

def and_n(masklist):
    ''' Function bitwise.and_n.

    Computes bitwise AND between multiple images.

    Parameters:
        masklist (list_of_array_of_int):

    Returns:
        OutpuArray (array_of_int):
    '''
    if len(masklist) == 2:
        return cv2.bitwise_and(masklist[0], masklist[1])
    return cv2.bitwise_and(masklist[0], and_n(masklist[1:]))

def or_n(masklist):
    ''' Function bitwise.or_n.

    Computes bitwise OR between multiple images.

    Parameters:
        masklist (list_of_array_of_int):

    Returns:
        OutpuArray (array_of_int): 
    '''
    if len(masklist) == 2:
        return cv2.bitwise_or(masklist[0], masklist[1])
    return cv2.bitwise_and(masklist[0], or_n(masklist[1:]))