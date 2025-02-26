#prefix to postfix
def prefixToInfix(prefix):
    stack = []
    
    # read prefix in reverse order
    i = len(prefix) - 1
    while i >= 0:
        if not isOperator(prefix[i]):
            
            # symbol is operand
            stack.append(prefix[i])
            i -= 1
        else:
          
            # symbol is operator
            str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
            stack.append(str)
            i -= 1
    
    return stack.pop()

def isOperator(c):
    if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
        return True
    else:
        return False


str = "-+*ab^cd/kt"
print(prefixToInfix(str))
    
# This code is contributed by avishekarora


# Function to return precedence of operators
def prec(c):
    
    if c == '^':
        return 3
    elif c == '/' or c == '*':
        return 2
    elif c == '+' or c == '-':
        return 1
    else:
        return -1

# Function to perform infix to postfix conversion
def infixToPostfix(s):
    st = []
    result = ""

    for i in range(len(s)):
        c = s[i]

        # If the scanned character is
        # an operand, add it to the output string.
        if (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or (c >= '0' and c <= '9'):
            result += c

        # If the scanned character is an 
        # ‘(‘, push it to the stack.
        elif c == '(':
            st.append('(')

        # If the scanned character is an ‘)’,
        # pop and add to the output string from the stack 
        # until an ‘(‘ is encountered.
        elif c == ')':
            while st[-1] != '(':
                result += st.pop()
            st.pop()

        # If an operator is scanned
        else:
            while st and (prec(c) < prec(st[-1]) or prec(c) == prec(st[-1])):
                result += st.pop()
            st.append(c)
    
    # Pop all the remaining elements from the stack
    while st:
        result += st.pop()

    print(result)

exp = prefixToInfix(str)
infixToPostfix(exp)
