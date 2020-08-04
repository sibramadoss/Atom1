
def jailbreak(phrase):
    new_phrase = ""
    for index in phrase:
        if index in "AEIOUaeiou":
            if index.isupper():
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
