import inflect

iteration = int(input("enter degree of fibancci:\n"))
i = 0

def recur_fibo(n):
  if n <= 1:
    return n
  else:
    return recur_fibo(n - 1) + recur_fibo(n - 2)

# def numToString(n):
#   underTwenty = {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight',
#                  9: 'Nine', 10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen',
#                  16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
#   underHundred = {2: 'Twenty', 3: 'Thirty', 4: 'Fourty', 5: 'Fifty', 6: 'Sixty', 7: 'Seventy', 8: 'Eighty', 9: 'Ninety'}
#   overHundred = ['Hundred', 'Thousand', 'Million', 'Billion', ]
#
#   if n < 20:
#     print(str(n) + '- ' + str(underTwenty[n]))
#   else:
#     bigger = list(map(int, str(n)))
#     print(bigger)

for i in range(0, iteration):
  number = inflect.engine().number_to_words(recur_fibo(i))
  print(str(recur_fibo(i)) + ' - ' + str(number))






