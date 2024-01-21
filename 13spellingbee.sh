# co-authors: Madison An and Jaime Young
gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "r" | grep -v "[bdefghjklmpqstuvwxy]" | grep -E ".{4,}"