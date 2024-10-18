from typing import List

def evalRPN(tokens: List[str]) -> int:
    stack = []
    for c in tokens:
        if c == "+":
            stack.append(stack.pop() + stack.pop())
        elif c == "-":
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif c == "*":
            stack.append(stack.pop() * stack.pop())
        elif c == "/":
            a, b = stack.pop(), stack.pop()
            stack.append(int(float(b) / a))
        else:
            stack.append(int(c))
    return stack[0]


tokens = ["1","2","+","3","*","4","-"]
print(evalRPN(tokens))