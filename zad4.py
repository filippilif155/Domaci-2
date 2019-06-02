def doors(n):
    from functools import reduce
    vrata = ["1"] * int(n)
    i = 2
    while i != int(n) + 2:
        for index in list(range(i-1, int(n))):
            if  (index + 1) % i == 0:
                if vrata[index] == '1':
                    vrata[index] = '0'
                else:
                    vrata[index] = '1'
                    
        i += 1
    #print(int(reduce(lambda x, y: x + y, vrata))) #Koja su vrata otvorena 0 -> zatvoreno 1 -> otvoreno
    return int(reduce(lambda x, y: int(x) + int(y), vrata))
print(doors(5))
n = input("Unesite broj vrata:\n")
print(doors(n))