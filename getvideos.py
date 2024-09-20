from pytube import Playlist

p = Playlist("https://www.youtube.com/playlist?list=PLHiueU_hUKFwM6kV8WTVF9fBGpIeat8Ba")
url = []

for link in p:
  url.append(link)