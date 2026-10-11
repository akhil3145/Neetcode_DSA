class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for n in asteroids:
            alive = True
            while stack and stack[-1]>0 and n<0:
                if stack[-1]<abs(n):
                    stack.pop()
                elif stack[-1] == abs(n):
                    stack.pop()
                    alive = False
                    break
                else:
                    alive = False
                    break
            if alive:
                stack.append(n)
        return stack