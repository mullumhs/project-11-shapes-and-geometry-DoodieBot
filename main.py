from shapes import Shape, Rectangle, Circle

def calc_circle():
    radius=int(input("please enter the radius of your circle: "))
    c = Circle(radius)
    print(c.calculate_area())
    print(c.calculate_circumference())
    print(c.calculate_diameter())

def calc_rectangle():
    input1=input("please enter the height of your Rectangle: ")
    input2=input("please enter the length of your Rectangle: ")
    r = Rectangle(input1, input2 )
    print(f" the area of your rectangle is {r.calculate_area()}")
    print(f" the perimeter of your rectangle{r.calculate_parameter()}")
    
chose=input("select 1 for circle or 2 for rectangle: ")
if chose == "1":
    calc_circle()
elif chose == "2":
    calc_rectangle()
