from pytube import Playlist, YouTube
import threading

p = Playlist("https://www.youtube.com/playlist?list=PLHiueU_hUKFwM6kV8WTVF9fBGpIeat8Ba")
url = []

def get_titulo(link):
  video = YouTube(link)
  split = video.title.split('(')
  if split[1] == 'Upward Swing Handle Switch)':
    split[1] = 'USHS'
  if split[1] == 'Team Fortress 2 Basic Spy Reversal)':
    split[1] = 'TF2 spy reversal'
  if split[1] == 'Pen Twirl from WeAreArtsea)':
    split[1] = 'Pen Twirl'
  url.append({"link": link, "titulo": split[1].replace(')', '')})

threads = []

for link in p:
  t1 = threading.Thread(target=get_titulo, args=(link,))
  threads.append(t1)
  t1.start()

for t in threads:
  t.join()