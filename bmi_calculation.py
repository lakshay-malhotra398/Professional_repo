# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List, Any

# Read the File
p_file = open(r"C:\Users\acer\Desktop\hw.txt")
v_file = p_file.read()
v_file = v_file.split()

#Declare Variables
weight = []
height = []
bmi =[]
underweight=[]
normal=[]
overweight=[]
obese =[]
avg_1=0
avg_2=0
avg_3=0
avg_4=0

#Loop to calculate height and weight and create a individual lists of those
for i in range(0, len(v_file)):
    if i % 2 == 0:
        height.append(int(v_file[i])/100)
    else:
        weight.append(int(v_file[i])/2.2)

#Calculation of bmi
for i in range(len(height)):
    bmi.append(weight[i]/(height[i])**2)

llist = [{}, {}, {}, {}]
#1: underweight
#2: Overweight
#3: Normal
#4: Obesity

#Underweight = <18.5
#Normal weight = 18.5–24.9
#Overweight = 25–29.9
#Obesity = BMI of 30 or greater


#Categorize them into category
for i in range(1, len(bmi)+1):
    if bmi[i-1] < 18.5:
        avg_1=avg_1+bmi[i-1]
        underweight.append(i)
        underweight.append(round(bmi[i-1],4))
        llist[0][f"Person- {i}"] = round(bmi[i-1],4)
    elif bmi[i-1] < 24.9:
        avg_2 = avg_2 + bmi[i - 1]
        normal.append(i)
        normal.append(round(bmi[i - 1], 4))
        llist[1][f"Person- {i}"] = round(bmi[i-1],4)
    elif bmi[i-1] < 29.9:
        avg_3 = avg_3 + bmi[i - 1]
        overweight.append(i)
        overweight.append(round(bmi[i - 1], 4))
        llist[2][f"Person- {i}"] = round(bmi[i-1],4)
    else:
        avg_4 = avg_4 + bmi[i - 1]
        obese.append(i)
        obese.append(round(bmi[i - 1], 4))
        llist[3][f"Person- {i}"] = round(bmi[i-1],4)


#Calculate average BMI of the groups
avg_1 = round(avg_1/len(llist[0]),4)
avg_2 = round(avg_2/len(llist[1]),4)
avg_3 = round(avg_3/len(llist[2]),4)
avg_4 = round(avg_4/len(llist[3]),4)

for n in range(0,len(underweight),2):
    print(f"Person- {underweight[n]} : {underweight[n+1]}")
#print(f"underweight: {llist[0]}")
print(f"Group Size: {len(llist[0])}")
print(f"Average BMI for this group: {avg_1}")

for n in range(0,len(normal),2):
    print(f"Person- {normal[n]} : {normal[n+1]}")
#print(f"Normal: {llist[1]}")
print(f"Group Size: {len(llist[1])}")
print(f"Average BMI for this group: {avg_2}")

for n in range(0,len(overweight),2):
    print(f"Person- {overweight[n]} : {overweight[n+1]}")
#print(f"Overweight: {llist[2]}")
print(f"Group Size: {len(llist[2])}")
print(f"Average BMI for this group: {avg_3}")

for n in range(0,len(obese),2):
    print(f"Person- {obese[n]} : {obese[n+1]}")
#print(f"Obesity: {llist[3]}")
print(f"Group Size: {len(llist[3])}")
print(f"Average BMI for this group: {avg_4}")