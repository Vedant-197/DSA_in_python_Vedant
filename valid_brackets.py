def is_valid(str):
    st = []

    for i in str:
        if (i == '(') or (i == '{') or (i == '['):
            st.append(i)
        else:
            if len(st) == 0:
                return False

            if (   (st[-1] == '(' and i == ')')   
                or (st[-1] == '{' and i == '}') 
                or (st[-1] == '[' and i == ']') ):
                st.pop()
            else:
                return False
            
    return len(st)  == 0

str = input("Enter Parentheses: ")

if is_valid(str):
    print("Valid Parentheses ")
else :
    print("Invalid parentheses")