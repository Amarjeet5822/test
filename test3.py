s = "121"
ans = ""
for i in range(len(s)-1,-1,-1):
    ans+=[i]
if s == ans:
    print("yes")
else:
    print("no")