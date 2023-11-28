# Nick Fernandes
# Inter Planetary Weights w/ Dict

#dictionary of surface gravity
gravity_dict = {
    "Mercury": 0.38,
    "Venus": 0.91,
    "Moon": 0.165,
    "Mars": 0.38,
    "Jupiter": 2.34,
    "Saturn": 0.93,
    "Uranus": 0.92,
    "Neptune": 1.12,
    "Pluto": 0.066
}

#inputs
name = input("What is your name: ")
earth_weight = float(input("What is your Earth weight in lbs: "))
print(f"{name}, here are your weights on our Solar System's planets:")

#loop thru dict and output converted weight
for key, value in gravity_dict.items():
    converted_weight = value * earth_weight
    print(f"Weight on {key:8}{converted_weight:10.2f}")
