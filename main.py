from shapes import Shape, Rectangle

input1=input("please enter the height of your Rectangle")
input2=input("please enter the length of your Rectangle")

r = Rectangle(input1, input2 )
print(r.calculate_area())
print(r.calculate_parameter)