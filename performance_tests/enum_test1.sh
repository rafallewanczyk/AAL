echo "przeprowadzam testy enumeracij dla alfa = 1" 
python ../main.py 1009 -n ../data/1000.txt > enum_test1.out
echo "zakonczylem enumeracji dla 1000"
python ../main.py 5003 -n ../data/5000.txt >> enum_test1.out
echo "zakonczylem enumeracji dla 5000"
python ../main.py 10007 -n ../data/10000.txt >> enum_test1.out
echo "zakonczylem enumeracji 10000"
python ../main.py 50021 -n ../data/50000.txt >> enum_test1.out
echo "zakonczylem enumeracji dla 50000"
python ../main.py 100003 -n ../data/100000.txt >> enum_test1.out
echo "zakonczylem enumeracji dla 100000"
python ../main.py 5000009 -n ../data/500000.txt >> enum_test1.out
echo "zaknczylem enumeracji dla 500000"
python ../main.py 1000003 -n ../data/1000000.txt >> enum_test1.out
echo "zakonczylem enumeracji dla 1000000"
python ../main.py 2000003 -n ../data/2000000.txt >> enum_test1.out
echo "skonczylem enumeracje 2000000"
python ../main.py 3000017 -n ../data/3000000.txt >> enum_test1.out
echo "skonczylem enumeracje 3000000"
