# single inheritence
class grandparent:
    def __init__(self):
        print('parent class constructor')

    def welcome(self):
        print('say hello')

    def property(self):
        print('property')
class parent(grandparent):
    def __init__(self):
        print('parent class constructor')

    def hello(self):
        print('say hello')
    def  sayHello(self):
        print('hello budy')

class Child (parent):

    def __init__(self):
        print('child class constructor')

    def bye(self):
        print('say hello')

# create a object ob the child class
child1=Child()
child1.hello()
child1.bye();
child1.property()
child1.sayHello();