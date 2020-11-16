def compteur(fonction):
    def espion(*args, **kwargs):
        espion.call += 1
        print("La fonction " + fonction.__name__ + " a été appelée " + str(espion.call) + " fois.")
        return fonction(*args, **kwargs)
    espion.call = 0
    return espion

@compteur
def decoree():
    return "Je décore";

decoree();
decoree();
decoree();
decoree();decoree();
decoree();
decoree();

