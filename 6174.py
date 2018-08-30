tab = []
loop = 'loop'
# tab will hold all Kaprekar numbers found
# loop is just for better wording

def asc(n):
    # puts the number's digits in ascending...
    return int(''.join(sorted(str(n))))

def desc(n):
    # ...and descending order
    return int(''.join(sorted(str(n))[::-1]))

n = input("Specify a number: ")
try:
    n = int(n)
except:
    # assuming n = 2016 to prevent program from crashing
    print("\nInvalid number specified!!!\nAssuming n = 2016.")
    n = "2016"
print("\nTransforming", str(n) + ":")

while True:
    # iterates, assigns the new diff
    print(desc(n), "-", asc(n), "=", desc(n)-asc(n))
    n = desc(n) - asc(n)

    if n not in tab:
        # checks if already hit that number
        tab.append(n)
    else:
        if tab.index(n) == len(tab)-1:
        # if found as the last, it is a constant...
            tab = []
            tab.append(n)
            loop = 'constant'
        else:
        # ...otherwise it is a loop
            tab = tab[tab.index(n):]
            # strip the first, non-looping items
        break

print('Kaprekar', loop, 'reached:', tab)

tab = []
loop = 'loop'
# tab will hold all Kaprekar numbers found
# loop is just for better wording

def asc(n):
    # puts the number's digits in ascending...
    return int(''.join(sorted(str(n))))

def desc(n):
    # ...and descending order
    return int(''.join(sorted(str(n))[::-1]))

n = input("Specify a number: ")
try:
    n = int(n)
except:
    # assuming n = 2016 to prevent program from crashing
    print("\nInvalid number specified!!!\nAssuming n = 2016.")
    n = "2016"
print("\nTransforming", str(n) + ":")

while True:
    # iterates, assigns the new diff
    print(desc(n), "-", asc(n), "=", desc(n)-asc(n))
    n = desc(n) - asc(n)

    if n not in tab:
        # checks if already hit that number
        tab.append(n)
    else:
        if tab.index(n) == len(tab)-1:
        # if found as the last, it is a constant...
            tab = []
            tab.append(n)
            loop = 'constant'
        else:
        # ...otherwise it is a loop
            tab = tab[tab.index(n):]
            # strip the first, non-looping items
        break

print('Kaprekar', loop, 'reached:', tab)
