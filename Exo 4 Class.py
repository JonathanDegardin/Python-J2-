import math
class Fraction:
    def __init__(self,num,denom):
        self.num=num;
        self.denom=denom;
        self.resultat=str(num)+"/"+str(denom);
    def affiche(self):
        print(self.resultat);
    def __add__(self, other):
        denom = self.denom * other.denom
        num = self.num * other.denom + self.denom * other.num
        i=2
        while i<=num and i<= denom:
            if num%i == 0 and denom%i==0:
                num=num//i
                denom=denom//i
            else:
                i=i+1
        return Fraction(num,denom)
    def __sub__(self, other):
        denom = self.denom * other.denom
        num = self.num * other.denom - self.denom * other.num
        i = 2
        while i <= num and i <= denom:
            if num % i == 0 and denom % i == 0:
                num = num // i
                denom = denom // i
            else:
                i = i + 1
        return Fraction(num, denom)
    def __mul__(self, other):
        numFin = self.num * other.num;
        denomFin = self.denom * other.denom;
        return Fraction(numFin, denomFin);
    def __truediv__(self, other):
        numFin = self.num * other.denom;
        denomFin = self.denom * other.num;
        i=2
        while i <= numFin and i <= denomFin:
            if numFin % i == 0 and denomFin % i == 0:
                numFin = numFin // i
                denomFin = denomFin // i
            else:
                i = i + 1
        return Fraction(numFin, denomFin);
    def __repr__(self):
        print("Fraction actuel : " + str(self.num) + "/" + str(self.denom));

f = Fraction(3, 4)
print("F")
f.affiche()
g = Fraction(1, 2)
print("G")
g.affiche()
print("Addition")
r1 = f + g
r1.affiche()
print("Soustraction")
r2 = f-g
r2.affiche()
print("Multiplication")
r3 = f*g
r3.affiche()
print("Division")
r4 = f/g
r4.affiche()
f.__repr__()
g.__repr__()
r1.__repr__()
r2.__repr__()
r3.__repr__()
r4.__repr__()