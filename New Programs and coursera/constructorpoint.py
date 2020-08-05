class Point: #pascalConvention
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10,20)  # x and y initialised
point.x = 11  # to update initialised x
point(point.x)
