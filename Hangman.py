import random

name = raw_input("What is your name? ")

print "Hello," + name+"! Time to play hangman!"

prev_guess = []
word = []

word.append("apple")
word.append("pie")
word.append("minecraft")
word.append("hangman")
word.append("steam")
word.append("mail")
word.append("ninja")
word.append("combat")
word.append("rain")
word.append("lava")
word.append("park")
word.append("bow")
word.append("arrow")
word.append("page")
word.append("phone")
word.append("pizza")
word.append("charger")
word.append("pokemon")
word.append("water")
word.append("naruto")
word.append("house")
word.append("bottle")
word.append("math")
word.append("can")
word.append("edit")
word.append("sky")
word.append("ground")
word.append("car")
word.append("android")
word.append("launch")
word.append("app")


x = random.randint(0,len(word)-1)

correct = word[x]

num = len(correct)
correct_guess = ["_"] * num



fail = 10 

while fail > len(prev_guess) and "_" in correct_guess:
	while True:
		print "Here are your correct guesse(s)"
		print correct_guess
		print "Here are your wrong guesses."
		print prev_guess
		guess = raw_input("What letter do you guess?")
		if (len(guess) != 1):
			print "Invalid Answer."
		else:
			break



	# print display

	if guess in correct: 
		# print correct_guess
		# correct_guess.append(guess)
		for i in range(num):
			if correct[i] == guess:
				correct_guess[i] = guess
	else:
		print "Try Again."
		prev_guess.append(guess)


if fail <= len(prev_guess):
	print "You Failed!!!"
else: 
	print "Congratulations!"
print "The correct word was " + word[x] + "!"
