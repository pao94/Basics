def find(getal):

    if(getal % 3 == 0): print(3**(getal/3))
    if(getal % 3 == 1): print(4*3**((getal-4)/3))
    if(getal % 3 == 2): print(2*3**((getal-2)/3))

find(23)