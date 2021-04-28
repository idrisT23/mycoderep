#!/usr/bin/env python3
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]


##Ask a user to choose a farm (NE Farm, W Farm, or SE Farm)... but only return ANIMALS from that particular farm.

FarmName = input("Which farm's plants/animals do you want to see(NE Farm, W Farm, SE Farm)? ").lower()

for farm in farms:
        if farm['name'].lower() == FarmName:
            NEFarm = farm['agriculture']
            for animal in NEFarm: 
                if animal in ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]:
                    print(f'{animal}')
       
