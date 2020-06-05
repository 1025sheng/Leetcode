s = input('input:')
s = s.strip()

list_num = [str(i) for i in range(0,10)]
out = []

for i in range(0,len(s)):
    if s[i] == '-':
        if i == 0:
            out.append(s[0])
        else:
            continue
    else:
        if s[i] in list_num:
            out.append(s[i])
        else:
            break

if out == []:
    print("output:0")
else:
    a = ''.join(out)
    a = int(a)
    if -2**31 <= a <= 2**31:
        print("output:%d"%a)
    else:
        if a < 0:
            a = -2**31
            print("output:%d"%a)
        else:
            a = 2**31-1
            print("output:%d"%a)