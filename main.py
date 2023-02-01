from art import artwork
# Creates a dictionary that includes the object name as well as the associated gravitational acceleration
Gravitational_Acceleration = {
    "sun": 274,
    "mercury": 3.7,
    "venus": 8.9,
    "earth": 9.8,
    "earth's moon": 1.6,
    "mars": 3.7,
    "jupiter": 24.8,
    "europa": 1.3,
    "saturn": 10.4,
    "titan": 1.4,
    "uranus": 8.9,
    "neptune": 11.2,
    "neutron star": 9.8 * 10 ** 9
}
# prints ASCII art
print(artwork)
# asks user for their weight in lbs
earth_weight = float(input("Please enter your weight in pounds (lbs) to see what you'd way on various astronomical "
                           "objects: "))
# calculates  the user's mass
mass = earth_weight / Gravitational_Acceleration["earth"]
# loops through each item in the dictionary
for object_name, object_gravitational_acceleration in Gravitational_Acceleration.items():
    # calculates new weight for each item in dictionary
    new_weight = mass * object_gravitational_acceleration
    # prints user's formatted new weight
    print(f"{object_name.capitalize()}: {round(new_weight):,} lbs")
