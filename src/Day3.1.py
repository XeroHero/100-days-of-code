#
# Example file for working with Classes
# 

# Self argument refers to instance of object. It is only passed when referring to functions in another class at declaration
class myClass():
    def method1(self):
        print("myClass method1")

    def method2(self, someString):
        print("myClass method2 " + someString)


# A class that inherits from myClass
class anotherClass(myClass):
    def method1(self):
        myClass.method1(self)
        print("anotherClass method1")

    def method2(self, someString):
        print("anotherClass method2 ")


def main():
    c = myClass()
    c.method1()
    c.method2("This is a string")

    c2 = anotherClass()
    c2.method1()
    c2.method2("This is a string!")

if __name__ == "__main__":
    main()
