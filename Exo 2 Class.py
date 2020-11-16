class CompteBancaire:
    solde=0
    def __init__(self,nomTitu,solde=0):
        self.nomTitu=nomTitu;
        self.solde=solde;
    def retrait(self,montant):
        self.solde= self.solde-montant;
    def dépot(self,montant):
        self.solde=self.solde+montant;
    def Affiche(self):
        print("Le solde actuel de " + str(self.nomTitu) + " est " + str(self.solde))

compte1 = CompteBancaire("Jean",1000)
compte1.retrait(200)
compte1.Affiche()
compte2 = CompteBancaire("Marc")
compte2.dépot(500)
compte2.Affiche()