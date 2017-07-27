import numpy as np
import math
from skimage.measure import compare_ssim as ssim

def mse (image1, image2):
    error = np.sum((image1.astype('float') - image2.astype('float'))**2)
    #Smaller is more similar
    error = error/float(image1.shape[0]*image1.shape[1])
    return error

def dssimCompare (image1, image2):
    #Smaller is more similar
    return (1 - ssim(image1, image2, 3))/2

def psnrCompare (image1, image2):
    #See http://docs.opencv.org/2.4/doc/tutorials/highgui/video-input-psnr-ssim/video-input-psnr-ssim.html#videoinputpsnrmssim
    #Larger is more similar!
    error = 10*math.log10((255*255)/mse(image1, image2))
    return error

def msssimCompare(image1, image2):
    return error