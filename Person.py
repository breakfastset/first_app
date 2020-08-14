class Person:
    def __init__(self):
        self.name = "Jordan"
        self.number = 23

    def __str__(self):
        return "{} - {}".format(self.name, self.number)
