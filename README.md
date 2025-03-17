# Index_generator
Generate random DNA sequences, such that every pair of sequences has a Hamming distance larger than specified one, for use in NextSeq 1000/2000 (Two-Channel Sequencing Chemistry).

Variables : 
- n : number of sequences. default; 20.
- m : length of each sequence. default; 8.
- min_haming : haming distance. default; 4.
- gc_content : %max gc content for index seqence. default; 70.

other conditions:
- Each position [0 – m-1] has at least one C or T across all sequences.
- Each index does not start with GG.

ref :
https://support-docs.illumina.com/SHARE/IndexAdaptersPooling/Content/SHARE/IndexAdaptersPooling/SequencingChemistry.htm
