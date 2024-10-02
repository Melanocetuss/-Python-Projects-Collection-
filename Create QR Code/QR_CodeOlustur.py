import qrcode
import PIL
link = qrcode.make("https://jukebox-official.github.io/JukeBox/Contact.html")
link.save("iletisimQR.png")