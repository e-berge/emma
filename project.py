#a
h=open("Exchrate.txt")
country = input("Enter name of country: ")

for line in h:
    line=line.split(",")
    if line[0] == country:
        currency=line[1]
        conversion=line[2]
        print("Currency:",currency)
        print("Exchange rate:", conversion)

#b
h=open("Exchrate.txt")
d={}

for line in h:
    line=line.strip()
    country=line.split(',')
    if country[0].lower() not in d:
        i=float(country[2])
        d[country[0].lower()]=[country[1], i]
for country in sorted(d.keys(), key=lambda country:d[country][1]):
    print(country)

#c
h=open("Exchrate.txt")
x=open("Exchrate.txt")
firCountry=input("Enter name of first country: ")
secCountry=input("Enter name second country: ")
money=input("Amount of money to convert: ")

for line in h:
    line=line.split(",")
    if line[0] == firCountry:
        firmoney = line[2]
        currencyone=line[1]
for line in x:
    line=line.split(",")
    if line[0]== secCountry:
        secmoney=line[2]
        currencytwo=line[1]
print(money, currencyone +"s", "from", firCountry, "equals", float(secmoney)/float(firmoney)*100, currencytwo +"s", "from", secCountry)

