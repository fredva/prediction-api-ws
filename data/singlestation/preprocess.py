import datetime

f = open("temperatures.original.txt")

lines = f.readlines()

def stationname(id):
    if id == "18700":
        return "BLINDERN"
    elif id == "41770":
        return "LINDESNES"
    elif id == "69100":
        return "VAERNES"
    else:
        return "KAUTOKEINO"

def dateordinal(datestr):
    date = datetime.datetime.strptime(datestr, "%d.%m.%Y")
    if date.day == 29 and date.month == 2:
        return date.replace(day=28, year=1).toordinal()
    else:
        return date.replace(year=1).toordinal()

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
    name = stationname(station)
    ordinal = dateordinal(date)
    if name is not "BLINDERN":
        continue
    try:
        int(ordinal)
        float(tam)
    except:
        continue

    print "{},{}".format(tam, ordinal)

f.close()
