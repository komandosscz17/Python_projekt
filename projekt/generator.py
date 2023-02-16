
import random
import string

class Generujheslo:
    """
    Třída Generujheslo je zodpovědná za generování náhodných hesel na základě seznamu slov zadaných uživatelem.
    """
    def __init__(self, slova):
        """
        Inicializuje třídu Generujheslo se seznamem slov.

        Parametry:
            words (List): Seznam slov, která se použijí při generování hesel.
        """
        self.slova = slova
    
    def generate(self):
        """
        Generuje náhodné heslo výběrem náhodného slova ze seznamu slov zadaného při inicializaci.

        Vrací:
            str: Vygenerované heslo sestávající z náhodného slova ze seznamu slov.
        """
        heslo = "".join([slovo[:len(slovo)//2] + slovo[len(slovo)//2 + 1:].capitalize() for slovo in random.sample(self.slova, 2)])
        heslo += str(random.randint(0, 100))
        heslo += "".join(random.choice(string.ascii_letters + string.digits) for i in range(3))
        return heslo