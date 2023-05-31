#BASIC
for a in range(151):
    print(a)


#MULTIPLES OF 5
for b in range(5, 1001):
    if b % 5 == 0:
        print(b)
    
    else:
        continue


#COUNTING, THE DOJO WAY
for c in range(1, 101):
    if c % 15 == 0:
        print("Coding Dojo")
    
    elif c % 5 == 0:
        print("Coding")
    
    else:
        print(c)


#WHOA. THAT SUCKER'S HUGE
sum = 0

for d in range(500000):
    if d % 2 != 0:
        sum += d
    else:
        continue
print(sum)


#COUNTDOWN BY FOURS
for e in range(2018, 0, -4):
    print(e)


#FLEXIBLE COUNTER
lowNum = 5
highNum = 5000
mult = 8

for f in range(lowNum, highNum):
    if f % mult == 0:
        print(f)
    