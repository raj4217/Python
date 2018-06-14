def balance_check(s):

    # Check is even number of brackets
    if len(s) % 2 != 0:
        return False

    brackets = {')': '(', '}': '{', ']': '['}

    stack = []
    # Check every parenthesis in string
    for paren in s:
        if paren in brackets.values():
            stack.append(paren)
        else:
            if brackets[paren] != stack.pop():
                return False
    return True


print(balance_check('[]'))
