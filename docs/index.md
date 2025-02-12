`dnaapler` is a simple python program that takes a single nucleotide input sequence (in FASTA format), finds the desired start gene using `blastx` against an amino acid sequence database, checks that the start codon of this gene is found, and if so, then reorients the chromosome to begin with this gene on the forward strand. 

It was originally designed to replicate the reorientation functionality of [Unicycler](https://github.com/rrwick/Unicycler/blob/main/unicycler/gene_data/repA.fasta) with dnaA, but for for long-read first assembled chromosomes. I have extended it to work with plasmids (`dnaapler plasmid`) and phages (`dnaapler phage`), or for any input FASTA desired with `dnaapler custom`, `dnaapler mystery` or `dnaapler nearest`.

Additionally, you can also reorient multiple bacterial chromosomes/plasmids/phages at once using the `dnaapler bulk` subcommand.

If your input FASTA is mixed (e.g. has chromosome and plasmids), you can also use `dnaapler all`, with the option to ignore some contigs with the `--ignore` parameter. 

For bacterial chromosomes, `dnaapler chromosome` should ensure the chromosome breakpoint never interrupts genes or mobile genetic elements like prophages. It is intended to be used with good-quality completed bacterial genomes, generated with methods such as [Trycycler](https://github.com/rrwick/Trycycler/wiki), [Dragonflye](https://github.com/rpetit3/dragonflye) or  [hybracter](https://github.com/gbouras13/hybracter).

A clear schematic of what dnaapler is trying to achieve is presented below:

![Image](Dnaapler_figure.png)