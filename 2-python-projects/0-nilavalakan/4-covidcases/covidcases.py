from covid import Covid
virus = Covid()
x = input('Enter the country Name :')
cases=virus.get_status_by_country_name(x)
for x in cases:
    print(x,':',cases[x])