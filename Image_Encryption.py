import cv2
import numpy as np
from PIL import Image, ImageFilter

#Input Image
input_image = cv2.imread('Image.jpg')

#Convert the truecolor RGB image to the grayscale image
gray = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
input_image = cv2.GaussianBlur(gray,(3,3),0)
input_image=np.array(input_image)
ed = Image.fromarray(input_image)
ed.show(title="Input image")

lt, bt = input_image.shape
image = input_image

#print(input_image)
print(input_image.shape)

input_image = input_image.flatten()
print(input_image.size)
#for i in range(input_image.size):
    #if(input_image[i] <=2):
        #input_image[i] = input_image[i]
    #else:
        #input_image[i] = input_image[i]   

#Edge Detection using Prewitt operator
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
img_prewittx = cv2.filter2D(input_image, -1, kernelx)
img_prewitty = cv2.filter2D(input_image, -1, kernely)
edge_detected = np.array(img_prewittx + img_prewitty)

edge_detected = edge_detected.reshape(lt, bt)

ed = Image.fromarray(edge_detected)
ed.show()

    #print(key[i])

#Key Generation using Chaotic Map proposed by the paper
key = []
k = 0
lmd = 12
edge_detected = edge_detected.flatten()
for i in range ( len(edge_detected) ):
    im = edge_detected[i]
    k1 = ( lmd - k ) / ( lmd - (im * k ))
    k = k1 
    #print(k)
    key.append(int((k*pow(10, 16))%256)) 

#Cipher image pixels by OTP ( modular addition with key and edge detected image)
cipher = []
for i in range ( len(input_image) ):
    e = edge_detected[i]
    k = key[i]
    c = e + k
    cipher.append(int((c%256)))

#Converting cipher array to image
l = 0
en = np.array(image)

print("Length", lt)
print("Breadth", bt)

for i in range (0 , lt):
    for j in range (0 ,bt):
        en[i][j] = cipher[l]
        l = l + 1
    
cipher = Image.fromarray(en)
cipher.show(title="Cipher")

