import time
times = 3

for x in range (times):
  def calculate(a, b, formula):
    if formula == '+':
      return a + b
    elif formula == '-':
      return a - b
    elif formula == '*':
      return a * b
    elif formula == '/':
      return a / b
    else:
      print('Just Leave!')
      return 'Closing program...'

  print('Choose a number')
  a = float(input())
  print('Choose a second number')
  b = float(input())
  print('Do you want to * / - or + ?')
  formula = input()
  answer = calculate(a, b, formula)
  print(answer)
sleep(3)