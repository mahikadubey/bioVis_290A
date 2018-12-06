import json


ensembl_ids_file = open('RedGenesFC1_ensembl_id.txt')
eids = ensembl_ids_file.readlines()

gene_ids_file = open('RedGenesFC1_gene_id.txt')
gids = gene_ids_file.readlines()

gene_dict = {}
for i in range(0,len(eids)):
    gene_dict[eids[i][:-2]] = gids[i][:-2]

file_object = open("evip_zscore.txt", "r")
data = []
all = file_object.readlines()
for line in all:
    split = line.split()

    gene_id = split[0][0:14]

    if gene_id in gene_dict:

        markers1 = str([float(split[1]), float(split[2]), float(split[3]), float(split[4])])
        wt = '{"title": "' + gene_dict[gene_id] + '" , "subtitle": "RNF43_WT", "ranges": [0, 8, 8], "measures": [1, 2, 3, 4, 5, 6, 7, 8], "markers":' + markers1 + '}'

        markers2 = str([float(split[5]), float(split[6]), float(split[7]), float(split[8])])
        gfp = '{"title": "' + gene_dict[gene_id] + '", "subtitle": "GFP", "ranges": [0, 8, 8], "measures": [1, 2, 3, 4, 5, 6, 7, 8], "markers":' + markers2 + '}'

        markers3 = str([float(split[9]), float(split[10]), float(split[11]), float(split[12])])
        fs659 = '{"title": "' + gene_dict[gene_id] + '", "subtitle": "RNF43_659fs", "ranges": [0, 8, 8], "measures": [1, 2, 3, 4, 5, 6, 7, 8], "markers":' + markers3 + '}'

        markers4 = str([float(split[13]), float(split[14]), float(split[15]), float(split[16])])
        fs117 = '{"title": "' + gene_dict[gene_id] + '", "subtitle": "RNF43_117fs", "ranges": [0, 8, 8], "measures": [1, 2, 3, 4, 5, 6, 7, 8], "markers":' + markers4 + '}'

        # Preferred Order: (GFP, WT, 117, 659)
        data.append(gfp)
        data.append(wt)
        data.append(fs117)
        data.append(fs659)

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
