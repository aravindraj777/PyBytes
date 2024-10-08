class Car:
    
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale


    

    def drive(self):
        print(f"You drive the {self.model}")  
   
   
   # car1 = Car("Mustang",2024,"red",False)
# car2 = Car("Corvete", 2025, "blue",True)

# print(car1.model)       