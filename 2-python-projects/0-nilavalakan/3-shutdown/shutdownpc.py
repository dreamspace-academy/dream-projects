import os



print('1.shutdown')
print('2.restart')
print('3.exit')

command=input('Enter your command : ')

if '1' in command:
    os.system('shutdown /s')
if '2' in command:
    os.system('shutdown /r')
if '3' in command:
    exit()