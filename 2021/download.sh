DAY=$(date -d "$D" '+%-d')
echo 'Today is the' $DAY 'of December'
mkdir $DAY
mkdir $DAY'/resources'
echo "raw = [x for x in open('resources/input.txt')]" > $DAY'/solve.py'
touch $DAY'/resources/input.txt'
# curl 
