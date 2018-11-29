import json

file_object  = open("evip_zscore.txt", "r")
data = []
all = file_object.readlines()
for line in all[1:]:
    split = line.split()

    first = '{"title": "' + str(split[0]) + '" , "subtitle": "RNF43_WT", "ranges": [0, 8, 8], "measures": [4, 8], "markers":' + str([float(split[1]), float(split[2]), float(split[3]), float(split[4])]) + '}'
    data.append(first)

    second = '{"title": "", "subtitle": "GFP", "ranges": [0, 8, 8], "measures": [4, 8], "markers":' + str([float(split[5]), float(split[6]), float(split[7]), float(split[8])]) + '}'
    data.append(second)

    third = '{"title": "", "subtitle": "RNF43_659fs", "ranges": [0, 8, 8], "measures": [4, 8], "markers":' + str([float(split[9]), float(split[10]), float(split[11]), float(split[12])]) + '}'
    data.append(third)

    fourth = '{"title": "", "subtitle": "RNF43_117fs", "ranges": [0, 8, 8], "measures": [4, 8], "markers":' + str([float(split[13]), float(split[14]), float(split[15]), float(split[16])]) + '}'
    data.append(fourth)

datajson = json.dumps(data)
print(datajson)

with open('data_reorg.json', 'w') as outfile:
    outfile.write('[')
    outfile.write('\n')
    for dataline in data:
        outfile.write('  ')
        outfile.write(dataline)
        if (dataline != data[-1]):
            outfile.write(',')
        outfile.write('\n')
    outfile.write(']')
#print("max = " + str(current_max))
#print("min = " + str(current_min))
