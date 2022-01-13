def PalindromeTwo(strParam):
    
    alfabets=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","w","v","x","y","z"]
    
    strParam=strParam.lower()
    s=""
    l=len(strParam)
    
    for i in range (l):
        if strParam[i] in alfabets :
            s=s+strParam[i]
    
    ls=len(s)
    temp=0
    
    for i in range (ls):
        if[i]==s[ls-i-1]:
            temp=temp+1
            
    if temp==ls :
        return True
    else :
        return False
    
    print(PalindromeTwo("Bonjour comment ça va ?"))

