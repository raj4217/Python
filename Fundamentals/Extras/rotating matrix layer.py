def matrixRotation(matrix, r, c, k):
    layers = min(r, c) // 2
    rings = []
    for l in range(layers):
        ring = [mat[l][j] for j in range(l, c - l)]\
            + [mat[j][c - l - 1] for j in range(l + 1, r - l)]\
            + [mat[r - 1 - l][j] for j in range(c - 2 - l, l - 1, -1)]\
            + [mat[j][l] for j in range(r - 2 - l, l, -1)]
        rings.append(ring)

    for i, ring in enumerate(rings):
        rings[i] = ring[k:] + ring[:k]

    new_mat = mat.copy()
    for l in range(layers):
        for j in range(l, c - l):
            new_mat[l][j] = rings[l][0]
            del rings[l][0]
        for j in range(l + 1, r - l):
            new_mat[j][c - l - 1] = rings[l][0]
            del rings[l][0]
        for j in range(c - 2 - l, l - 1, -1):
            new_mat[r - 1 - l][j] = rings[l][0]
            del rings[l][0]
        for j in range(r - 2 - l, l, -1):
            new_mat[j][l] = rings[l][0]
            del rings[l][0]

    for i in new_mat:
        print(" ".join(map(str, i)))


mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
matrixRotation(mat, 4, 4, 1)
