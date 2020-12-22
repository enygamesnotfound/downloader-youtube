import pytube
import time
import os

url = input("inserisci il link del video: ")
video = pytube.YouTube(url)
os.system("cls")
for stream in video.streams:
    print(stream)
stream = video.streams.get_by_itag(
    input("inserisci il numero identificativo del itag per il tipo di video: "))
fileofname = input("come vorresti chiamare il tuo file? ")
os.system("cls")


is_download_done = True

print("ottima scelta!")
time.sleep(2)
print("il download e iniziato, attendere prego...")
time.sleep(5)
os.system("cls")

if is_download_done == True:
    stream.download(filename=fileofname)
    print("download eseguito con successo!")