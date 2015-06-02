
def strFind(s, d):
    i = 0
    j = 0

    while i + j < len(d):
        if s[j] == d[i+j]:
            j += 1
            if j >= len(s):
                return i
        else:
            i += 1
            j = 0

    return -1

print "cd, abcde"
print strFind("cd", "abcde")

print "cg, abcde"
print strFind("cg", "abcde")
