#!/usr/bin/python3
"""RZFeeser | Alta3 Research
   Printing dictionary data stored as lists to the screen"""

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

farm_list = [key["name"] for key in farms]
#farm_list = list(farms.keys("names"))
#farm_list = []
#
#for dict in farms:
#    farm_list.append(dict["name"])

animals = ("sheep", "cows", "pigs", "chickens", "llamas", "cats")

vegtables = ("carrots", "celery")

print(animals)
print(vegtables)

def main():
    """On this farm there was a..."""

    # this is the data we want to loop across
    # it is a list containing 3 dictionaries
    #farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},

    # each time through the loop
    # farm will be equal to one of the dict within the list "farms"
    for farm in farms:
        #print(farm)   # this might be a good "first step" after developing the loop
        print(farm.get("name", "Unknown Farm"), end=":\n")  # this is like saying, "farm['name']"
                                                 # only it will not return an error
        for agri in farm.get("agriculture"):     # from a single "farm" get the list from the key "agriculture"
            print("  -", agri)                   # each time through the list "agriculture", print out an item


def main1():
    """On this farm there was a..."""

    # this is the data we want to loop across
    # it is a list containing 3 dictionaries
    #farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
    farm1 = input(f"Choice a farm: {farm_list}: ")    

    # each time through the loop
    # farm will be equal to one of the dict within the list "farms"
        #print(farm)   # this might be a good "first step" after developing the loop
                                                 # only it will not return an error
    for farm in farms == farm1:
        if farm.name:
        #print(farm)   # this might be a good "first step" after developing the loop
            print(farm.get("name", "Unknown Farm"), end=":\n")  # this is like saying, "farm['name']"
                                                 # only it will not return an error
            for agri in farm.get("agriculture"):     # from a single "farm" get the list from the key "agriculture"
                print("  -", agri)                   # each time through the list "agriculture", print out an item



main()
main1()
#main2()
