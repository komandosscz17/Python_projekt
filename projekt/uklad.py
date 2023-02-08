class ulozit:
    def __init__(self, file_name):
        self.file_name = file_name
    
    def save(self, passwords):
        with open(self.file_name, "a") as file:
            for password in passwords:
                file.write(password + "\n")
