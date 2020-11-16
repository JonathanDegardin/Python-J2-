class Poly:
    def __init__(self,*args):
        self.List = [];
        for i in range(0,len(args)):
            self.List.append(args[i]);
    def coef(self):
        return print(self.List);
    def evalue(self,num):
        calculAuto=0
        for i in range(0,len(self.List)):
            calculAuto = calculAuto + self.List[i] * (num ** i)
        return print(calculAuto);

p = Poly(3,4,-2)
p.coef()
p.evalue(2)