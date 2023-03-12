# 3 + 5
import math
# Calculate BMI (Body mass Index) not the formula is as show below.
# BMI =  WEIGHT (KG)/ height  square (m2)
height = input("Enter your hight: ")
weight = input("Enter your weight: ")
print ("Your height is: " + height + " " "and your weight is: " " " + weight )
print ("====== We will be calculating your body mass Index===== ")
bmi = int(weight) / float(height) ** 2  # The double *** 2 is a square root 
bmi_as_int =  int(bmi)
print (bmi_as_int)