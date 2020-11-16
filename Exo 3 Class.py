class TableMultiplication:
    def __init__(self,num):
        self.num=num;
        self.multiplicateur=0;
    def prochain(self):
        total = self.num * self.multiplicateur;
        print (total);
        self.multiplicateur = self.multiplicateur +1;

tab = TableMultiplication(3)
tab.prochain()
tab.prochain()
tab.prochain()
tab.prochain()