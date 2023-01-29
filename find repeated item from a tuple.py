#3.repeated items from a tuple

tuple=(200,300,400,200,500,200)

for i in tuple:
    if tuple.count(i)>1:
        print(i)