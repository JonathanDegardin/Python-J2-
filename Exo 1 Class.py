class Domino:
    def __init__(self, faceA, faceB):
        self.FaceA = faceA
        self.FaceB = faceB
    def total(self):
        total = self.FaceA + self.FaceB
        return total
    def AffichePoints(self):
        print ("Face A : " + str(self.FaceA) + " et Face B : " +str(self.FaceB));

d = Domino(2,4)
d.AffichePoints()
x = d.total()
print(x)