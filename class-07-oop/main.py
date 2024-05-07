# abstraction

class User:
    def __init__(self, name, cpf):
        self.name = name
        self.__cpf = cpf

    def get_cpf(self):
        return self.__cpf  

    def info(self): # polymorphism
        return (self.name, self.get_cpf(), self.__cpf)
    
user = User("Eric", "000.000.000-00")
print(user.name)
# user.cpf = "xxxx"
# print(user.__cpf)
print(user.info())

# inheritance

class Admin(User):
    def __init__(self, name, cpf):
        super().__init__(name, cpf)
        self.__status = "admin"

    def set_status(self, status):
        self.__status = status

    def get_status(self):
        return self.__status
    
    def info(self):
        return (self.name, self.get_cpf(), self.__status)

admin = Admin("Luiza", "111.111.111-11")
print(admin.name)
print(admin.get_status())
admin.set_status("default")
print(admin.get_status())
print(admin.info())