__author__ = 'georg.michlits'

__author__ = 'georg.michlits'

sample_name = input('enter filename/samplename: ')
indexfilename = input('enter indexfilename path: ')
guidefile_name = input('enter guidefile_filename: ')
input_out0_file = open('out_0_'+sample_name, 'r')
Indexfile = open(indexfilename,'r')
sgALLfile = open(guidefile_name,'r')
output_2_MD = open('out_2_'+sample_name+'i'+ '0MM_MD.sam','w')
output_1_kicked_f = open('out_1_'+sample_name+'i'+'0MM_kicked.sam','w')

#create index dictonaries that contain information on indices

Indexdict = {}
for line in Indexfile:
    element = line.rstrip('\n').split(',')
    Exp_name = element[1]
    Index_n = element[5]
    Indexdict[Index_n] = Exp_name
print('Index dictionaries done')
Indexfile.close()

#from allguides creat dict that counts in experiments - clones - count
gDNA = {}
readout = {}
for line in sgALLfile:
    element = line.rstrip('\n').split('\t')
    gDNAname = (element[0])
    guide20nt = element[1]
    gDNA[gDNAname] = guide20nt
    readout[gDNAname] = {}
sgALLfile.close()

index_match = 0
index_fail = 0
total_lines = 0

ruled_out_index = 0
print('reading NGS.sam file')
print('generating MD_dict')
for line in input_out0_file:
    if not line == '\n' or '':
        total_lines = total_lines + 1
        print(total_lines)
        element = line.rstrip('\n').split('\t')
        gDNAname = element[4]
        bc2_index = element[2][5:11]
        barcode = element[3][5:15]

        if bc2_index in Indexdict:
            index_match = index_match + 1
            exp_name = Indexdict[bc2_index]
            #guide20nt = gDNA[gDNAname]
            #count it into the readoutdictionary
            #readout = {'gDNAname:{index:{barcode:count}}}
            if not exp_name in readout[gDNAname]:
                readout[gDNAname][exp_name] = {}
            if not barcode in readout[gDNAname][exp_name]:
                readout[gDNAname][exp_name][barcode] = 0
            readout[gDNAname][exp_name][barcode] = readout[gDNAname][exp_name][barcode] + 1

        else:
            output_1_kicked_f.write(line)
            index_fail = index_fail + 1
input_out0_file.close()

print('total lines: ' + str(total_lines))
print('cleaned lines (index match): ' + str(index_match))
print('kicked lines (index fail): ' + str(index_fail))

# write output file (to view or to save - the saved file can later be used to read in the dict again)

print('writing Masterdict')
for gDNAname in sorted(readout):
    for exp_name in sorted(readout[gDNAname]):
        for i in sorted(readout[gDNAname][exp_name].items(), key=lambda t: t[1], reverse=True):
            barcode = i[0]
            c = i[1]
            output_2_MD.write(gDNAname + '\t' + exp_name + '\t' + barcode + '\t' + str(c) + '\n')

print('writing Masterdict finished')
output_2_MD.close()