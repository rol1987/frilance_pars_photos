# import required module
import cv2
  
# get image
filepath = r"C:\Users\Olga\Desktop\onfotolife\foto.jpg"
image = cv2.imread(filepath)
#print(image.shape)
  
# get width and height
height, width = image.shape[:2]
  
# display width and height
print("The height of the image is: ", height)
print("The width of the image is: ", width)