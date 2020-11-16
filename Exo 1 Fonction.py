def chiffrePorteBonheur(nb):
    d=nb
    e = [int(e) for e in str(nb)]
    compte = 0;
    while d > 10:
      for i in range(0,len(e)):
          d = 0;
          d = d + e[i]*e[i];
          print(d);
      e = [int(e) for e in str(d)];
      compte = compte +1;
      if compte > 100:
          return 'no';
      if d == 1:
        return 'yes';
    return 'no';

a = int(input("Choisissez votre nombre : "));
[int(i) for i in str(a)]
b = chiffrePorteBonheur(a);
if b == 'yes':
    print("Votre nombre est bien porte bonheur !");
else :
    print("Votre nombre n'est pas porte bonheur !");
