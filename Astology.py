import pyaztro as py
#creating our Astrology class
class Astrology:
    #creating our self object
    def __init__(self,zsign):
         self.zsign = zsign

    #Characteristics function
    def Characteristics(self):
        sign_char = py.Aztro(sign=self.zsign)
        print(sign_char.description)
        print('You are feeling',sign_char.mood,'.')
        print('You are compatible with',sign_char.compatibility,'.')






Zodiac_sign = Astrology('Cancer')
Zodiac_sign.Characteristics()
