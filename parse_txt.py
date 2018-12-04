import json

file_object  = open("evip_zscore.txt", "r")
data = []
all = file_object.readlines()
for line in all[1:3]:
    split = line.split()

    gene_id = split[0]

    markers1 = str([float(split[1]), float(split[2]), float(split[3]), float(split[4])])
    avg1 = str([(float(split[1]) + float(split[2]) + float(split[3]) + float(split[4]))/4.0])

    first = '{"title": "' + str(gene_id[0:4]) + '-' + str(gene_id[10:]) + '" , "subtitle": "RNF43_WT", "ranges": [0, 8, 8], "measures": [1, 2, 3, 4, 5, 6, 7, 8], "markers":' + markers1 + '}'
    data.append(first)

    markers2 = str([float(split[5]), float(split[6]), float(split[7]), float(split[8])])
    avg2 = str([(float(split[5]) + float(split[6]) + float(split[7]) + float(split[8]))/4.0])

    second = '{"title": "' + str(gene_id[0:4]) + '-' + str(gene_id[10:]) + '", "subtitle": "GFP", "ranges": [0, 8, 8], "measures": [1, 2, 3, 4, 5, 6, 7, 8], "markers":' + markers2 + '}'
    data.append(second)

    markers3 = str([float(split[9]), float(split[10]), float(split[11]), float(split[12])])
    avg3 = str([(float(split[9]) + float(split[10]) + float(split[11]) + float(split[12]))/4.0])

    third = '{"title": "' + str(gene_id[0:4]) + '-' + str(gene_id[10:]) + '", "subtitle": "RNF43_659fs", "ranges": [0, 8, 8], "measures": [1, 2, 3, 4, 5, 6, 7, 8], "markers":' + markers3 + '}'
    data.append(third)

    markers4 = str([float(split[13]), float(split[14]), float(split[15]), float(split[16])])
    avg4 = str([(float(split[13]) + float(split[14]) + float(split[15]) + float(split[16]))/4.0])

    fourth = '{"title": "' + str(gene_id[0:4]) + '-' + str(gene_id[10:]) + '", "subtitle": "RNF43_117fs", "ranges": [0, 8, 8], "measures": [1, 2, 3, 4, 5, 6, 7, 8], "markers":' + markers4 + '}'
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
