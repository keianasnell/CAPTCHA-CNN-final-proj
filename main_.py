from CAPTCHA_object_detection import *
#import cv2
import os

# test = r'/Users/keianarei/Desktop/CAPTCHA-final/test/ttest.jpg'
# print(Captcha_detection(test))



#directory = r'/Users/keianarei/Desktop/CAPTCHA-final/kaggle_data/train/'
directory = r'/Users/keianarei/Desktop/CAPTCHA-final/test/'
for filename in os.listdir(directory): 
	# if filename.endswith(".jpg"):
	input_path = os.path.join(directory, filename)
	#image_np = cv2.imread(input_path)
	#print(image_np.shape())
	# print input_path
	print filename, Captcha_detection(input_path)

