import re

while True:

    invoer = input("Voer je kenmerken in: ")

    patroon = r"[A-Z]{2}\S{1}[0-9]{3}\S{1}[A-Z]{3}"
    matches = re.findall(patroon, invoer)

    if(len(matches) > 0):
       break

# Hier kom je pas uit als het telefoonnumer in het juiste formaat ingevoerd is.
print("Bedankt nummer in juiste formaat:", matches[0])

