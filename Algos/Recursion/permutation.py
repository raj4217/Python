def permute(s):
    out = []
    if len(s) == 1:
        return s
    for i, j in enumerate(s):
        for p in permute(s[:i] + s[i + 1:]):
            # out.append(j+p)
            out += [j + p]
    return out


print(permute('abc'))
