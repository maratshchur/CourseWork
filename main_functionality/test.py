
def check(test):
    if test[0] != "<" or test[-1] != ">":
        return False
    testlist = test[1:-1].split("><")
    for s in testlist:
        if "<" in s or ">" in s or "/" in s[1:]:
            return False
    q = []
    for s in testlist:
        if s[0] != '/':
            q.append(s)
        elif not q or q.pop() != s[1:]:
            return False
    if q:
        return False
    return True

def solve(s):
    alph = "qwertyuiopasdfghjklzxcvbnm<>/" 
    for i in range(len(s)):
        for c in alph:
            test = s[:i] + c + s[i+1:]
            if check(test):
                return test
               
s=input()
print(solve(s))
