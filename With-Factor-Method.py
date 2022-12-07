class EnglishTranslator:

    #returns the message as is because it is given in english

    def translate(self,msg):
        return msg

class FrenchTranslator:

    #the translations are different and are returned in french
    def __init__(self):
        self.translations = {"Yes":"Oui" , "No":"Non"}

    def translate(self,msg):
        return self.translations.get(msg,msg)

class GermanTranslator:
    
     #the translations are different and are returned in german
     def __init__(self):
        self.translations = {"Yes":"Ja" , "No" : "Nein"}

     def translate(self,msg):
        return self.translations.get(msg,msg)

def Factory(language ="English"):
 
    """Factory Method"""
    translators = {
        "English": EnglishTranslator,
        "French": FrenchTranslator,
        "German": GermanTranslator,
    }
 
    return translators[language]()

if __name__ == "__main__":
 
    # main method to call others
    e = Factory("English")
    f = Factory("French")
    g = Factory("German")
 
    # list of strings
    message = ["Yes" , "No"]
 
    for msg in message:
        print(e.translate(msg))
        print(f.translate(msg))
        print(g.translate(msg))