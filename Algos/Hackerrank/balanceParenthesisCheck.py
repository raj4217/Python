def balance_check(s):
    if len(s) % 2 != 0:
        return False
    bracks = {')': '(', '}': '{', ']': '['}
    st = []
    for item in s:
        if item in bracks.values():
            st.append(item)
        else:
            if len(st) < 1:
                return False
            if bracks[item] != st.pop():
                return False
    return True
