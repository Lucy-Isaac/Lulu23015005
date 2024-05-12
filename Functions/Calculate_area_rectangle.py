def calulate_area_rectangle(Length, Width):
    Area = Length * Width
    return Area

Length = int(input("Enter the length of the rectangle: "))
Width = int(input("Enter the width of the rectangle: "))
result = calulate_area_rectangle(Length, Width)
print(result)
