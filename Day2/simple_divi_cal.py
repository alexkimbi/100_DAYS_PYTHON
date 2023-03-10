# 3 + 5
import math
# 7 - 5
# 4 * 5
# 6 / 5
#print (3 * 3 + 6 / 5 - 3)

# Calculate BMI (Body mass Index) not the formula is as show below.
# BMI =  WEIGHT (KG)/ height  square (m2)
height = input("Enter your hight: ")
weight = input("Enter your weight: ")
print ("Your height is: " + height + " " "and your weight is: " " " + weight )
print ("====== We will be calculating your body mass Index===== ")
bmi = int(weight) / float(height) ** 2
bmi_as_int =  int(bmi)
print (bmi_as_int)


