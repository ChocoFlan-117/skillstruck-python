ride = {
    "Sam": 96,
    "Dan": 100,
    "Eren": 122,
    "Mary": 87,
    "Anne": 32
}

for x in ride.values():
    if x >= 100:
        print("This person is tall enough to ride.")
    else:
        print("This person is too short to ride.")