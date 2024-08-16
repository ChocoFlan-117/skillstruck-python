#Work schedule

work = {
    "Monday": 10, "Tuesday": 12, "Wednesday": 13, "Thursday": 11, "Friday": 16 
}

work["Saturday"] = 10

work.pop("Wednesday")

print(len(work))

if "Friday" in work:
    print("Friday is in the dictionary")