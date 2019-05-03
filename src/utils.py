def writeCSV(name, values):
    try:
        csv = open(name, "w", encoding="UTF-8")
        new = "\n".join(str(x) for x in values)
        csv.write(new)
        csv.close()
    except IOError:
        print("Invalid name")
