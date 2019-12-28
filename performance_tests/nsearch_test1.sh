echo "przeprowadzam testy n wyszukan dla alfa = 1" 
python ../main.py 1009 -n ../data/1000.txt > nsearch_test1.out
echo "zakonczylem n przeszukan dla 1000"
python ../main.py 5003 -n ../data/5000.txt >> nsearch_test1.out
echo "zakonczylem n przeszukan dla 5000"
python ../main.py 10007 -n ../data/10000.txt >> nsearch_test1.out
echo "zakonczylem n przeszukan dla 10000"
python ../main.py 50021 -n ../data/50000.txt >> nsearch_test1.out
echo "zakonczylem n przeszukan 50000"
python ../main.py 100003 -n ../data/100000.txt >> nsearch_test1.out
echo "zakonczylem n przeszukan dla 100000"
python ../main.py 500009 -n ../data/500000.txt >> nsearch_test1.out
echo "zakonczylem n przeszukan 500000"
python ../main.py 1000003 -n ../data/1000000.txt >> nsearch_test1.out
echo "zakonczylem n przeszukan dla 1000000"
