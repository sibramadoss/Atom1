
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
