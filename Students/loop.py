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


n8s = ["Memphis", "Portland(q)", "San Antonio", "Phoenix", "Orlando(q)", "Sacramento", "Washington D.C.", "Charlotte", "Chicago"]
for team in n8s:
    if "(q)" in team:
        print team + " has qualified for the nba playoffs."
    else:
        print team + " has not qualified for the nba playoffs."


LS5 = ["Lebron James(ASG)", "Kentavious Caldwell-Pope", "Anthony Davis(ASG)", "JaVale McGee", "Danny Green"]

for player in LS5:
    if "ASG" in player:
        print player + " has qualified for the 2020 All-Star Game."
    else:
        print player + " has not qualified for the 2020 All-Star Game."


clf = ["Bayern Munich(+gd)", "Olympique Lyon(-gd)", "Paris-Saint Germain(+gd)", "RedBull Leipzig(-gd)"]

for team in clf:
    if "+gd" in team:
        print team + " has qualified for the the Champions League Final."
    else:
        print team + " has not qualified for the the Champions League Final."

g1n = ["LAC(1)", "DAL(0)", "POR(1)", "ORL(1)", "MIA(1)", "TOR(1)", "BOS(1)", "HOU(1)", "DEN(1)", "LAL(0)", "MIL(0)", "IND(0)", "PHI(0)", "OKC(0)", "UTA(0)", "BKN(0)"]

for team in g1n:
    if "(1)" in team:
        print team + " is up 1-0 in the playoff series."
    else:
        print team + " is down 0-1 i the playoff series."


def UEL(sevilla, inter_milan):
    if sevilla > inter_milan:
        print "Sevilla wins the Europa League."
    elif inter_milan > sevilla:
        print "Inter Milan wins the Europa League."
    else:
        print "The match will be settled through extra time and, if needed, penalties."

UEL(3,3)


g2n = ["LAC(0)", "DAL(1)", "POR(0)", "ORL(0)", "MIA(1)", "TOR(1)", "BOS(1)", "HOU(1)", "DEN(0)", "LAL(1)", "MIL(1)", "IND(0)", "PHI(0)", "OKC(0)", "UTA(1)", "BKN(0)"]
for team in g2n:
    if "0" in team:
        print team + " has lost the game second game of the series"
    if "1" in team:
        print team + " has won the second game of the series"


def UCF(FCB, PSG):
    if FCB > PSG:
        print "Bayern Munich has won the 2020 Champions League Final."
    elif PSG > FCB:
        print "Paris Saint-Germain has won the 2020 Champions League Final."
    else:
        print "The match was not completed for unspecified reasons."

UCF(1,1)


g3n = ["LAC(1)", "DAL(0)", "POR(0)", "ORL(0)", "MIA(1)", "TOR(1)", "BOS(1)", "HOU(0)", "DEN(0)", "LAL(1)", "MIL(1)", "IND(0)", "PHI(0)", "OKC(1)", "UTA(1)", "BKN(0)"]
for team in g3n:
    if "1" in team:
        print team + " has won the third game of the series."
    else:
        print team + " has lost the third game of the series."
