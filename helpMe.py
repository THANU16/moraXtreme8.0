def minOpeningTime(codeword, l, p, q):
    string=codeword[0]
    cost = p

    while(len(string)<l):
        length = len(string)
        subString=""
        for i in range(length):
            temp = codeword[length :length+i+1]
            # print("temp",temp)
            if(subString==temp):
                break
            elif(temp in string):
                subString = temp
            else:
                if (len(temp) == 1):
                    subString = temp
                    break
                else:
                    break
        
        # print(subString)
        if(len(subString)==1):
            string = string + subString
            cost += p
        elif(p*len(subString)<q):
            string = string + subString
            cost += p*len(subString)
        else:
            string = string + subString
            cost += q
        # print(cost)
        # print(string)

    
    return cost



t = int(input())

for i in range(t):
    secondLine = input()
    l= list(map(int, secondLine.split()))[0]
    p = list(map(int, secondLine.split()))[1]
    q = list(map(int, secondLine.split()))[2]

    codeword = input()
    # print(codeword)
    print(minOpeningTime(codeword,l,p,q))