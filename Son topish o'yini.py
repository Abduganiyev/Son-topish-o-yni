import random

def sontop(x=10):
    tasodifiy_son = random.randint(1,x)
    print(f"1 dan {x} gacha son o'yladim. Topa olasizmi?")
    O_big=0
    while True:
        O_big+=1
        taxmin=int(input(">>>"))
        if taxmin<tasodifiy_son:
            print("Xato. Men o'ylagan son bundan kattaroq. Yana xarakt qiling:")
        elif taxmin>tasodifiy_son:
            print("Xato. Men o'ylagan son bundan kichikroq. Yana xarakt qiling:")
        else:
            break
    print(f"Tabriklaymiz, O({O_big}) ta taxmin bilan topdingiz!")
    return O_big

def sontop_pc(x=10):
    input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing!.Men topaman!")
    quyi=1
    yuqori = x
    log_son,O_big=0,0
    while True:
        O_big+=1
        if quyi!=yuqori:
            log_son=(quyi+yuqori)//2
        else:
            log_son=quyi
        javob=input(f"Siz {log_son} sonini o'yladingiz: to'g'ri(=),\nmen o'ylagan son bundan kattaroq(+),\nyo'ki kichikroq(-)")
        if javob=="-":
            yuqori=log_son-1
        elif javob=="+":
            quyi=log_son+1
            continue
        else:
            break
    print(f"Men O({O_big}) ta taxmin bilan topdim!")
    return O_big


while True:
    O_big=sontop()
    O_big_pc=sontop_pc()
    if O_big>O_big_pc:
        print("Men yutdim!")
    elif O_big<O_big_pc:
        print("Siz yutingiz!")
    else:
        print("Durrang!")
    h_y=input("Yana o'ynaymizmi? ha(1),yo'q(0)")
    if h_y=='0':
        break