
class ClassTest:
     def hello(self):
         print("hello")
     # @classmethod
     # def class_method(cls):
     #     print("called class method")
     @staticmethod
     def  static_method():
           print("called static method")


# classTest=ClassTest()
# classTest.hello()
# ClassTest.hello(classTest)
# ClassTest.class_method()
ClassTest.static_method()

#  interview question