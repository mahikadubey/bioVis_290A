file_object  = open("evip_zscore.txt", "r")
current_min = 0
current_max = 1
firstline = False
all = file_object.readlines()
for line in all[1:]:
    split = line.split()
    for item in split:
        #print(float(item))
        itemlist = list(item)
        if itemlist[0] != "E":
            print(float(item))
            if (float(item) < current_min):
                current_min = float(item)
            if (float(item) > current_max):
                current_max = float(item)

print("max = " + str(current_max))
print("min = " + str(current_min))
