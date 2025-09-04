class solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        ops = {'+', '-', '*', '/'}
        for token in tokens:
            if token in ops:
                b = token.pop()
                a = token.pop()
                if token == '+':
                    res = a + b
                elif token == '-':
                    res = a - b
                elif token == '*':
                    res = a * b
                else:
                    res = int(a / b)
                stack.append(res)
            else:
                stack.append(int(token))
        return stack[-1]

