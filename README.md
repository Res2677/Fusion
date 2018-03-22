# Fusion

#get fusion reads from sam and tsv
`perl /public/home/hangjf/script/about_fusion/creat_all_fasta_for_STAR_tsv.pl -t /public/home/hangjf/cancer-changhai/result/STAR-Fusion-GRCh8/process/ZF013/ZF013-N/star-fusion.fusion_predictions.tsv -sam /public/home/hangjf/cancer-changhai/result/STAR-Fusion-GRCh8/process/ZF013/ZF013-N/std.Chimeric.out.sam -s ZF013 -o /public/home/hangjf/cancer-changhai/result/STAR-Fusion-GRCh8/fasta/ZF013-N`

#merge fasta
`perl /public/home/hangjf/script/about_fusion/merge.fusion.fasta.pl  /public/home/hangjf/cancer-changhai/result/STAR-Fusion-GRCh8/RNAfasta/ZF-RNA006-C/* >/public/home/hangjf/cancer-changhai/result/STAR-Fusion-GRCh8/DNA.ZF-RNA006-C.fasta`

#blat
`blat /public/home/hangjf/data/database/STAR/GRCh38_gencode_v26_CTAT_lib_July192017/ref_genome.fa /public/home/hangjf/cancer-changhai/result/STAR-Fusion-GRCh8/DNA_merge_fa/MERGE_ZF008-C.sh.o290610.fasta /public/home/hangjf/cancer-changhai/result/STAR-Fusion-GRCh8/DNA_blat/MERGE_ZF008-C.sh.o290610.fasta.psl`

#check and output
`for i in \`ls /public/home/hangjf/cancer-changhai/result/STAR-Fusion-GRCh8/RNA_blat|awk -F '.' '{print $2}'\`; do echo $i;python check_blat.py --psl=\`ls /public/home/hangjf/cancer-changhai/result/STAR-Fusion-GRCh8/RNA_blat/DNA.$i.fasta.psl\` --fa=\`ls /public/home/hangjf/cancer-changhai/result/STAR-Fusion-GRCh8/RNA_merge_fa/DNA.$i.fasta\` --out=/public/home/hangjf/cancer-changhai/result/STAR-Fusion-GRCh8/filter_fusion/RNA/$i.fusion.xls; done`

