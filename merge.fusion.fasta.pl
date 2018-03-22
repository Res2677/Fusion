use Data::Dumper;
`cd $ARGV[0]`;
$all_fasta = `find $ARGV[0] |grep '.fasta'`;
@file = split/\n/,$all_fasta;
shift @file;
foreach $fa (@file)
{
        @mm = split/\//,$fa;
        $mer_read=`perl /public/home/hangjf/script/Algorithm/small_read_merg.pl -fa $fa -overlap 15 -dis 0.999`;
        print ">$mm[-1]\n$mer_read";
}
