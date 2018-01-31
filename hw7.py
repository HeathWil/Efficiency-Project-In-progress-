
#check if number is prime
def prime(num):
    if (num == 2):
        return True

    for i in range(2, num):
        if (num % i)==0:
            return False
        else:
            return True


def primegen(num):
    list=range(1,num)
    for i in list:
        if prime(i) == True:
            yield(i)



def power3(num):
    temp=num
    while(temp % 3 ==0):
        temp/=3
    return temp==1


#check if number is power3

def power3gen(num):
    list = range(3, num)
    for i in list:
       if power3(i) == True:
           yield (i)


#check if interesting
def isInteresting(num):
    list3=power3gen(num)
    listp=primegen(num)
    for i in listp:
        for j in list3:
            if i + j == num:
                return True
    return False


#yields all interesting nums increasing order greater than n
#use interesting in generator
def interestGen(base, amount):
    temp=base
    for i in range(amount):
        while isInteresting(temp)== False:
            temp+=1
        if isInteresting(temp) == True:
            yield(temp)
            temp+=1










temp1=interestGen(113049801*10,20)

for i in temp1:
    print(i)

