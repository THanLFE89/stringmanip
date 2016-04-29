from TestingPackage.MyStringS9 import MyString
s=MyString("Development")
print(s.indexOf(c="D"))


def indexOf(self,c):
    b=len(self.str)-1
    while b>=0:
        if self.str[d]==c:
            return self.str[d]