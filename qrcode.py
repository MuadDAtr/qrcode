import qrcode
zakoduj = qrcode.make("https://github.com/MuadDAtr")
zakoduj.save("kod_qr.png")
