#postfix to prefix

def isOperand(x):
    return ((x >= 'a' and x <= 'z') or
            (x >= 'A' and x <= 'Z')) 

def getInfix(exp) :
 
    s = [] 
 
    for i in exp:     
         
        # Push operands 
        if (isOperand(i)) :         
            s.insert(0, i) 
             
 
        else:
         
            op1 = s[0] 
            s.pop(0) 
            op2 = s[0] 
            s.pop(0) 
            s.insert(0, "(" + op2 + i + op1 + ")") 
             
 
    return s[0]


exp = "ab*cd^+kt/-"
print(getInfix(exp.strip()))

# Python code to convert infix to prefix expression


# Function to check if the character is an operator
def isOperator(c):
	return (not c.isalpha()) and (not c.isdigit())



# Function to get the priority of operators
def getPriority(c):
	if c == '-' or c == '+':
		return 1
	elif c == '*' or c == '/':
		return 2
	elif c == '^':
		return 3
	return 0



# Function to convert the infix expression to postfix
def infixToPostfix(infix):
	infix = '(' + infix + ')'
	l = len(infix)
	char_stack = []
	output = ""

	for i in range(l):
		
		# Check if the character is alphabet or digit
		if infix[i].isalpha() or infix[i].isdigit():
			output += infix[i]
			
		# If the character is '(' push it in the stack
		elif infix[i] == '(':
			char_stack.append(infix[i])
		
		# If the character is ')' pop from the stack
		elif infix[i] == ')':
			while char_stack[-1] != '(':
				output += char_stack.pop()
			char_stack.pop()
		
		# Found an operator
		else:
			if isOperator(char_stack[-1]):
				if infix[i] == '^':
					while getPriority(infix[i]) <= getPriority(char_stack[-1]):
						output += char_stack.pop()
				else:
					while getPriority(infix[i]) < getPriority(char_stack[-1]):
						output += char_stack.pop()
				char_stack.append(infix[i])

	while len(char_stack) != 0:
		output += char_stack.pop()
	return output



# Function to convert infix expression to prefix
def infixToPrefix(infix):
	l = len(infix)

	infix = infix[::-1]

	for i in range(l):
		if infix[i] == '(':
			infix[i] = ')'
		elif infix[i] == ')':
			infix[i] = '('

	prefix = infixToPostfix(infix)
	prefix = prefix[::-1]

	return prefix




s = exp

# Function call
print(infixToPrefix(s))
