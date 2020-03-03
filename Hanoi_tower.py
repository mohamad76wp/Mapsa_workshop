# # __author__ mohamad76wp

rod_a = [3, 2, 1]

rod_b = []

rod_c = []
print("a",rod_a)
print("b",rod_b)
print("c",rod_c)
print("")

rod_c.append(rod_a[2])
del rod_a[2]
print("a",rod_a)
print("b",rod_b)
print("c",rod_c)
print("")

rod_b.append(rod_a[1])
del rod_a[1]
print("a",rod_a)
print("b",rod_b)
print("c",rod_c)
print("")
rod_b.append(rod_c[0])
del rod_c[0]
print("a",rod_a)
print("b",rod_b)
print("c",rod_c)
print("")

rod_c.append(rod_a[0])
del rod_a[0]
print("a",rod_a)
print("b",rod_b)
print("c",rod_c)
print("")

rod_a.append(rod_b[1])
del rod_b[1]
print("a",rod_a)
print("b",rod_b)
print("c",rod_c)
print("")

rod_c.append(rod_b[0])
del rod_b[0]
print("a",rod_a)
print("b",rod_b)
print("c",rod_c)
print("")

rod_c.append(rod_a[0])
del rod_a[0]
print("a",rod_a)
print("b",rod_b)
print("c",rod_c)
print("")
