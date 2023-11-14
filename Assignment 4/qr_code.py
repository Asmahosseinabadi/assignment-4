import qrcode
name=input("enter your name : ")
phone_number=input("enter your phone number: ")

name_qr=qrcode.make(name)
name_qr.save("my_qrcode1.png")

phone_qr=qrcode.make(phone_number)
phone_qr.save("my_qrcode2.png")
