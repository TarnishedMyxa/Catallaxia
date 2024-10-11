

class protocol:
    def __init__(self, name, version):
        self.name = name
        self.version = version

    def __str__(self):
        return self.name + " " + self.version