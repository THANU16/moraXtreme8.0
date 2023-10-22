    subString=""
        for i in range(length):
            temp = codeword[length :length+i+1]
            if(temp in string):
                subString = temp
            else:
                break
        if(p*len(subString)<q):
            string = string + subString
            cost += p*len(subString)
        else:
            string = string + subString
            cost += q