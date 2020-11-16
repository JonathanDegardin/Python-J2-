def genateurxFois(nb):
    generateur = ['a','b','c','d','e'];
    generateur2 = [];
    for i in range (0,len(generateur)):
        for j in range(0,nb):
            print(generateur[i]);
            generateur2.append(generateur[i]);

    print (generateur2);


a= int(input("Choisissez le nombre d'itérations : "));
genateurxFois(a);