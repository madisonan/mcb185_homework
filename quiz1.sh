# authors: Jaime Young and Madison An

gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "a" | grep -v "[bdeghijklnpqrsuvwxyz]" | grep -E ".{4,}" | wc -l
gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "a" | grep -v "[bdeghijklnpqrsuvwxyz]" | grep -E ".{4,}"
gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "b" | grep -v "[cdefghjkmopqsuvwxyz]" | grep -E ".{4,}" | wc -l
gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "b" | grep -v "[cdefghjkmopqsuvwxyz]" | grep -E ".{4,}"
gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "c" | grep -v "[befghjklpqrstuvwxyz]" | grep -E ".{4,}" | wc -l
gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "c" | grep -v "[befghjklpqrstuvwxyz]" | grep -E ".{4,}"
gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "z" | grep -v "[bcdefhjklmpqstuvwxy]" | grep -E ".{4,}" | wc -l
gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "z" | grep -v "[bcdefhjklmpqstuvwxy]" | grep -E ".{4,}"

gunzip -c ~/Code/MCB185/data/jaspar2024_core.transfac.gz | echo "diatoms | gregunzip -c ~/Code/MCB185/data/jaspar2024_core.transfac.gz | grep "diatoms" | grep wc -l
gunzip -c ~/Code/MCB185/data/jaspar2024_core.transfac.gz | grep "urochordates" | grep wc -l
gunzip -c ~/Code/MCB185/data/jaspar2024_core.transfac.gz | grep "nematodes" | grep wc -l
gunzip -c ~/Code/MCB185/data/jaspar2024_core.transfac.gz | grep "fungi" | grep wc -l
gunzip -c ~/Code/MCB185/data/jaspar2024_core.transfac.gz | grep "insects" | grep wc -l
gunzip -c ~/Code/MCB185/data/jaspar2024_core.transfac.gz | grep "plants" | grep wc -l
gunzip -c ~/Code/MCB185/data/jaspar2024_core.transfac.gz | grep "vertebrates" | grep wc -l 
