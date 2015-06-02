

def isP(s):
    l = 0
    r = len(s) -1

    while l<r:
        if not s[l].isalpha():
            l += 1
            continue
        if not s[r].isalpha():
            r -= 1 
            continue

        if s[l].lower() == s[r].lower():
            l += 1
            r -= 1
        else:
            return False

    return True


print "abc"
print isP("abc")
x = "A man, a plan, a canal: Panama"
print x
print isP(x)
