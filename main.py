#"()[]" -> valid, "([]" -> invalid
#"([])" -> valid, "()]["-> invalid, "([)]" ->invalid

#"()" -> correct
#"[]" -> correct ##<-----
#"()()" -> correct
#"[]()()()()()()()()"
#"([])"
#"([][]()()()()()()()())"
def check_string(st):
    if len(st)%2 !=0: # len= 1,3,5,7,9, odd number
        return False
    else: # the len must be even number
        keys_text = {
            "(": ")",
            "[":"]"
        }
        for k in keys_text:
            if k == st[0] && keys_text[k] == st[1]: #(  == ( && )  ==]
                if len(st)>2: #4
                    st = [2:] #st=])
                else:
                    return True
            if k == st[0] && keys_text[k] == st[-1]: #if ( == ( && ) = )
                if len(st)>2:
                    st = [1:-1] # []
                else:
                    return True
        if len(st)>0:
            check_string(st)



# // Example test:   'aaBabcDaA'
#         // WRONG ANSWER (got D expected B)
#         //
#         // Example test:   'Codility'
#         // WRONG ANSWER (got C expected NO)
#         //
#         // Example test:   'WeTestCodErs'
#         // WRONG ANSWER (got W expected T)

def solution(S):
    occ = {}
    for ii in S.lower():
        occ[ii] = 1 if ii not in occ else occ[ii] + 1

    print(occ)
    newS = ''
    for ii in occ:
        if occ[ii]>1:
            newS+=ii

    largS = 'NO'
    if len(newS)>1:
        largNum = 0
        for ii in newS:
            if ord(ii) > largNum:
                largS = ii
                largNum = ord(ii)

    return largS.upper()


solution('aaBabcDaA')  # expected B
solution('Codility') # expected NO
solution('WeTestCodErs')  # expected T
