import FileReader as fReader
import BTree as BT

data = fReader.readCSVFile()
print ("yrhenertuytreyh")

B = BT.BTree(3)

print("Inserted 1,a")
B.insert((1,"z"))
B.insert((1,"zz"))
B.insert((1,"zzz"))
B.insert((1,"zzzz"))
B.insert((1,"zzzzz"))
B.print_tree(B.root)

print("--------------------------")
print("Inserted 1,a")
B.insert((2,"h"))
B.print_tree(B.root)
print("--------------------------")
print("Inserted 1,a")
B.insert((3,"g"))
B.print_tree(B.root)
print("--------------------------")
print("Inserted 1,a")
B.insert((3,"z"))
B.print_tree(B.root)
print("--------------------------")
print("Inserted 1,a")
B.insert((4,"f"))
B.print_tree(B.root)
print("--------------------------")
print("Inserted 1,a")
B.insert((5,"e"))
B.print_tree(B.root)
print("--------------------------")
print("Inserted 1,a")
B.insert((6,"d"))
B.print_tree(B.root)
print("--------------------------")
print("Inserted 1,a")
B.insert((7,"c"))
B.print_tree(B.root)
print("--------------------------")
print("Inserted 1,a")
B.insert((8,"b"))
B.print_tree(B.root)
print("--------------------------")
print("Inserted 1,a")
B.insert((9,"a"))
B.print_tree(B.root)
print("--------------------------")

print("Deleted 8,b")
B.delete(B.root, (8,"b"))
B.print_tree(B.root)

Obtained = B.find_key(B.root, 1)
print("trehjyrjereyj")
