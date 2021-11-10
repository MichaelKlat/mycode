# standard library
import csv
with open("pokedex.txt","r") as pokefile:
    for pokedict in csv.DictReader(pokefile):
        print(f"{pokedict['Name']} is of the {pokedict['Type 1']} type and has {pokedict['HP']} hit points.")
