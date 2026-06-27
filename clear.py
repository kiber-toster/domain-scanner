import keyboard
print('press the key (if you press it again your files will be empety)')
knopka = keyboard.read_key()
print('you choose the key', knopka)
i = int(input('how many times you want to clear the files?'))
while i > 0:
    keyboard.wait(knopka)
    with open('nekruto.txt', 'w', encoding='utf-8') as file:
                file.write('')
    with open('kruto.txt', 'w', encoding='utf-8') as file:
                file.write('')
    with open('bukvi.txt', 'w', encoding='utf-8') as file:
        file.write('')
    print('files are empety now')
    i -= 1