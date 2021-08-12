# Python-QRCode
A code that generate QR Code in Python

##How to use?
This is very simple.

First install Python
Then type these two command:
```
pip3 install qrcode   
pip3 install pillow
```

Then you can run the code

##How to edit the code?

At this line :
```
qr.add_data('https://9e-docteur.github.io/qrcodelandingpage/')
```
There is a link, the link is where when you scan the QR Code, you will be redirected to the link

---
```
img = qr.make_image(fill_color="black", back_color="white")
```
fill color is the color of the QR Code
Back color is the background color
---
```
img.save('qrcode.png')
```
This the name of the file
.png is the image file type.
