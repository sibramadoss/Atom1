def jailbreak(phrase):
    new_phrase = ""
    for index in phrase:
        if index in "AEIOUaeiou":
            if index.isupper() == True:
                new_phrase = new_phrase + "C"
            else:
                new_phrase = new_phrase + "c"
        else:
            new_phrase = new_phrase + index
    return new_phrase

print(jailbreak(input("Enter a password: ")))

social = ["twitter", "facebook", "instagram", "reddit"]

for index in social:
    if "a" in index:
        print index + " stops"
    else:
        print index + " continues"

nba = ["Lebron James(AS/USA) ", "Kevin Durant(AS/USA)", "Carmelo Anthony(USA)", "Jordan Clarkson(USA)", "Giannis Antetokounmpo(AS/GRE)", "Chris Paul(AS/USA)", "Draymond Green(USA)", "Kyle Korver(USA)", "Marco Belinelli(ARG)"]

for index in nba:
    if "AS/USA" in index:
        print index + " has qualified for the US Olympic basketball team."
    elif "AS" in index:
        print index + " has qualified for an Olympic basketball team."
    else:
        print index + " has not qualified for an Olympic basketball team."


Balondor = ["Robert Lewandowski", "Cristiano Ronaldo", "Lionel Messi", "Kylian Mbappe", "Ciro Immobile", "Paulo Dybala", "Neymar Jr.", "Virgil Van Dijk", "Mohamed Salah", "Karim Benzema"]
for index in range(len(Balondor)):
        if index <= 2:
            print Balondor[index] + " (Finalist)"
        else:
            print Balondor[index]

print("Conclude")

UCL = ["PSG/1st", "Madrid/2nd", "Brugge/3rd", "Galatasaray/4th", "Bayern/1st", "Tottenham/2nd", "Olympiacos/3rd", "Crvena/4th", "MCI/1st", "Atalanta/2nd", "Shakhtar/3rd", "Zagreb/4th", "Juventus/1st", "Atletico/2nd", "Leverkusen/3rd", "Lokomotiv/4th", "Liverpool/1st", "Napoli/2nd", "Red Bull/3rd","Genk/4th", "FCB/1st", "BVB/2nd", "Inter/3rd", "Slavia/4th", "Leipzig/1st", "Lyon/2nd", "Benfica/3rd", "Zenit/4th", "Valencia/1st", "Chelsea/2nd", "Ajax/3rd", "Lille/4th"]
for index in UCL:
    if "1st" in index:
        print index + " qualifies for round of 16 (will play 2nd place finisher)"
    elif "2nd" in index:
        print index + " qualifies for round of 16 (will play 1st place finisher)"
    else:
        print index + " does not qualify for round of 16"

i=1
while i <= 5:
    if i == 5:
        print(3**i)
    i += 1

print("CONCLUDE")

def power(base, twit):
    answer = 1
    for index in range(twit):
        answer = answer * base
    print answer

power(4,3)

def test():
    i=1
    while i <= 10:
        print i**i
        i += 1

def the_wire(number):
    flipped = ""
    for index in number:
        if index == "1":
            flipped = flipped + "9"
        if index == "2":
            flipped = flipped + "8"
        if index == "3":
            flipped = flipped + "7"
        if index == "4":
            flipped = flipped + "6"
        if index == "5":
            flipped = flipped + "0"
        if index == "6":
            flipped = flipped + "4"
        if index == "7":
            flipped = flipped + "3"
        if index == "8":
            flipped = flipped + "2"
        if index == "9":
            flipped = flipped + "1"
        if index == "0":
            flipped = flipped + "5"
            print(flipped)

the_wire(input("Enter a number: "))


def stopped(number):
    if "9" in number:
        return "Your call has been reported to the department of homeland security."
    else:
        return number

print(stopped(input("Enter a number: ")))


baseball = "Miguel Cabrera, Mike Trout, Christian Yelich"
bsb = ""
for index in baseball:
    if index in "AEIOUaeiou":
        bsb = bsb + "o"
    else:
        bsb = bsb + index

print(bsb)


lan = ["Java is useful", "Java is the primary language", "Python is superior"]

for index in lan:
    if "Java" in index:
        print(index.replace("Java", "Python"))
    else:
        print index


rap = ["Tjay(0)", "Birdman(0)", "Pump(0)", "Drake(1)", "Rae Sreemurd(1)", "J Cole(1)", "Kendrick Lamar(1)", "Lil Uzi(1)", "Roddy Rich(1)"]

for rapper in rap:
    if "0" in rapper:
        print rapper + " is traaaash"
    if "1" in rapper:
        print rapper + " is fireeeee"


qf = ["FCB(w)", "BAR", "RBL(w)", "ATM", "OL(w)", "MCI", "PSG(w)", "ATA"]

for team in qf:
    if "(w)" in team:
        print team + " qualifies for semi-final."
    else:
        print team + " has been eliminated."


arr = [3,4,4,4,5,5,6]
arr.sort(reverse = True)
print (arr)

soc = ["Ronaldo", "Messi", "Mbappe", "Neymar", "Lewandowski", "De Bruyne", "Gnabry", "Hazard", "Son"]
a, b = soc.index("Lewandowski"), soc.index("Mbappe")
soc[a], soc[b] = soc[b], soc[a]
print(soc)
print(soc.index("Lewandowski"))
print(range(len(soc)))

nfl = ["Mahomes", "Donald", "Jackson", "Wilson", "Thomas", "McCaffrey", "Kittle", "Gilmore", "Hopkins", "Henry"]
nfl.insert(0, nfl.pop(3))
nfl.insert(2, nfl.pop(3))
nfl.insert(8, nfl.pop(4))
print(nfl)
