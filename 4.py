import pprint
massages = "O curva ja perdole, co tu ribuh tuit padlo"
count = {}

for charekter in massages:
    print (charekter)
    count.setdefault(charekter, 0)
    count[charekter] += 1
pprint.pprint (count)    

