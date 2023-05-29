#CS 3620 coding challenge 3
#Alexander Lustig

#-----------------------< P1 discount functions >---------------------
#student discount
def student_discount(price):
    return price - (price * 0.1)

#regular discount
def discount(price):
    return price - (price * 0.05)

price = 100
print("Price: " + str(price))
print("Double-discounted price: " +  str(discount(student_discount(price))))
print("\n")

#-----------------------< P2 lambda expression >---------------------
print("Lambda result: " + str((lambda x:x*(x+5)**2)(5)))
print("\n")

#-----------------------< P3 map discount function to cost list >---------------------
def item_discount(cost):
    return cost - (cost * 0.1)

item_costs = [1,3,5,7,9,100]

#map item_discount to item_costs
new_costs = list(map(item_discount, item_costs))

print("Original list: " + str(item_costs))
print("Discount list: " + str(new_costs))
print("\n")

#-----------------------< P4 computer class inheritence>---------------------
#base class
class Computer():
    model_name = "none"
    cost = -1

    def __init__(self, _model, _cost):
        self.model_name = _model
        self.cost = _cost

    def get_specs(self):
        return "model:{0}\tcost:{1}\n".format(self.model_name, self.cost)

    def display_specs(self):
        print(self.get_specs())

#desktop
class Desktop(Computer):
    size = "none"

    def __init__(self,_model,_cost,_size):
        self.model_name = _model
        self.cost = _cost
        self.size = _size

    def get_specs(self):
        return "model:{0}\tcost:{1}\tsize:{2}\n".format(self.model_name, self.cost, self.size)

    def display_specs(self):
        print(self.get_specs())

#laptop
class Laptop(Computer):
    weight = -1

    def __init__(self,_model,_cost,_weight):
        self.model_name = _model
        self.cost = _cost
        self.weight = _weight

    def get_specs(self):
        return "model:{0}\tcost:{1}\tweight:{2}\n".format(self.model_name, self.cost, self.weight)

    def display_specs(self):
        print(self.get_specs())

#instantiate
a = Computer("generic",1000)
b = Desktop("custom",1250,"mid-tower")
c = Laptop("asus",900,4.2)

#print
print("Computer, Desktop, Laptop")
a.display_specs()
b.display_specs()
c.display_specs()

#-----------------------< P5 operator overload >---------------------
class Values():
    a = -1
    b = -1

    def __init__(self,_a,_b):
        self.a = _a
        self.b = _b

    #overload * to act like +
    def __mul__(self, other):
        return Values(self.a + other.a, self.b + other.b)

#instantiate
first = Values(1,3)
second = Values(2,4)

#use overloaded *
result = first * second

print("overloaded *: ({0},{1}) * ({2},{3}) = ({4},{5}) ".format(first.a, first.b, second.a, second.b, result.a, result.b))