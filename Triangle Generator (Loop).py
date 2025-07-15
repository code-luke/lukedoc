def choice():
    print('''What type of triangle do you want to create? (choose either 1-3)
1. Isosceles Triangle
2. Right Triangle
3. Done''')

def f_or_w():
    a_m=print('''Which method do you want to use?
1. For Loop method
2. While Loop method''')

def r_or_l():
    print('''Which side do you want to align to?
1. Right Alligned
2. Left Alligned''')

def ITF():
    a_s=int(input('How long is the base?\n'))
    print('Here is For Loop')
    side= range(1,a_s+1,2)
    space= a_s//2
    for i in side:
        print(' '*space+'+'*i)
        space=space-1

def ITW():
    a_s=int(input('How long is the base?\n'))
    print('Here is While Loop')
    start=1
    space= a_s//2 -1
    while start<=a_s:
        print(' '*space+'+'*start)
        start=start+2
        space=space-1

def RTF_r():
    a_b= int(input('How long is the base?\n'))
    print('Here is For Loop')
    for i in range(1,a_b+1,2):
        print('+'*i)

def RTF_l():
    a_b= int(input('How long is the base?\n'))
    print('Here is For Loop')
    space=a_b-1
    for i in range(1,a_b,2):
        print(' '*space+'+'*i)
        space=space-2

def RTW_r():
    a_b=int(input('How long is the base?\n'))
    print('Here is While Loop')
    start=1
    while a_b>=start:
        print('+'*start)
        start=start+2

def RTW_l():
    a_b= int(input('How long is the base?\n'))
    print('Here is While Loop')
    start=1
    space=a_b-1
    while a_b>=start:
        print(' '*space+'+'*start)
        start=start+2
        space=space-2

while True:
    choice()
    ask=int(input(''))
    if ask==1:
        f_or_w()
        ask2=int(input(''))
        if ask2==1:
            ITF()
        elif ask2==2:
            ITW()
        else:
            print('GAADA!!!')
    elif ask==2:
        f_or_w()
        ask3=int(input(''))
        if ask3==1:
            r_or_l()
            ask4=int(input(''))
            if ask4==1:
                RTF_r()
            elif ask4==2:
                RTF_l()
            else:
                print('GAADA!!!')
        if ask3==2:
            r_or_l()
            ask4=int(input(''))
            if ask4==1:
                RTW_r()
            elif ask4==2:
                RTW_l()
            else:
                print('GAADA!!!')
    elif ask==3:
        break