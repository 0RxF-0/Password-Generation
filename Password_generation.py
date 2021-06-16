import random

char = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

nb = random.randint(12,16)
gen = []
for n in range(nb):
    choix = random.choice(char)
    gen.append(choix)
STRG = "".join(gen)
print("Bienvenue sur le générateur de mot de passe")
print("Voici votre mot de passe : ", STRG)

# @0RxF-0
