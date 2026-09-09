"""
ChatGPT's response to the following prompt:
(1) Show lifespan of pets, such as dog, cat, and rabbit. Also, show lifespan of human in America. show references articles, research papers, or government resources. I need to access to validate them.
(2) OK. I downloaded some of them. How to use case in Python?
(3) How to use match case in Python
https://chatgpt.com/share/6aa1b605-2380-83e8-bd27-bcbbdd5a8120

I checked the references because sometimes AI shows hallucination, but I found the references are valid. Here are the references for calculating lifespan of pets and humans:

References
[1] O'Neill et al., “Life expectancy tables for dogs and cats derived from clinical data” (2023)
url = https://pmc.ncbi.nlm.nih.gov/articles/PMC9989186/
[2] Jiaquan Xu et al., "Mortality in the United States 2024", National Center for Health Statistics, Centers for Disease Control and Prevention (CDC), 2024
url = https://www.cdc.gov/nchs/products/databriefs/db548.htm
[3] Angela M Lennox, "Care of the Geriatric Rabbit", Veterinary Clinics of North America
url = https://pmc.ncbi.nlm.nih.gov/articles/PMC7129804/?utm_source=chatgpt.com
"""


class Pet:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species
    def calc_lifespan(self):
        match self.species:
            case "Dog":
                # Dog lifespan in America is 12.69 years according to O'Neill et al. [1]
                return 12.69
            case "Cat":
                # Cat lifespan in America is 11.18 years according to O'Neill et al. [1]
                return 11.18
            case "Rabbit":
                # Rabbit lifespan in America is about 9 years according to Lennox [3]
                return 9.0
    def calc_lifespantoHuman(self):
        # Human lifespan in America is 79.0 years according to CDC [2]
        return 79.0 * self.age / self.calc_lifespan() 


dog = Pet("Buddy", 5, "Dog")
cat = Pet("Whiskers", 3, "Cat")
rabbit = Pet("Thumper", 2, "Rabbit")

print(f"{dog.name} is a {dog.species} and {dog.name}'s age in human years is approximately {dog.calc_lifespantoHuman():.2f} years.")
print(f"{cat.name} is a {cat.species} and {cat.name}'s age in human years is approximately {cat.calc_lifespantoHuman():.2f} years.")
print(f"{rabbit.name} is a {rabbit.species} and {rabbit.name}'s age in human years is approximately {rabbit.calc_lifespantoHuman():.2f} years.")

print(f"{dog.name} is a {dog.species} and has a lifespan of {dog.calc_lifespan()} years.")
print(f"{cat.name} is a {cat.species} and has a lifespan of {cat.calc_lifespan()} years.")
print(f"{rabbit.name} is a {rabbit.species} and has a lifespan of {rabbit.calc_lifespan()} years.")
