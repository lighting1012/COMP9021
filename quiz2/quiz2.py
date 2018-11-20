# Written by Jiaquan and Eric Martin for COMP9021


'''
Prompts the user for two strictly positive integers, numerator and denominator.

Determines whether the decimal expansion of numerator / denominator is finite or infinite.

Then computes integral_part, sigma and tau such that numerator / denominator is of the form
integral_part . sigma tau tau tau ...
where integral_part in an integer, sigma and tau are (possibly empty) strings of digits,
and sigma and tau are as short as possible.
'''


import sys
from math import gcd


try:
    numerator, denominator = input('Enter two strictly positive integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    numerator, denominator = int(numerator), int(denominator)
    if numerator <= 0 or denominator <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()


has_finite_expansion = False
integral_part = 0
sigma = ''
tau = ''

# written by Jiaquan
integral_part = numerator // denominator
numerator_1 = numerator // (gcd(numerator, denominator))
denominator_1 = denominator // (gcd(numerator, denominator))
#print('numerator_1 =', numerator_1)
#print('denominator_1 =', denominator_1)

Y = denominator_1
while Y > 1:
    if Y % 5 == 0:
        Y = Y // 5
    elif Y % 2 == 0:
        Y = Y // 2
    else:
        break
if Y == 1:
	has_finite_expansion = True

modlist = []
afterstring = ''
afterX = numerator_1
i = 0
while afterX // denominator_1 != 0:
	afterX = afterX % denominator_1
while afterX not in modlist:
	modlist.append(afterX)
	afterstring += str((afterX * 10) // denominator_1)
	afterX = (afterX * 10) % denominator_1
	i += 1
#print('modlist =', modlist)
#print('i =', i)
#print('afterX =', afterX)
#print('afterstring =', afterstring)
if afterX != 0:
	tau = afterstring
	for j in range(1, i):
		if modlist[j] == afterX:
			sigma = afterstring[:j]
			tau = afterstring[j:]

else:
	if numerator_1 % denominator_1 != 0:
		sigma = afterstring[:-1]

#written by Jiaquan
if has_finite_expansion:
    print(f'\n{numerator} / {denominator} has a finite expansion')
else:
    print(f'\n{numerator} / {denominator} has no finite expansion')
if not tau:
    if not sigma:
        print(f'{numerator} / {denominator} = {integral_part}')
    else:
        print(f'{numerator} / {denominator} = {integral_part}.{sigma}')
else:
    print(f'{numerator} / {denominator} = {integral_part}.{sigma}({tau})*')

