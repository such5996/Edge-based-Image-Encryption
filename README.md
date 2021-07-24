# Edge-based-Image-Encryption
It is an Edge based Image Lightweight Encryption. It is based on the above paper mentioned<br />
Encryption Technique summary <br />
1. Generate edge map of the image and get the significant blocks (Prewitt Edge Detection used) <br />
2. Generate a key with a Chaotic Map. The key sequence is equal to the number of significant blocks in the edge map <br />
3. OTP based Encryption using the Key generated in Chaotic Map and the significant pixels in the Original Image <br />
4. Generate a special key while encryption for extra security and to be used in the Decryption phase
5. Decryption

<p align="center">
  <img src="https://github.com/such5996/Edge-based-Image-Encryption/blob/main/XRay.jpg" width="350" alt="accessibility text">
  <img src="https://github.com/such5996/Edge-based-Image-Encryption/blob/main/Edge_Detected.jpg" width="350" title="Edge Map">
  <img src="https://github.com/such5996/Edge-based-Image-Encryption/blob/main/Encrypted_Image.jpg" width="350" title="Encrypted Image">
  <img src="https://github.com/such5996/Edge-based-Image-Encryption/blob/main/Decrypted_Image.jpg" width="350" title="Decrypted Image">
</p>
