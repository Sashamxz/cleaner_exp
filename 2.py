cat_name = []

while True:
    print("Please type your cat name: " + str(len(cat_name) + 1) +
          "or enter 'q' or nothing to stop: ")  
    name = input()
    if name == "q":
        break
    cat_name = cat_name + [name]
print ("the cat name are: ")    
for name in cat_name:
    print (" " + name)
