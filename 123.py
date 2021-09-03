

class car():

    def __init__(self):
        self.one = 1


    def changed(self,send):
        self.one = send

    def printed(self):
        print(self.one)

a = car()
a.changed(10)
a.printed()
print(a.one)