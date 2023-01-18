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
        
