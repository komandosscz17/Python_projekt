class ulozit:
    """
    Třída Ulozit je zodpovědná za ukládání vygenerovaných hesel do textového souboru.
    """
    def __init__(self, file_name):
        """
        Inicializuje třídu Ulozit s názvem souboru.

        Parametry:
        file_name (str): Název souboru, do kterého se ukládají vygenerovaná hesla.
        """
        self.file_name = file_name
    
    def save(self, hesla):
        """
        Uloží seznam hesel do textového souboru.

        Parametry:
         hesla (List): Seznam hesel, která mají být uložena do souboru.
        """
        with open(self.file_name, "a") as file:
            for heslo in hesla:
                file.write(heslo + "\n")
