import cv2
import numpy as np
from PIL import Image, ImageFilter
import random

#Input Image
input_image = cv2.imread('XRay.jpg')
#print(input_image)


#Convert the truecolor RGB image to the grayscale image
gray = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
input_image = cv2.GaussianBlur(gray,(3,3),0)

img = np.array(input_image)
lt, bt = img.shape
ed = Image.fromarray(img)
ed.show()
img = img.flatten()

#Edge Detection using Prewitt operator
oi = np.array([[-1,-1,-1], [0,0,0],[1,1,1]])
oj = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
x = cv2.filter2D(img, cv2.CV_16S, oi)
y = cv2.filter2D(img, cv2.CV_16S, oj)
absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)
result = cv2.addWeighted(absX, 1, absY, 1, 0)
result = np.array(result)
result = result.reshape(lt,bt)
ed = Image.fromarray(result)
ed.show()


#print('Result', result)

#Key Generation using Chaotic Map proposed by the paper
key = []
k = 1.4
lmd = 12
q = 2
p = 0
lt, bt = input_image.shape
for i in range(lt):
        for j in range(bt):
            s =  result[i][j]
            if(s != 0):
                p = p + s
sd = int((p / (lt * bt)) % 256)
edge_detected = result.flatten()
significant_image = np.array(edge_detected)
#print("significant_image", significant_image)
for i in range (len(edge_detected) ):
    s = significant_image[i]
    if( s > sd ):
        k1 = ( lmd - k ) / ( lmd - ( q * k ))
        q = random.randint(2,255)
        k = k1
        key.append(int((k*pow(10, 10))%256)) 
#print("Key",key)


#Cipher image pixels by OTP ( modular addition with key and edge detected image)
cipher = []
Prk = []
l=0
input_image = input_image.flatten()
for i in range ( len(input_image) ):
    e = significant_image[i]
    inp = input_image[i]
    
    if ( e > sd):
        k = key[l]
        c = inp + (k*lmd)
        cipher.append(int((c%256)))
        p = (k  +  inp ) / 255
        Prk.append(int(p))
        l += 1
        
    
    else:
        cipher.append(inp)
    
#print(cipher)

#Converting cipher array to image
l = 0
en = np.array(result)

#print("Length", lt)
#print("Breadth", bt)

for i in range (0 , lt):
    for j in range (0 ,bt):
        en[i][j] = cipher[l]
        l = l + 1
    
c = Image.fromarray(en)
c.show(title="Cipher")

#Decryption
decrypt = []
l = 0
for i in range (0, len(input_image) ):
    c = cipher[i]
    s = significant_image[i]
    if (s > sd):
        prk = Prk[l]
        enk = cipher[i]
    #ksq = Ksq[i]
        ksq = key[l]
        d = int ((( enk - ( ksq * lmd )) + (prk * 255)) % 256)
        decrypt.append(( d ))
        l += 1
       

    else:
        decrypt.append(( c )) 
        

    
#Decrpted array to image matrix
dp = np.array(result)
l=0
for i in range (0 , lt):
    for j in range (0 ,bt):
        dp[i][j] = decrypt[l]
        l = l + 1
    
en = Image.fromarray(dp)
en.show(title="Decrypted Image")