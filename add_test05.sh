python main.py 2003 -s data/1000.txt > add_test05.out
echo "1000"
python main.py 10007 -s data/5000.txt >> add_test05.out
echo "5000"
python main.py 20011 -s data/10000.txt >> add_test05.out
echo "10000"
python main.py 100003 -s data/50000.txt >> add_test05.out
echo "50000"
python main.py 200003 -s data/100000.txt >> add_test05.out
echo "100000"
python main.py 1000003 -s data/500000.txt >> add_test05.out
echo "500000"
python main.py 2000003 -s data/1000000.txt >> add_test05.out
echo "1000000"
