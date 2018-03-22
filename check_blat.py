import os
import argparse
import linecache
from itertools import islice
parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('--psl', type = str, default = None)
parser.add_argument('--fa', type = str, default = None)
parser.add_argument('--out', type = str, default= None)
args = parser.parse_args()
miss_max = 2;
q_gap_max = 2;
t_gap_max = 2;

fudict = {}
psl_file = open(args.psl)
for line in islice(psl_file, 5, None):
  mess = line.strip().split()
  #print mess[1],mess[5],mess[6]
  if (int(mess[1]) <= miss_max and int(mess[5]) <= q_gap_max and int(mess[6]) <= t_gap_max):
    #print mess
    if mess[9] in fudict.keys():
      fudict[mess[9]].append(line)
    else:
      fudict[mess[9]] =[]

final_dict = dict()
for fusion in fudict.keys():
  if fudict[fusion] == []:
    continue
  fusion_arr = fusion.split('.')
  fusion_name = fusion_arr[1]
  upstream_arr = []
  downstream_arr = []
  upstream = ''
  downstream = ''
  upstream_max = 0
  cc = fudict[fusion][0].split()
  downstream_min = int(cc[10])
  length = int(cc[10])
  for line in fudict[fusion]:
    mess = line.split()
    if (int(mess[11]) == 0 and int(mess[12]) == int(mess[10]) ):
      pass
    elif (int(mess[11]) == 0):
      if (int(mess[12]) >= upstream_max):
        upstream_arr.append(mess[11])
        upstream_arr.append(mess[12])
        upstream = line
        upstream_max = int(mess[11])
    elif (int(mess[12]) == length):
      if (int(mess[11]) <= downstream_min):
        downstream_arr.append(mess[11])
        downstream_arr.append(mess[12])
        downstream = line
        downstream_min = int(mess[12])
    else:
      pass
    if (len(upstream_arr)>1 and len(downstream_arr)>1):
      pp = int(upstream_arr[1]) - int(downstream_arr[0])
      #print pp
      try:
        if (pp > -2):
          res = upstream + downstream.strip()
          final_dict[fusion_name] = res
          #print upstream,downstream
      except:
        pass

#print final_dict
out_file = open(args.out,'w')
print >> out_file,'fusion\tsequence\tleft part\tleft seq\tleft on ref\tright part\tright seq\tright on ref'
fasta_c = len(open(args.fa).readlines())
for i in range(fasta_c):
  if (i-1) % 2 == 0:
    fu = linecache.getline(args.fa,i)
    seq = linecache.getline(args.fa,i+1).strip()
    fu_name = fu.strip('>').strip().split('.')[1]
    #print fu_name
    #print fu_name + '\n' + seq.strip()
    if fu_name in final_dict.keys():
      up_mess = final_dict[fu_name].split('\n')[0]
      up_mess_arr = up_mess.split('\t')
      down_mess = final_dict[fu_name].split('\n')[1]
      down_mess_arr = down_mess.split('\t')
      #for pos in range(int(up_mess_arr[11]),int(up_mess_arr[12])):
      #  up_seq = up_seq + seq_arr[pos]
      up_seq = seq[int(up_mess_arr[11]):int(up_mess_arr[12])]
      down_seq = seq[int(down_mess_arr[11]):int(down_mess_arr[12])]
      up_sppos = up_mess_arr[13]+up_mess_arr[8]+':'+up_mess_arr[15]+'-'+up_mess_arr[16]
      down_sppos = down_mess_arr[13]+down_mess_arr[8]+':'+down_mess_arr[15]+'-'+down_mess_arr[16]
      fu_m = fu_name + '\t' + seq
      up_m = up_mess_arr[11]+'-'+up_mess_arr[12]+'\t'+up_seq+'\t'+up_sppos
      down_m = down_mess_arr[11]+'-'+down_mess_arr[12]+'\t'+down_seq+'\t'+down_sppos
      #print 'up_seq: ' + seq[int(up_mess_arr[11]):int(up_mess_arr[12])] + '\n' + 'down_seq: ' + seq[int(down_mess_arr[11]):int(down_mess_arr[12])]
      print >> out_file,fu_m + '\t' + up_m + '\t' + down_m
      #print (up_mess +'\n' + down_mess + '\n')
