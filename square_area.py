
#Finding square area of a shape, using OOP 

# Class for designing
class design:
    def topDesign(self):
        print("------------------------")
        print("... Find square Area ...")
        print("------------------------")

# Class for data and operationss
class data_and_operations:
    def lenWid(self):
        self.len
        self.wid

    def getInputs(self):
        self.len = input("Enter length in feet : ")
        self.wid = input("Enter width in feet : ")
        self.convert_len = int(self.len)
        self.convert_wid = int(self.wid)
    
    def formula(self):
        self.f = self.convert_len *self.convert_wid
        print(f"Area is : {self.f}")

# Class for viewing 
class view(data_and_operations):
    def getResult(self):
        self.getInputs()
        self.formula()


# Creating object for design class
obj_design = design()
obj_design.topDesign()

# Creating object for view class
obj_view = view()
obj_view.getResult()