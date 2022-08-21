class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")
        
    # def __str__(self) -> str:
    #     self.instance_method
    
    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")
        
    @staticmethod
    def static_method():
        print("Class static_method.")
        
test = ClassTest()
test.instance_method()
ClassTest.instance_method(test)

ClassTest.class_method()

ClassTest.static_method()