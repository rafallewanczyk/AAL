echo "przeprowadzam testy dodawania dla alfa = 1" 
python ../main.py 1009 -s ../data/1000.txt > add_test1.out
echo "skonczylem dodawanie 1000"
python ../main.py 5003 -s ../data/5000.txt >> add_test1.out
echo "skonczylem dodawanie 5000"
python ../main.py 10007 -s ../data/10000.txt >> add_test1.out
echo "skonczylem dodawanie 10000"
python ../main.py 50021 -s ../data/50000.txt >> add_test1.out
echo "skonczylem dodawanie 50000"
python ../main.py 100003 -s ../data/100000.txt >> add_test1.out
echo "skonczylem dodawanie 100000"
python ../main.py 500009 -s ../data/500000.txt >> add_test1.out
echo "skonczylem dodawanie 500000"
python ../main.py 1000003 -s ../data/1000000.txt >> add_test1.out
echo "skonczylem dodawanie 1000000"
python ../main.py 2000003 -s ../data/2000000.txt >> add_test1.out
echo "skonczylem dodawanie 2000000"
python ../main.py 3000017 -s ../data/3000000.txt >> add_test1.out
echo "skonczylem dodawanie 3000000"