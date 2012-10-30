from obd2 import Command

class SpeedCommand(Command):
    def __init__(self):
        Command.__init__(self, "SPEED_COMMAND", "Gets the speed")

class TachCommand(Command):
    def __init__(self):
        Command.__init__(self, "TACH_COMMAND", "Gets the tach")
