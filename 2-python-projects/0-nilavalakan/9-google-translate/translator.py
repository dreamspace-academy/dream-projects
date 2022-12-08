from googletrans import Translator


sen = str(input('Enter the sentence : '))
n = Translator()
lang = str(input('Your language : '))
convert = str(input('Which language : '))
output = n.translate(sen, src=lang, dest=convert)
print(output.text)