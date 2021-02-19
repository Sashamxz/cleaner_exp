allGuest = {'Alise' : {'appls': 5, 'banana':5},
            'Bob'   : {'cakes' : 5, 'banana' : 5},
            'Curl'  : {'appls': 10, 'sucsses' : 5}
           }


def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
        
    return numBrought

#print(' - apples     ' + str(totalBrought(allGuest,'appls')))    

aplls = totalBrought(allGuest,'appls')
print ("total appls - " + str(aplls)) 