from random import randint
import socket
import time as tm
import requests
from bs4 import BeautifulSoup
import keyboard
bukvizapad = 'abcdefghijklmnopqrstuvwxyz1234567890'
bukvizov = 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя1234567890'
zonizapad = ['.com', '.net', '.org', '.ru', '.online', '.xyz', '.tk', '.ml', '.ga', '.cf', '.gq','.app', '.dev', '.blog', '.shop','.info', '.biz', '.pro', '.name','.site', '.website', '.space', '.tech','.store', '.club', '.world', '.live']
zonizov = ['.рф', '.рус', '.дети', '.москва', '.онлайн', '.сайт', '.орг']
gadkieimena = ['is for sale', 'buy now', 'access denied', 'domain', 'reserved','403', 'for sale', 'domain', 'домены', 'доменов', 'domains', 'хостинга', 'доменных имен', 'доменные имена',
'домен', 'продается', 'припаркован']
krutolist = []
vupolneno = 0
starttm = tm.time()
mojno = 1
oboroti = 0
custom_zones = []
customgadosti = []
while oboroti == 0:
    try:
        oboroti = int(input('Enter amount of domen generations:'))
    except:
        print('Please enter number')
    if oboroti == 0 or oboroti < 0:
        print('You enter invalid number, please enter different number')
        oboroti = 0
usedomensalefiltr = str(input('Use filtration for domen sale?(y/n)')).lower()
if usedomensalefiltr == 'n' :
    gadkieimena = []
    print('Filtration for domen sale are deactivated')
else:
    print('Filtration for domen sale are activated')
vreme_mejdy_tickami = 0
vreme_ojidania = 0
vreme_ojidania_bez_ineta = 0
while vreme_mejdy_tickami == 0:
    try:
        vreme_mejdy_tickami = float(input('Enter time between domen generations(dont enter a number less than 0.1):'))
    except:
        print('You enter invalid number, please enter different number')
    if vreme_mejdy_tickami < 0 or vreme_mejdy_tickami == 0:
        print('You enter invalid number, please enter different number')
        vreme_mejdy_tickami = 0
while vreme_ojidania == 0:
    try:
        vreme_ojidania = float(input('Enter time you wait for the domain response:'))
    except:
        print('You enter invalid number, please enter different number')
    if vreme_ojidania < 0 or vreme_ojidania == 0:
        print('You enter invalid number, please enter different number')
        vreme_ojidania = 0
while vreme_ojidania_bez_ineta == 0:
    try:
        vreme_ojidania_bez_ineta = float(input('Enter time you wait in generation without internet:'))
    except:
        print('You enter invalid number, please enter different number')
    if vreme_ojidania_bez_ineta < 0 or vreme_ojidania_bez_ineta == 0:
        print('You enter invalid number, please enter different number')
        vreme_ojidania_bez_ineta = 0
custom_zones = input('Enter your domain zones separated by space (example: .test .my .zone) or press Enter:')
if custom_zones:
    zonizapad += custom_zones.split()
    print('Added domain zones:', custom_zones)
customgadosti = input('Enter key words that you not want to see in the title of the domains separated by space (example: keyword1 keyword2 keyword3) or press Enter:')
if customgadosti:
    customgadosti = customgadosti.lower().split()
    print('Added banned key words:', customgadosti)
while vupolneno < oboroti:
    if keyboard.is_pressed('q'):
        print(oboroti, 'rpm set')
        print(vupolneno, 'rpm complete')
        print((oboroti - vupolneno) * ((vreme_mejdy_tickami + vreme_ojidania)/2), 'time before end(seconds)')
        print('press space to stop the programm')
    if keyboard.is_pressed('space'):
        vupolneno = oboroti
        break
    try:
        mojno = '1'
        socket.gethostbyname('google.com')
    except:
        mojno = '0'
    if mojno == '0':
        print('no internet connecting')
        tm.sleep(vreme_ojidania_bez_ineta)
        continue
    stroka = ''
    zona0 = zonizapad[randint(0, len(zonizapad) - 1)]
    zona1 = zonizov[randint(0, len(zonizov) - 1)]
    vibori = randint(0, 1)
    if vibori == 1:
        zona = zona0
        for i in range(randint(1, 20)):
            stroka += bukvizapad[randint(0, len(bukvizapad) -1 )]
    elif vibori == 0 :
        zona = zona1
        for i in range(randint(1, 20)):
            stroka += bukvizov[randint(0, len(bukvizov) -1 )]
    domen = stroka + zona
    krutodomen = 'http://' + domen + '/'
    try:
        status = 'OK'
        socket.gethostbyname(domen)
    except:
        status = 'FAIL'
    if status == 'OK':
        try:
            gadosti = requests.get(krutodomen, timeout=vreme_ojidania)
            gadosti.encoding = 'utf-8'
            for i in gadkieimena:
                if i in BeautifulSoup(gadosti.text, 'html.parser').find('title').text.lower().strip():
                    status = 'FAIL'
            if customgadosti:
                for i in customgadosti:
                    if i in BeautifulSoup(gadosti.text, 'html.parser').find('title').text.lower().strip():
                        status = 'FAIL'
        except:
            status = 'FAIL'
    if status == 'FAIL':
        with open('nekruto.txt', 'a', encoding='utf-8') as file:
            file.write(domen + "\n")
    if status == 'OK':
        with open('kruto.txt', 'a', encoding='utf-8') as file:
            if not domen in krutolist:
                file.write(domen + "\n")
                krutolist.append(domen)
    vupolneno += 1                
    procent = round(vupolneno / oboroti * 100, 3)
    print(procent, '% сomplete')
    tm.sleep(vreme_mejdy_tickami)
endtime = tm.time()
with open('nekruto.txt', 'r', encoding='utf-8') as file:
    strokibad = sum(1 for line in file)
with open('kruto.txt', 'r', encoding='utf-8') as file:
    strokigood = sum(1 for line in file)
    vsegostroki = strokigood + strokibad
    kof1 = str(100 * (strokigood/vsegostroki)) + '% working'
    kof2 = str(100 * (strokibad/vsegostroki)) + '% not working'
with open('bukvi.txt', 'a', encoding='utf-8') as file:
    file.write(kof1 + "\n")
    file.write(kof2 + "\n")
    file.write(str(strokigood) + ' working(amount)' + "\n")
    file.write(str(strokibad) + ' not working(amount)' + "\n")
    file.write('estimated minimal time: ' + str(round(oboroti * (vreme_mejdy_tickami + vreme_ojidania) / 2, 1)) + ' sec\n')
    file.write(str(round(endtime - starttm, 3)) + '  real time' + "\n")
print('work complete!')