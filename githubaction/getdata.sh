wget "https://docs.google.com/spreadsheets/d/"$1"/export?format=tsv&gid=0" -O $1.tsv
tail +10 $1.tsv | head -100 > $1-100.tsv

