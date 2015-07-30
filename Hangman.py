
name = raw_input("What is your name? ")

print "Hello," + name+"! Time to play hangman!"

prev_guess = []

correct_guess = []

fail = 10 

win = 

while 
	while fail > len(prev_guess):
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

		word = "bad"

		guesses = word



		if guess in guesses: 
			print correct_guess
			correct_guess.append(guess)
		else:
			print "Try Again."
			prev_guess.append(guess)
			
	print "You Failed!!!"