class TableMultiplication:
    def __init__(self,num):
        self.num=num;
        self.multiplicateur=0;
    def prochain(self):
        total = self.num * self.multiplicateur;
        print (total);
        self.multiplicateur = self.multiplicateur +1;
    def __repr__(self):
        print("Numéro choisis : " + str(self.num) + "; Multiplicateur actuel : " + str(self.multiplicateur));
    def reset(self):
        self.multiplicateur=0;
tab = TableMultiplication(3)
tab.__repr__()
tab.prochain()
tab.__repr__()
tab.prochain()
tab.__repr__()
tab.prochain()
tab.__repr__()
tab.prochain()