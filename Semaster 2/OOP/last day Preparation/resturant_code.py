class Resturant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describeRestaurant(self):
        print(f"{self.name} serves {self.cuisine} food.")

    def openResaurant(self):
        print(f"{self.name} is open.")