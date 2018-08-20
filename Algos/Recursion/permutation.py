# def permute(s):
#     out = []
#     if len(s) == 1:
#         return s
#     for i, j in enumerate(s):
#         for p in permute(s[:i] + s[i + 1:]):
#             # out.append(j+p)
#             out += [j + p]
#     return out


# print(permute('abc'))


from itertools import permutations

# Get all permutations of [1, 2, 3]
perm = permutations([1, 2, 3])

# Print the obtained permutations
for i in perm:
    print(i)
