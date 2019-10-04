# Name: Nathan Balos
# Period
# Dice Rolling Simulator
import random
ones = 0
twos = 0
threes = 0
fours = 0
fives = 0
sixes = 0
cChoices = ["1", "2", "3", "4", "5", "6"]
loopNumber = input("How many dice rolls will be performed?")
a=0
while a < int(loopNumber):
	rollnumber = random.choice(cChoices)
	print("Roll number : " + str(a + 1))
	if rollnumber == "1":
		ones = ones + 1
	elif rollnumber == "2":
		twos = twos + 1
	elif rollnumber == "3":
		threes = threes +1
	elif rollnumber == "4":
		fours = fours + 1
	elif rollnumber == "5":
		fives = fives + 1
	elif rollnumber == "6":
		sixes = sixes + 1
	print("1s - " + str(ones))
	print("2s - " + str(twos))
	print("3s - " + str(threes))
	print("4s - " + str(fours))
	print("5s - " + str(fives))
	print("6s - " + str(sixes))
	a=a+1
print("Total Rolls: " + str(a))
print("1s - " + str(ones))
print("2s - " + str(twos))
print("3s - " + str(threes))
print("4s - " + str(fours))
print("5s - " + str(fives))
print("6s - " + str(sixes))
ones = (int(ones))/(int(loopNumber))
print("1s - " + str(ones))
ones = (int(ones))/(int(loopNumber))
print("1s - " + str(ones))
ones = (int(ones))/(int(loopNumber))
print("1s - " + str(ones))
ones = (int(ones))/(int(loopNumber))
print("1s - " + str(ones))
ones = (int(ones))/(int(loopNumber))
print("1s - " + str(ones))
ones = (int(ones))/(int(loopNumber))
print("1s - " + str(ones))