

def panagram(s):
    alphabet= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
     'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in alphabet:
        if i not in s:
            return False
    return True 

def palindrome(s):
    temp=s
    rev=0
    while s!=0:
        digits=s%10
        rev=(rev*10)+digits
        s=s//10
    if temp == rev:
        return True
    else:
        return False

def pramaility (s):
    for i in range (2,s+1):
        for j in range (2,i):
            if i%j==0:
                return False
            else:
                return True

def frequency (s):
    dictinary = dict()
    for key in s:
        if key not in dictinary:
            dictinary[key] = 1
        else:
            dictinary[key] += 1
    return dictinary

