class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def isAdult(self):
        return self._age >= 18

    def greetAsRovarsprak(self):
        halsning = "Hej " + self._name;        
        return self._rovarsprak(halsning)


    def _rovarsprak(s):
        vocals = ['a', 'o', 'u', 'å', 'e', 'i', 'y', 'ä', 'ö']
        
        result = ""
        for ch in s:
            if ch in vocals:
                result = result + ch
            else:
                result = result + ch + "o" + ch
    
        return result        
    