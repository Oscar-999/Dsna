class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == '+':
                stack.append(stack[-1]+stack[-2])
            elif op == 'D':
                stack.append(stack[-1]*2)
            elif op == 'C':
                stack.pop()
            else:
                stack.append(int(op))

        return sum(stack)


When should we use stack?
1. When we want to ensure a system does not move onto another action before completing those before it.
2. When we want to do something in reverse order.
3. When we want to implement an undo/redo feature.
4. When we want to backtrack in searching algos (e.g path finding in a maze)
5. When we use recursion; it utilizes the call stack
