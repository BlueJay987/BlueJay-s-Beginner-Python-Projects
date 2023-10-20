#QR CODE GENERATOR
import segno 

#Declare Variables
data = input("Input the data you need to encrypt: ")
bordersize = int(input("Input border size: "))
scaleqr = int(input("Input scale: "))
filename = input("Input the file name: ")

#Generate
qrcode = segno.make(data)
qrcode.save(filename + ".png", border=bordersize, scale=scaleqr)

#Confirm
print("GENERATED")