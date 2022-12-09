import os


print('1.shutdown')
print('2.restarrt')
print('1.exit')



command=input('enter your command :')

if '1' in command:
    os.system('shutdown /s')
if '2' in command:
    os.system('shutdown /r')
if '3' in command:
    exit()


