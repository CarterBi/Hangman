x = int(raw_input("What number do you want factored?"))

factors = []

end = int(x**0.5 + 1)


for i in range(1, end + 1):
    if x % i == 0:
        factors.append(i)

rev_factors = factors[::-1]

for i in rev_factors:
	new_factor = x/i
	if new_factor not in factors:
		factors.append(new_factor)


for f in factors:
	print f

print "There are %d factor(s) for the number %d." % (len(factors), x)