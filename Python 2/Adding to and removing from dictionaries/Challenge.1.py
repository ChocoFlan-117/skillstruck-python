#Dictionary of Shapes

new_shape = input("New shape: ")
new_height = int(input("New height: "))

shapes = {

"Triangle": 8,

"Circle": 15,

"Square": 10,

"Rectangle" : 12

}

shapes[new_shape] = new_height

print(shapes)