# name of student: Jurrian Schouten
# number of student: 99067235
# purpose of program: Het geeft aan hoeveel munten je terugkrijgt van een bepaalde waarde
# function of program: berekenen
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) # De input wordt omgezet naar centen
paid = int(float(input('Paid amount: ')) * 100) # De input wordt omgezet naar centen
change = paid - toPay # Python trekt het te betalen bedrag af van het betaalde bedrag

if change > 0: # als de uitkomst van change groter dan 0 is, gaat hij naar de volgende regel
  coinValue = 200 # 
  
  while change > 0 and coinValue > 0: # Als change en coinValue beiden groter dan 0 zijn, gaat hij naar de volgende regel
    nrCoins = change // coinValue # Hij berekent het en zet het om naar een heel getal

    if nrCoins > 0: # als nrCoins groter dan 0 is:
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) # Er wordt aangegeven hoeveel coins van welke waarde moeten worden teruggegeven
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) # je moet invullen hoeveelje teruggegeven hebt
      change -= nrCoinsReturned * coinValue # Python berekent hoeveel coins van welke value je terugkrijgt.

# comment on code below: De waarde
    if coinValue == 200:
      coinValue = 100
    elif coinValue == 100:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: # Hij controleert of het hoger is dan 0
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')