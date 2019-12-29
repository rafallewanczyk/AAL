echo "przeprowadzam testy enumeracij dla alfa = 0.5" 
python ../main.py 2003 -e ../data/1000.txt > enum_test05.out
echo "zakonczylem enumeracje dla 1000"
python ../main.py 10007 -e ../data/5000.txt >> enum_test05.out
echo "zakonczylem enumeracje dla 5000"
python ../main.py 20011 -e ../data/10000.txt >> enum_test05.out
echo "zakonczylem enumeracje 10000"
python ../main.py 100003 -e ../data/50000.txt >> enum_test05.out
echo "zakonczylem enumeracje dla 50000"
python ../main.py 200003 -e ../data/100000.txt >> enum_test05.out
echo "zakonczylem enumeracje dla 100000"
python ../main.py 1000003 -e ../data/500000.txt >> enum_test05.out
echo "zaknczylem enumeracje dla 500000"
python ../main.py 2000003 -e ../data/1000000.txt >> enum_test05.out
echo "zakonczylem enumeracje dla 1000000"
python ../main.py 4000037 -e ../data/2000000.txt >> enum_test05.out
echo "skonczylem enumeracje 2000000"
python ../main.py 6000011 -e ../data/3000000.txt >> enum_test05.out
echo "skonczylem enumeracje 3000000"
