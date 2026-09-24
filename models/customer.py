class customer:

    def __init__(self, mobileNumber):
        self.mobileNumber = mobileNumber
    def display(self):
        print("Mobile Number:",self.mobileNumber)
       
customer1=customer("9567789302")
customer1.display()
