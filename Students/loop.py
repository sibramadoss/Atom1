
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
