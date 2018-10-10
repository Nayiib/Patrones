class Singleton:
    # aqui se crea la instancia
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance 

    def __init__(self):
        """ Virtually private constructor. """
        if Singleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self

# un pequeño test

s = Singleton() # Ok
#Singleton() # execption
print s

s = Singleton.getInstance()
print s

s = Singleton.getInstance()
print s # imprimir la misma instancia que antes
