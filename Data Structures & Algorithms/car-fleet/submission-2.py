'''
go through list and  do (target - position) / speed

problem is that we need to sort because the 1st car may be further than 2nd (they are not in order)
'''


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)

        stack = []

        for p, s in cars:
            temp = (target-p)/s
            stack.append(temp)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)