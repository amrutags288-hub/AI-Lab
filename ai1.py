def reflex_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Right"
    else:
        return "Left"


# Initial Environment
environment = {
    "A": "Dirty",
    "B": "Dirty"
}

location = "A"

print("Initial Environment:", environment)

while True:
    status = environment[location]
    action = reflex_agent(location, status)

    print(f"\nLocation: {location}")
    print(f"Status  : {status}")
    print(f"Action  : {action}")

    if action == "Suck":
        environment[location] = "Clean"

    elif action == "Right":
        location = "B"

    elif action == "Left":
        location = "A"
    if environment["A"] == "Clean" and environment["B"] == "Clean":
        print("\nFinal Environment:", environment)
        print("Goal Achieved: Both rooms are clean.")
        break