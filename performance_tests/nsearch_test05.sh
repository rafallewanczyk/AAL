echo "przeprowadzam testy n przeszukan dla alfa = 0.5" 
python ../main.py 2003 -n ../data/1000.txt > nsearch_test05.out
echo "zakonczylem n przeszukan dla 1000"
python ../main.py 10007 -n ../data/5000.txt >> nsearch_test05.out
echo "zakonczylem n przeszukan dla 5000"
python ../main.py 20011 -n ../data/10000.txt >> nsearch_test05.out
echo "zakonczylem n przeszukan 10000"
python ../main.py 100003 -n ../data/50000.txt >> nsearch_test05.out
echo "zakonczylem n przeszukan dla 50000"
python ../main.py 200003 -n ../data/100000.txt >> nsearch_test05.out
echo "zakonczylem n przeszukan dla 100000"
python ../main.py 1000003 -n ../data/500000.txt >> nsearch_test05.out
echo "zaknczylem n przeszukan dla 500000"
python ../main.py 2000003 -n ../data/1000000.txt >> nsearch_test05.out
echo "zakonczylem n przeszukan dla 1000000"
