from algorithms.HashTable import HashTable
from algorithms.Generator import Generator
import argparse
import os
import time


def main():
    parser = argparse.ArgumentParser(description="Program obslugujacy tablice mieszajaca")
    group = parser.add_argument_group()
    parser.add_argument("size", type=int, help="Rozmiar tablicy mieszajace")
    parser.add_argument("-i", "--input", action="store_true", help="Program czyta dane z wejscia standardowego")
    group.add_argument("-g", "--generator", type=str,
                        help="Program używa generatora w celu uzyskania danych")


    parser.add_argument("-s", "--statistic", type=str,
                        help="Program używa generatora oraz prowadzi statystyke")
    parser.add_argument("-e", "--enumeration", type=str, help="Program przeprowadza analize dla enumeracji tablicy")
    args = parser.parse_args()

    hashtable = HashTable(args.size)
    if args.input:
        print("add, delete, find, getall, exit")
        while (True):
            g = input("podaj operacje : ")

            try:
                operation = g.split()[0]
                argument = g.split()[1]

            except IndexError:
                operation = g

            if operation == "add":
                hashtable.insert(argument)
            elif operation == "delete":
                hashtable.delete(argument)
            elif operation == "find":
                print(f"znaleziono na pozycji {hashtable.find(argument)}")
            elif operation == "getall":
                print(hashtable.getall())
            elif operation == "exit":
                break

    if args.generator:
        if "http" in args.generator:
            os.system(f"wget -O index.html {args.generator}")
            adress = "index.html"
        else :
            adress = args.generator
        for word in Generator(adress).generate(): hashtable.insert(word)
        print(hashtable.getall())

    if args.statistic:
        if "http" in args.statistic:
            os.system(f"wget -O index.html {args.statistic}")
            adress = "index.html"
        else :
            adress = args.statistic

        totaltime = 0
        mintime = float("inf")
        maxtime  = 0

        all = Generator(adress).generate()
        for word in all:
            start = time.time()
            hashtable.insert(word)
            end = time.time()
            totaltime += (end - start)
            mintime = min(mintime, end-start)
            maxtime = max(maxtime, end-start)

        print(f"maxtime: {maxtime}, mintime: {mintime}, totaltime: {totaltime}, average: {totaltime/len(all)}, fulfillment: {hashtable.getSize()/hashtable.K}, accepted: {hashtable.getSize()/len(all)}")

    if args.enumeration:
        if "http" in args.enumeration:
            os.system(f"wget -O index.html {args.enumeration}")
            adress = "index.html"
        else :
            adress = args.enumeration

        totaltime = 0
        mintime = float("inf")
        maxtime  = 0

        all = Generator(adress).generate()
        for word in all:
            hashtable.insert(word)

        for word in all:
            start = time.time()
            hashtable.find(word)
            end = time.time()
            maxtime=max(end-start, maxtime)
            mintime=min(end-start, mintime)
            totaltime+=end-start
        print(f"{adress} : maxtime: {maxtime}, mintime: {mintime}, totaltime: {totaltime}, average: {totaltime / len(all)}, fulfillment: {hashtable.getSize() / hashtable.K}, accepted: {hashtable.getSize() / len(all)}")

if __name__ == "__main__":
    main()
