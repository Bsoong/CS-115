'''
Created on Oct 23, 2017

@author: brand
I pledge my honor that I have abided by the Stevens Honor System-- Bsoong
'''


def numToBaseB(N,B):
    """Uses a helper function to convert a number into a base of the input choosing."""
    if N==0:
        return '0'
    def numToBaseB_helper(N,B):
        if N == 0:
            return ''
        return numToBaseB(N//B,B)+str(N%B)
    return numToBaseB_helper(N,B)
print(numToBaseB(36, 4))

def baseBToNum(S, B):
    """Uses a helper with an incrementing exponent and a constant base to convert the string into the number value"""
    if S == '':
        return 0
    def helper(S,B, ex):
        if S == '':
            return 0
        return helper(S[:-1],B, ex+1) + int(S[-1]) * (B**ex)
    return helper(S, B, 0)

def baseToBase(B1, B2, SinB1):
    """Uses a helper function to remove the extra zero on it. Uses a variable so that the helper can run, and then calls the variable as the last result.
    By using previous functions your're able to convert it into whatever base is needed."""
    result = numToBaseB(baseBToNum(SinB1, B1),B2)
    def baseTobase_helper(result):
        if result[0] == '0':
            return baseTobase_helper(result[1:])
        return result
    return baseTobase_helper(result)

def add(S,T):
    """Uses a helper function to remove the extra zero on it. Uses a variable so that the helper can run, and then calls the variable as the last result.
    By using baseBtoNum, you convert the bases back into numbers, add them, and then convert the answer to the two back into base."""
    result = numToBaseB(baseBToNum(S, 2)+baseBToNum(T, 2), 2)
    def add_helper(result):
        if result[0] == '0':
            return add_helper(result[1:])
        return result
    return add_helper(result)



FullAdder = {
    ('0','0','0') : ('0','0'),
    ('0','0','1') : ('1','0'),
    ('0','1','0') : ('1','0'),
    ('0','1','1') : ('0','1'),
    ('1','0','0') : ('1','0'),
    ('1','0','1') : ('0','1'),
    ('1','1','0') : ('0','1'),
    ('1','1','1') : ('1','1') 
    }

def addB(S1, S2):
    """Uses a helper and specific base cases to create variables that use the FullAdder to match the desired three variable outputs."""
    def addB_helper(S1, S2, carry):
        if S1 == "" and S2 == "":
            if carry == "0":
                return ""
            return "1"
        if S1 == "":
            sum, carrier = FullAdder[('0', S2[-1], carry)]
        elif S2 == "":
            sum, carrier = FullAdder[(S1[-1], "0", carry)]
        else:
            sum, carrier = FullAdder[(S1[-1], S2[-1], carry)]
        return addB_helper(S1[:-1], S2[:-1], carrier)+sum 
    return addB_helper(S1, S2, "0")


    
            
            
            
            
    
   