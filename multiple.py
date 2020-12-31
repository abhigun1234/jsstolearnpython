class Person:

    def hello(self):
        print('hello')

class Student(Person):


    def bye(self):
        super().hello()


st=Student()
st.bye();