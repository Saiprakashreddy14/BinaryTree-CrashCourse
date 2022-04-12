def reorganizeString(s):
    a = sorted(sorted(s),key=s.count)
    h = len(a)//2
    a[1::2],a[::2] = a[:h],a[h:]
    if a[-1:]==a[-2:-1]:
        return ""
    return "".join(a)

print(reorganizeString("aabababababccccccc"))