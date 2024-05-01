import datetime
current = datetime.datetime.now()
filen = ""
ops = ["%Y", "%m", "%d", "%H", "%M", "%S"]
for loop in range(6):
    filen = filen + current.strftime(ops[loop])

filen = filen[:8] + "-" + filen[-6:] + ".png"
print(filen)

