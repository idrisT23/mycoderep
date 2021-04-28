#!/usr/bin/env python3

heroes=  {
"wolverine":
    {"real name": "James Howlett",
    "powers": "regeneration",
    "archenemy": "Sabertooth",},
"harry potter":
    {"real name": "Harry Potter",
    "powers": "magic",
    "archenemy": "Voldemort",},
"captain america":
    {"real name": "Steve Rogers",
    "powers": "frisbee shield",
    "archenemy": "Hydra",}
        }
character_name = input("Which character do you want to know about? (Wolverine, Harry Potter, Captain America)")
statistic = input("What statistic do you want to know about? (real name, powers, archenemy)")

print (heroes[character_name].get(statistic, "this is not a real character"))



