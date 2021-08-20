List=[5,10,15,20,25,50,20]
def my_list(List):
    i = 0
    for i in range (len(List)):
        if List[i]==20:
            List[i]=200
    print(List)
my_list(List)