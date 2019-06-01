class Line:
    def __init__(self, A = (1,1), B = (0,0)):
        self.A = A
        self.B = B
    def distance(self):
        return ((self.B[0] - self.A[0])**2 + (self.B[1] - self.A[1])**2)**(1/2)
    def slope(self):
        return (self.B[1] - self.A[1])/(self.B[0] - self.A[0])
'''
line = Line((3, 2), (8, 10))
print(line.distance())
print(line.slope())
'''
