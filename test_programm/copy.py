
src = open("C:\\Users\\athar\\Downloads\\audio.mp3","rb")
des= open("audio.mp3","wb")
des.write(src.read())
print("File copied")