
name = raw_input("What is your name? ")

print "Hello," + name+"! Time to play hangman!"

prev_guess = []
word = "rain"

guesses = word

num = len(word)
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

	if guess in guesses: 
		# print correct_guess
		# correct_guess.append(guess)
		for i in range(num):
			if word[i] == guess:
				correct_guess[i] = guess
	else:
		print "Try Again."
		prev_guess.append(guess)


if fail < len(prev_guess):
	print "You Failed!!!"
else: 
	print "Congratulations!"