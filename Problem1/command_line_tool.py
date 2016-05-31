#!/usr/bin/env python3

import argparse
from bs4 import BeautifulSoup
import sys
import os
import webbrowser
from PyDictionary import PyDictionary
dictionary = PyDictionary()


def extract(filename):
    file = open(filename)
    contents = file.read()
    soup = BeautifulSoup(contents, "html.parser")
    soup.prettify()
    file.close()
    h1_total = soup.findAll('h1')
    h2 = soup.find('h2').text
    h3 = soup.find('h3').text
    h4 = soup.find('h4').text
    h5 = soup.find('h5').text
    p = soup.find('p').text
    div = soup.find('div').text
    b = soup.find('b').text
    i = soup.find('i').text
    td = soup.find('td').text
    span = soup.find('span').text

    if os.path.exists('example.properties'):
        f = open('example.properties', 'w+')
    else:
        f = open('example.properties', 'a+')

    count = len(h1_total)
    f.write("h1 = ")
    for j in range(0, count):
        f.write("%s " % h1_total[j].text)

    f.write("\nh2 = %s\n" % h2)
    f.write("h3 = %s\n" % h3)
    f.write("h4 = %s\n" % h4)
    f.write("span = %s\n" % span)
    f.write("h5 = %s\n" % h5)
    f.write("p = %s\n" % p)
    f.write("div = %s\n" % div)
    f.write("b = %s\n" % b)
    f.write("i = %s\n" % i)
    f.write("td = %s\n" % td)
    f.close()


def language(la):
    if la == "hindi":
        abbr = "hi"
    flag = open('example.properties')
    t = flag.read()
    length = t.count('=')
    flag.close()
    file = open('example.properties')
    if os.path.exists('example.hindi'):
        f = open('example.hindi', 'w+')
    else:
        f = open('example.hindi', 'a+')
    for e in range(0, length):
        z = file.readline()
        l = z.split(" ")
        for j in range(0, len(l[:2])):
            f.write("%s " % l[j])
        k = l[2:]
        for i in range(0, len(l[2:])):
            try:
                f.write(dictionary.translate("%s", '%s') % (k[i], abbr))
            except:
                f.write("%s" % k[i])
    file.close()


def display(la):
    x = open('example.%s' % la)
    y = x.read()
    z = y.count("=")
    x.close()
    a = open('example.hindi')
    if os.path.exists('temp.html'):
        f = open('temp.html', 'w+')
    else:
        f = open('temp.html', 'a+')
    for i in range(0, z):
        b = a.readline()
        f.write(b)
    f.close()
    webbrowser.open("temp.html")


def main():
    parser = argparse.ArgumentParser(description="A Command Line Tool")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-ext", "--extract", help="Performs \
        text-extraction", action="store_true")
    group.add_argument("-lan", "--language", help="Performs \
        transaltion", action="store_true")
    group.add_argument("-dis", "--display", help="Performs \
        display", action="store_true")

    group1 = parser.add_mutually_exclusive_group()
    group1.add_argument("-file", "--file", help="filename \
        to extract", action="store_true")
    group1.add_argument("-lang", "--lang", help="language \
        to translate", action="store_true")

    parser.add_argument("value", help="argument value")

    args = parser.parse_args()

    if args.extract:
        extract(args.value)
    elif args.language:
        language(args.value)
    elif args.display:
        display(args.value)


if __name__ == '__main__':
    main()
