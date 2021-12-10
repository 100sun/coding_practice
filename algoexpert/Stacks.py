# Feel free to add new properties and methods to the class.
class MinMaxStack:
    def __init__(self):
        from collections import deque
        self.stack = deque()

    def peek(self):
        return self.stack[-1]

    def pop(self):
        return self.stack.pop()

    def push(self, number):
        return self.stack.append(number)

    def getMin(self):
        return min(self.stack)

    def getMax(self):
        return max(self.stack)


def sunsetViews(buildings, direction):
    runningMaxHeight = 0
    buildingsWithSunsetViews = []
    for idx in range(len(buildings)):
        curIdx = -idx - 1 if direction == 'EAST' else idx
        if runningMaxHeight < buildings[curIdx]:
            runningMaxHeight = buildings[curIdx]
            buildingsWithSunsetViews.append((len(buildings) + curIdx) % len(buildings))
    return sorted(buildingsWithSunsetViews)


def decodeString(s: str) -> str:
    from collections import deque
    stack = deque()
    digits, alphas = '', ''
    for letter in s:
        # print("letter: ", letter, "digits: ", digits, "\talphabets: ", alphabets, "\t\t\tstack: ", stack)
        if letter.isdigit():
            digits += letter
        elif letter.isalpha():
            alphas += letter
        elif letter == '[':
            stack.append((int(digits), alphas))
            digits, alphas = '', ''
        elif letter == ']':
            n_repeat, existed_str = stack.pop()
            alphas = existed_str + alphas * n_repeat
    return alphas

  
print(decodeString("2[abc]3[cd]ef"))
