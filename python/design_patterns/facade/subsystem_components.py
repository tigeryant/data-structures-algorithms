# Class definitions for the home theater subsystem

class Popper():
    def on(self):
        print("Popper is turning on...")

    def pop(self):
        print("Popper is popping...")

    def off(self):
        print("Popper is turning off...")

class Lights():
    def dim(self, brightness):
        print(f"Dimming lights to {brightness}...")
    
    def on(self):
        print("Turning lights on...")

class Screen():
    def down(self):
        print("Turning screen down...")

    def up(self):
        print("Turning screen up...")

class Projector():
    def on(self):
        print("Turning projector on...")
    
    def wideScreenMode(self):
        print("Projector going into wide screen mode...")
    
    def off(self):
        print("Turning projector off...")
    
class Amp():
    def on(self):
        print("Turning amp on...")
    
    def setDvd(self, dvd):
        print(f"Setting the following dvd player: {dvd}...")
    
    def setSurroundSound(self):
        print("Setting surround sound...")
    
    def setVolume(self, volume):
        print(f"Setting the volume to {volume}...")
    
    def off(self):
        print("Turning amp off...")

class Dvd():
    def __str__(self):
        return "Dvd player 1"

    def on(self):
        print("Turning Dvd player on...")
    
    def play(self, movie):
        print(f"Dvd player is playing {movie}...")
    
    def stop(self):
        print("Dvd player is stopping...")
    
    def eject(self):
        print("Dvd player is ejecting movie...")
    
    def off(self):
        print("Dvd player is turning off...")