
def is_valid_brackets(expression : str) -> bool: # проверяет правильность расстановки скобок в выражении
    stack = []
    brackets = {')':'(', '}':'{',']':'['}
    for letter in expression:
        if letter in brackets.values():
            stack.append(letter)
        if letter in brackets.keys():
            if not stack or stack.pop() != brackets[letter]:
                return False
    return not stack


print(is_valid_brackets("(]2+3)["))
print(is_valid_brackets("(2+{3*9})"))
print(is_valid_brackets("((2+3)"))
print(is_valid_brackets(")2+(2+3)("))
# 성년 시간
