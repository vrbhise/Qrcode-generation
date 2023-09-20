import pyqrcode
s = "https://www.youtube.com/@vaibhavibhise8520"
url = pyqrcode.create(s)
url.svg("qr.svg")
url.png("qr.png")