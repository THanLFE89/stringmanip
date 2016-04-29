class MyString():
    def __init__(self, str=""): # initializes  the object
        self.str=str

    #Returns the current string.

    def getString(self):
        return self.str

    #Returns a string that consists of all and only the vowels in the current string.
    #Only letters a, e, i, o, and u (both lower and upper case) are considered vowels.
    #The returned string contains each occurrence of a vowel in the current string.
    def getVowels(self):
        lowercase=self.str
        lowercase=lowercase.lower()
        vowels=""
        count=len(lowercase)
        for a in range(0,count):
            if lowercase[a]=='a'or lowercase[a]=='e' or lowercase[a]== 'i' or lowercase[a]=='o' or lowercase[a]== 'u':
                vowels=vowels+self.str[a]
        return vowels

    #Returns a string that consists of the substring between start and end indexes (both included) in the current string.
    #Index 1 corresponds to the first character in the current string.'''
    def getSubstring(self,a,b):
        substring=""
        try:
            for d in range(a,b+1):
                substring=substring+self.str[d]
            return substring
        except:
            print("Invalid Range")
    #Breaks the string down, and returns it as a character string
    def getCharList(self):
        CharList=[]
        b = len(self.str) - 1
        for e in range(0,b+1):
            CharList.append(self.str[e])
        return CharList

    #Returns the index of the first occurrence of a character in the current string.
    #Index 1 corresponds to the first character in the current string.
    # return 0 if no match is found

    def indexOf(self, c):
        b = len(self.str)
        Valid = False
        while Valid == False:
            for d in range(1, b):
                if self.str[d] == c:
                    return self.str[d]

    # Removes all occurrences of the specified character from the current string.
    def removeChar(self,c):

        return 1


    #Invert the current string.
    def invert(self):
        invert=self.str[::-1]


        return 1
