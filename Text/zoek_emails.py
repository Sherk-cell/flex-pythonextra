import re

emails = []

with open("tekstmetemails.txt", "r") as bestand:

    regel = bestand.readline()

    while regel:

        # Vul de juiste regular expression voor een email in op de puntjes
        patroon = r"[\w-]{1,20}@\w{2,20}.\w{2,3}"

        # Gebruik de juiste code op de plaats van de puntjes
        gevonden = re.findall(patroon, regel)

        # Alle gevonden emails aan de email list toevoegen
        emails.extend(gevonden)

        # Volgende regel lezen
        regel = bestand.readline()

print(emails)
