List = ("Macka", "Pas", "Stol")

def fun1(List):
    for x in List:
        if len(x)>=4 and isinstance(x,str):
            return x
print(fun1(List))