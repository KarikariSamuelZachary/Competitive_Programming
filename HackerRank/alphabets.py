def swap_case(s):
    temp = ""
    
    for i in s:
        if i.isalpha():
            if i.isupper():
                temp += i.lower()
                
            elif i.islower():
                temp += i.upper()
        else:
            temp += i
    return temp
            
if __name__ == '__main__':
    s = input()
    result = swap_case(s)   
    print(result)