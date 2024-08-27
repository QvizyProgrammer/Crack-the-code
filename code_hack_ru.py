import random
import os
import time

viv = ''
schet = 0
schetchik = 0
pop = 0
print('выберите сложность (1, 2, 3...)')
slozh = int(input('>>> '))
os.system('clear')

for i in range(slozh):
    chislo = random.randint(0, 9)
    viv = viv + str(chislo)
start = time.time()
while True:
    code = input('код: ')
    code1 = list(code)
    code2 = list(viv)
    if code == 'код 1':
        os.system('clear')
        stop = time.time()
        result = stop - start
        print(f'код успешно взломан!\nинформация:\nвремя взлома: {result}\nпопытки: {pop}\nкод: {viv}')
        break
    for i in range(slozh):
        if code1[schet] == code2[schet]:
            schetchik += 1
        schet += 1
    print(f'совпавших: {schetchik}')
    if schetchik == slozh:
        os.system('clear')
        stop = time.time()
        result = stop - start
        print(f'код успешно взломан!\nинформация:\nвремя взлома: {result}\nпопытки: {pop}\nкод: {viv}')
        break
    schetchik = 0
    schet = 0
    pop += 1