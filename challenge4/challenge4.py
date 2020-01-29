
iteration = int(input("enter degree of fibancci:\n"))

def recur_fibo(n):
  if n <= 1:
    return n
  else:
    return recur_fibo(n - 1) + recur_fibo(n - 2)

overHundred = ['Hundred', 'Thousand', 'Million', 'Billion', 'Trillion', 'Quadrillion']

def splitNumber(n):
  print('-' * 40)
  numList = list(map(int, str(n)))
  print(numList)
  if len(str(n))%3 == 0:
    divByThree(numList, n)
  else:
    finalNum = []
    toPop = len(str(n))%3
    for j in range(0, toPop):
     finalNum.append(numList.pop(0))
    print('final')
    print(finalNum)
    print(numList)



def divByThree(numList, n):
  for j in range(0, len(str(n)), 3):
    numlistFull = ()
    numEnd = numList.pop()
    numMid = numList.pop()
    numStart = numList.pop()
    numlistFull = (numStart, numMid, numEnd)
    print('numListFull')
    print(numlistFull)


for i in range(0, iteration):
  splitNumber(recur_fibo(i))




def numToString(n):
  underHundred = {2: 'Twenty', 3: 'Thirty', 4: 'Fourty', 5: 'Fifty', 6: 'Sixty', 7: 'Seventy', 8: 'Eighty', 9: 'Ninety'}
  overHundred = ['Hundred', 'Thousand', 'Million', 'Billion', 'Trillion', 'Quadrillion']

  numList = list(map(int, str(n)))

  if numList[1] < 2:
    print(str(n) + ' - ' + underTwenty(n))
  else:
    bigger = list(map(int, str(n)))
    print(len(bigger))
    if len(bigger)%3 == 0:
      multipleOfThree(bigger)


def underTwenty(n):
  possibleValues = {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight',
                 9: 'Nine', 10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen',
                 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
  return possibleValues[n]



def multipleOfThree(n):
    tens = int(n[-1]) + int(n[-2]*10)
    print('tens')
    print(tens)








