# Uses National Data on the relative frequency of given names in the population of U.S. births,
# stored in a directory "names", in files named "yobxxxx.txt with xxxx being the year of birth.
#
# Prompts the user for a first name, and finds out the first year
# when this name was most popular in terms of frequency of names being given,
# as a female name and as a male name.
# 
# Written by *** and Eric Martin for COMP9021


import os
from collections import defaultdict


first_name = input('Enter a first name: ')
directory = 'names'
min_male_frequency = 0
male_first_year = None
min_female_frequency = 0
female_first_year = None

# Written by Jiaquan Xu
male_all_count_list = []
female_all_count_list = []

for filename in os.listdir(directory):
	male_population = 0
	female_population = 0
	if not filename.endswith('.txt'):
		continue
	with open(directory + '/' + filename) as data_file:
		for line in data_file:
			name, gender, count = line.split(',')
			if gender == 'M':
				male_population += int(count)
			else:  
				female_population += int(count)

	with open(directory + '/' + filename) as data_file1:
		year = str(filename)[3:7]
		for line in data_file1:
			name, gender, count = line.split(',')
			if name == first_name and gender == 'M':
				male_frequency = int(count) / male_population * 100
				male_all_count_list.append((male_frequency, year))
			if name == first_name and gender == 'F':
				female_frequency = int(count) / female_population * 100
				female_all_count_list.append((female_frequency, year))
if male_all_count_list != []:
	min_male_frequency = max(male_all_count_list)[0]
	male_first_year = max(male_all_count_list)[1]
if female_all_count_list != []:
	min_female_frequency = (max(female_all_count_list))[0]
	female_first_year = (max(female_all_count_list))[1]


# Replace this comment with your code

if not female_first_year:
    print(f'In all years, {first_name} was never given as a female name.')
else:
    print(f'In terms of frequency, {first_name} was the most popular '
          f'as a female name first in the year {female_first_year}.\n'
          f'  It then accounted for {min_female_frequency:.2f}% of all female names.'
         )
if not male_first_year:
    print(f'In all years, {first_name} was never given as a male name.')
else:
    print(f'In terms of frequency, {first_name} was the most popular '
          f'as a male name first in the year {male_first_year}.\n'
          f'  It then accounted for {min_male_frequency:.2f}% of all male names.'
         )

