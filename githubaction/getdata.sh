wget 'https://docs.google.com/spreadsheets/d/1qTqvAzQWizPQX67-ou0IDQWJCQ_GypvRMhYtUMbl_MA/export?format=csv&gid=1838501433' -O test3.csv
tail +10 test3.csv | head -100 > test3-100.csv

