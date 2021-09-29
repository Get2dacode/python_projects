#import our necessary library
from queue import Queue
#Creating our class Playlist
class Playlist:
    #creating our self object function
    def __init__(self,song,song1,song2,song3):
        self.song = song
        self.song1 = song1
        self.song2 = song2
        self.song3 = song3
#queue function for our song playlist
    def queue_song(self):
        queue = []
        queue.append(self.song)
        queue.append(self.song1)# Next song up
        queue.append(self.song2)
        queue.append(self.song3)
        print(queue)
        while (queue != []) :
            #pushes current node to top
            print('Now Playing-',queue.pop(0))
            print('Next up-',queue)
            if queue == 1 :
                print(queue)
            if queue == []:
               print('queue empty')
               #readding previous songs to playlist
    def add(self):
        playlist = Queue()
        playlist.put(self.song)
        playlist.put(self.song1)
        playlist.put(self.song2)
        playlist.put(self.song3)
        while playlist.empty()!= True:
            print(playlist.get())















Uk_drill = Playlist('Moscow 17 (GB x Screw x Mayski) - Did You See?','The Return - Screw ,Wizz' ,'Next Up - Part 1 ','Sonic - Kwengface')
print(Uk_drill.queue_song())
print(Uk_drill.add())

Top_100 = Playlist('Stay-The Kid LAROI & Justin Bieber','Industry Baby-Lil Nas X & Jack Harlow','ShiversEd-Sheeran','Woman-Doja Cat')
Top_100.queue_song()
Top_100.add()
