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
    def __repr__(self):
        print("Solde : " + str(self.solde) + "; Titulaire : " + str(self.nomTitu));

compte1 = CompteBancaire("Jean",1000)
compte1.retrait(200)
compte1.Affiche()
compte2 = CompteBancaire("Marc")
compte2.dépot(500)
compte2.Affiche()
compte1.__repr__()
compte2.__repr__()