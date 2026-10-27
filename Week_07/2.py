class Monitor:
    def __init__(self, width:int,height:int):
        self.width = width
        self.height = height

    def __eq__(self, other):
        return self.width == other.width and self.height == other.height

monitor1 = Monitor(1920,1080)
monitor2 = Monitor(1920,1080)
monitor3 = Monitor(3840,2160)
print(monitor1 == monitor2)
print(monitor1 == monitor3)