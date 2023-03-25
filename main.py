lcd_screens = int(input('What is the total number of LCD screens sir? '))
eInk_screens = int(input('What is the total number of E-ink screens sir? '))

#in grams
weight_lcd = 63 * lcd_screens
weight_eInk = 30 * eInk_screens

print(f"Total weight of LCD screens is {weight_lcd} grams.")
print(f"Total weight of E-ink screens is {weight_eInk} grams.")
