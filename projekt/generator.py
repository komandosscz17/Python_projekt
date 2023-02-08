
import random
import string

class Generujheslo:
    def __init__(self, slova):
        self.slova = slova
    
    def generate(self):
        heslo = "".join([slovo[:len(slovo)//2] + slovo[len(slovo)//2 + 1:].capitalize() for slovo in random.sample(self.slova, 2)])
        heslo += str(random.randint(0, 100))
        heslo += "".join(random.choice(string.ascii_letters + string.digits) for i in range(3))
        return heslo