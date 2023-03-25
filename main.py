distance_mile = int(input('What is the distance boss? (in miles) '))

speed = int(input(
  'What is the speed Donna? '))  # Oh! it's {any_input_on_workbook} honey!

# first do the conversion
distance_km = 1.6 * distance_mile

timeItWillTake = (distance_km / speed) * 60  #in minutes

print("{:.2f}".format(
  timeItWillTake))  #repeat the 1.1 Varying dept if you're stuck!
