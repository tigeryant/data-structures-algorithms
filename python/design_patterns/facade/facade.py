from subsystem_components import *

class HomeTheaterFacade():

    # The facade is passed a reference to each component of the subsystem in its constructor.
    # The facade then assigns each to the corresponding instance variable
    def __init__(self, amp, dvd, projector, screen, lights, popper):
        self.amp = amp
        self.dvd = dvd
        self.projector = projector
        self.screen = screen
        self.lights = lights
        self.popper = popper

    # For each task, we delegate the responsibility to a subsystem
    def watchMovie(self, movie):
        print("Get ready to watch a movie...")
        self.popper.on()
        self.popper.pop()
        self.lights.dim(10)
        self.screen.down()
        self.projector.on()
        self.projector.wideScreenMode()
        self.amp.on()
        self.amp.setDvd(self.dvd)
        self.amp.setSurroundSound()
        self.amp.setVolume(5)
        self.dvd.on()
        self.dvd.play(movie)

    # When shutting down the theater with endMovie(), we again delegate each task to the
    # appropriate component in the subsystem
    def endMovie(self):
        print("Shutting home theater down...")
        self.popper.off()
        self.lights.on()
        self.screen.up()
        self.projector.off()
        self.amp.off()
        self.dvd.stop()
        self.dvd.eject()
        self.dvd.off()

# Instantiating the subsystem objects
popper = Popper()
lights = Lights()
screen = Screen()
projector = Projector()
amp = Amp()
dvd = Dvd()

# Instantiating the home theater
homeTheater = HomeTheaterFacade(amp, dvd, projector, screen, lights, popper)

# Testing the home theater
homeTheater.watchMovie("Raiders of the Lost Ark")
homeTheater.endMovie()