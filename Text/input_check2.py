import re

while True:

    invoer = input("Voer je postcode in: ")
    patroon = r"[0-9]{4}\s?[A-Z]{2}$"
    matches = re.findall(patroon, invoer)

    if(len(matches) > 0):
       break

# Hier kom je pas uit als het telefoonnumer in het juiste formaat ingevoerd is.
print("Bedankt nummer in juiste formaat:", matches[0])
