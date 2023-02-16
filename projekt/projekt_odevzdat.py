import tkinter as tk
from generator import Generujheslo
from uklad import ulozit

class GUI(tk.Tk):
    """
    Třída GUI je grafické rozhraní pro generátor hesel. Umožňuje uživateli zadávat slova, která mají být použita pro generování
    hesla, zadat počet hesel, která se mají vygenerovat, vygenerovat hesla a uložit vygenerovaná hesla do úložiště.
    souboru.
    """
    def __init__(self):
        """
        Inicializuje třídu GUI a nastaví grafické uživatelské rozhraní.
        """
        super().__init__()   

        self.geometry("600x600")

        vstup_text = tk.Label(self, text="slova oddelana carkou:")
        vstup_text.pack()
        self.vstup = tk.Entry(self, width=40)
        self.vstup.pack()

        pocet_hesel = tk.Label(self, text="pocet hesel:")
        pocet_hesel.pack()
        self.pocet = tk.IntVar(value=1)
        spinbox_pocet_hesel = tk.Spinbox(self, from_=1, to=10, textvariable=self.pocet)
        spinbox_pocet_hesel.pack()

        vytvor_button = tk.Button(self, text="vytvor hesla", command=self.vytvor_hesla)
        vytvor_button.pack()

        uloz_button = tk.Button(self, text="Uloz hesla", command=self.uloz_hesla)
        uloz_button.pack()

        exit_button = tk.Button(self, text="Ukoncit", command=self.quit)
        exit_button.pack()

        self.checkboxes = []
    
    def vytvor_hesla(self):
        """
        Generuje hesla na základě zadaných slov a počtu hesel.
        """
        slova = self.vstup.get().split(",")
        generator = Generujheslo(slova)
        hesla = [generator.generate() for i in range(self.pocet.get())]
        for heslo in hesla:
            pom = tk.StringVar(value=heslo)
            cb_var = tk.BooleanVar()
            cb = tk.Checkbutton(self, textvariable=pom, variable=cb_var)
            cb.pack()
            self.checkboxes.append((cb, pom, cb_var))
    
    def uloz_hesla(self):
        """
        Uloží vybraná hesla (podle checkboxu) do textového souboru.
        """
        uloziste =ulozit("hesla.txt")
        hesla = [pom.get() for cb, pom, cb_var in self.checkboxes if cb_var.get()]
        uloziste.save(hesla)

