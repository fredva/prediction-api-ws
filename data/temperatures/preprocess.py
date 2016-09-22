import datetime

def stationname(id):
    if id == "18700":
        return "BLINDERN"
    elif id == "41770":
        return "LINDESNES"
    elif id == "69100":
        return "VAERNES"
    else:
        return "KAUTOKEINO"

def stationcoord(id):
    if id == "18700":
        return 59.9423
    elif id == "41770":
        return 57.9826
    elif id == "69100":
        return 63.4596
    else:
        return 68.9968


def dateordinal(datestr):
    date = datetime.datetime.strptime(datestr, "%d.%m.%Y")
    if date.day == 29 and date.month == 2:
        return date.replace(day=28, year=1).toordinal()
    else:
        return date.replace(year=1).toordinal()

if __name__ == "__main__":
    f = open("temperatures.original.txt")

    lines = f.readlines()


    # Fjern alt i toppen
    for i in range(len(lines)):
        line = lines.pop(0)
        if line.startswith("Stnr;Dato"):
            break

    for line in lines:
        if line.isspace():
            break
        if "x" in line:
            continue
        station, date, tam, tan, tax = line.split(";")
        ordinal = dateordinal(date)
        try:
            int(ordinal)
            float(tam)
        except:
            continue

        #print "{},\"{}\",{}".format(tam, stationname(station), ordinal)
        print "{},{},{}".format(tam, stationcoord(station), ordinal)

    f.close()
