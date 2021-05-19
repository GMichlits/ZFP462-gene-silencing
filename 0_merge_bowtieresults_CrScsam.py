__author__ = 'georg.michlits'

# The program gets the aligned reads from Thomas (bowtie 2MM alignment) and takes them out of the sam file

sample_name = input('enter filename/samplename of your choice: ')
bowtie_result_file = open(input('enter bowtie result file path: '),'r')
CrScsam_file = open(input('enter short (1,10,12,14) sam file path: '),'r')
output_file0 = open('out_0_'+sample_name,'w')

#first make a dict with coordinates. then search for every line of the NGS file if it is in the dict. if yes print it to the output file.

coordinates_d = {}
n=1
mm1 = 0
mm2 = 0
mm0 = 0

print('reading in bowtie file')
i = 0
for line in bowtie_result_file:
    i = i + 1
    #k = int(i/1000000)
    #print(str(k) + '\t' + str(i))
    element = line.rstrip('\n').split('\t')
    coordinate = element[0]
    genename = element[2]
    n = n+1
    coordinates_d[coordinate] = genename
    if element[13][5] == '0':       #element [13][5] give the number of mismatches
        mm0 = mm0+1
    if element[13][5] == '1':
        mm1 = mm1+1
    if element[13][5] == '2':
        mm2 = mm2+1
print('total lines = ' + str(n))
print('mm0 = ' + str(mm0) + '\t' +'mm1 = ' + str(mm1) + '\t' +'mm2 = ' + str(mm2))

n_yes = 0
n_no = 0
i = 0
print ('search lines in CrSc.sam file')
for line in CrScsam_file:
    i = i + 1
    k = int(i/1000000)
    print(str(k) + '\t' + str(i))
    element = line.rstrip('\n').split('\t')
    coordinate = element[0]
    if coordinate in coordinates_d:
        n_yes = n_yes + 1
        output_file0.write(line.rstrip('\n') + '\t' + coordinates_d[coordinate] +'\n')
    else:
        n_no = n_no + 1
print('n_no = ' + str(n_no) + '\t' + 'n_yes = ' + str(n_yes))