
def concat_str(strarr, i, k):
    r = ""
    for c in range(i, i+k):
        r += strarr[c]
    return r


def longest_consec(strarr, k):
    r = concat_str(strarr, 0, k)
    l = len(r)
    for i in range(len(strarr) - (k-1)):
        a = concat_str(strarr, i, k)
        b = len(a)
        if l < b:
            r = a
            l = len(r)
    return r


print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2))
