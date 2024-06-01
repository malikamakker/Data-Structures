def is_operand(ch: str) -> bool:
    return ch.isalpha() or ch.isdigit()

def infix_to_postfix(infix):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    postfix = []

    for char in infix:
        if is_operand(char):
            postfix.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            if stack[-1] == '(':
                stack.pop()
        else:
            while stack and precedence.get(stack[-1], 0) >= precedence.get(char, 0):
                postfix.append(stack.pop())
            stack.append(char)        
    
    while stack:
        postfix.append(stack.pop())
    return ''.join(postfix)

infix = "a+b*(c^d-e)^(f+g*h)-i"
print(infix_to_postfix(infix)) # abcd^e-fgh*+^*+i-
