import RPi.GPIO as GPIO

class ArduinoController:
    def __init__(self):
        self.NORTH = True
        self.SOUTH = False
        self.EAST = True
        self.WEST = False
        self.GO = True
        self.STOP = False

        self.PIN_NORTH_SOUTH = 14
        self.PIN_GO_STOP_NORTH_SOUTH = 15
        self.PIN_EAST_WEST = 18 #18
        self.PIN_GO_STOP_EAST_WEST = 23 #23

        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.PIN_NORTH_SOUTH, GPIO.OUT)
        GPIO.setup(self.PIN_EAST_WEST, GPIO.OUT)
        GPIO.setup(self.PIN_GO_STOP_NORTH_SOUTH, GPIO.OUT)
        GPIO.setup(self.PIN_GO_STOP_EAST_WEST, GPIO.OUT)

        GPIO.output(self.PIN_NORTH_SOUTH, False)
        GPIO.output(self.PIN_EAST_WEST, False)
        GPIO.output(self.PIN_GO_STOP_NORTH_SOUTH, False)
        GPIO.output(self.PIN_GO_STOP_EAST_WEST, False)

    def GoNorthSouth(self):
        GPIO.output(self.PIN_GO_STOP_NORTH_SOUTH, self.GO)

    def StopNorthSouth(self):
        GPIO.output(self.PIN_GO_STOP_NORTH_SOUTH, self.STOP)

    def GoEastWest(self):
        GPIO.output(self.PIN_GO_STOP_EAST_WEST, self.GO)

    def StopEastWest(self):
        GPIO.output(self.PIN_GO_STOP_EAST_WEST, self.STOP)

    def North(self):
        self.GoNorthSouth()
        GPIO.output(self.PIN_NORTH_SOUTH, self.NORTH)

    def South(self):
        self.GoNorthSouth()
        GPIO.output(self.PIN_NORTH_SOUTH, self.SOUTH)

    def East(self):
        self.GoEastWest()
        GPIO.output(self.PIN_EAST_WEST, self.EAST)

    def West(self):
        self.GoEastWest()
        GPIO.output(self.PIN_EAST_WEST, self.WEST)

# control = ArduinoController()

# Direction = None

# print("w: Go Forward\n s: Go Backward\n a: Go Left\n d: Go Right")

# while Direction != 'q':
#     Direction = input("Current Direction: ")

#     #North
#     if Direction == 'w':
#         Controller.North()

#     #South
#     if Direction == 's':
#         Controller.South()

#     #East
#     if Direction == 'a':
#         Controller.East()

#     #West
#     if Direction == 'd':
#         Controller.West()

#     #Stop Moving North/South
#     if Direction == 'b':
#         Controller.StopNorthSouth()

#     #Stop Moving East/West
#     if Direction == 't':
#         Controller.StopEastWest()

#     if Direction == 'q':
#         Controller.StopNorthSouth()
#         Controller.StopEastWest()
#         GPIO.cleanup()
#         print("Quitting")
#         exit()