import re

while True:

    invoer = input("Voer je telefoonnummer in: ")
    patroon = r"A-Z^06-?\d{8}$"
    matches = re.findall(patroon, invoer)

    if(len(matches) > 4):
       break

# Hier kom je pas uit als het telefoonnumer in het juiste formaat ingevoerd is.
print("Bedankt nummer in juiste formaat:", matches[0])
