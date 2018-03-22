use Data::Dumper;
use Getopt::Long;
my ($tsv,$sam,$sample,$out,$help);
GetOptions(
        "t=s" => \$tsv,
        "sam=s" => \$sam,
        "s=s" => \$sample,
        "o=s" => \$out,
        "h|?" => \$help
);
if (!defined $tsv || !defined $sam || !defined $sample || !defined $out ||defined $help) {
        die << "USAGE";
        description: cluster
        usage: perl $0 [options]
options:
        -t <file>    *tsv file from STAR_Fusion
        -sam <file>    *sam file from STAR_Fusion
        -s  <string>  sample name
        -o  <path>    outdir
        -help|?       information for help
e.g.:
perl $0 -ct 
USAGE
}

`mkdir -p $out/$sample`;
open TSV,$tsv,or die $!;
<TSV>;
while(<TSV>)
{
        chomp;
        @a =split/\t/,$_;
        $a[8]=~s/,/|/g;
        $fusion_id{$a[0]} = $a[8];
}

foreach $fusion (keys %fusion_id)
{
        open OUT,">$out/$sample/fusion.$fusion.fasta",or die $!;
        $cmd = "grep -E \'$fusion_id{$fusion}\' $sam|grep -v \'=\'|awk \'{print \">\"\$1\" $sample $fusion\\n\"\$10}\'";
        #print "$cmd";
        $fasta = `$cmd`;
        print OUT "$fasta";
        close OUT;
}
