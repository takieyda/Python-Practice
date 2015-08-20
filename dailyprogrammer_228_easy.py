#Practicing challenge #228 Easy from r/dailyprogrammer

list1 = ["billowy", "biopsy", "chinos", "defaced", "chintz", "sponged",\
        "bijoux", "abhors", "fiddle", "begins", "chimps", "wronged"]

for item in list1:
    if item == "".join(sorted(item)):
        print(item + " IN ORDER")
    elif item == "".join(sorted(item, reverse=True)):
        print(item + " REVERSE ORDER")
    else:
        print(item + " NOT IN ORDER")
      
