class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        #val = min(val, self.minStack[-1] if self.minStack else val)
        
        if self.minStack:
            val = min(val, self.minStack[-1])
        else:
            val = val

        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
    
def main():
    input =  ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]

    minStack = MinStack()
    minStack.push(1)
    minStack.push(2)
    minStack.push(0)
    print(minStack.getMin()) # return 0
    minStack.pop()
    print(minStack.top())    # return 2
    print(minStack.getMin()) # return 1

if __name__ == "__main__":
    main()