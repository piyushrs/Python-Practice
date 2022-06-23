s = "no worries bro"
r = ''
t = ''.join(s)
for i in range(len(t)):
    if not i%2:
        r += t[i].upper()
    else:
        r += t[i].lower()
print(r)