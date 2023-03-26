def interleave(*params):
    max_len = max(len(param) for param in params)
    res = []
    for i in range(max_len):
        for param in params:
            if i < len(param):
                res.append(param[i])
    return res


print(interleave('abc', [1, 2, 3], ('!', '@', '#')))
