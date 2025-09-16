class Track:
    def __init__(self, song, artist):
        self.song = song  # assignment by reference
        self.artist = artist

def print_track_info(vocalist):# vocalist = singer
    print(f"Song is => {vocalist.song}")
    print(f"Arist is=> {vocalist.artist}")

# object creation 
singer = Track("This first time ever", "Roberta Flack")

# passing an object as an argument to initialize the variable
#  vocalist
print_track_info(singer)

    
