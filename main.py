import qrcode as qr
img = qr.make("https://www.youtube.com/results?search_query=eshika+shrestha")
img.save("eshika_youtube.png")