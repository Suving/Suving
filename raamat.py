import re

fail = open('ram.py', encoding='UTF-8')

for rida in fail:
    temp1 = re.findall(r'\d+', rida)
    res2 = list(map(int, temp1))
    numb = (res2[0])
    x = (numb * 2 / 120)
    
    print('järje korra järgi! lugemis aeg on ' + str(x) + ' päeva')
    
    
fail.close()