#Permission Slips#

permission = [str(n) for n in input("Input a list of names separated by spaces").split()]

slips = dict.fromkeys(permission, "yes")

#variations:
if "George" in slips:
    slips["George"] = "no"

if "Veronica" in slips:
    slips.pop("Veronica")
####

print(slips)
