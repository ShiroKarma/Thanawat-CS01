get = int(input('คะเเบบเก็บ : '))
midtest = int(input('คะเเนนสอยกลางภาค : '))
FinalTest = int(input('คะเเนนสอบปลายภาค : '))
if get >= 0 and get <= 30 :
    if midtest >= 0 and midtest <= 30 :
        if FinalTest >= 0 and FinalTest <= 4300 :
            All = get+midtest+FinalTest
            if All <=100 :
                if All >= 80 and All <=100:
                    print('A')
                elif All >= 75 and All <= 79 :
                    print('B+')
                elif All >= 70 and All <= 74 :
                    print('B')
                elif All >= 65 and All <= 69 :  
                    print('C+')
                elif All >= 60 and All <= 64 :
                    print('C') 
                elif All >= 55 and All <= 59 :
                    print('D+')
                elif All >= 50 and All <= 54 :
                    print('D')        
                else :
                    print('F')
            else :
                print('Error')  
        else:
            print("Error")
    else:
        print('Error')
else :
    print("error") 