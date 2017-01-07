#!/usr/bin/python 
import sys
import os


if len(sys.argv) != 2 :
    print sys.stderr, " Invalid args "  
    print sys.stderr, " %s fio_minimal.output " % (sys.argv[0])  
    exit(1)

print "Input Minimal File = ", sys.argv[1]

dirpath=os.path.dirname(sys.argv[0])
csv = open(sys.argv[1],'r').read().strip()
fn = open(dirpath + '/fio_minimal_header.csv','r').read().split(',')
index = 0
for h in enumerate(csv.split(';'), start=1):
    print("%d\t%s\t%s" % (index, fn[index], h[1]))
    index += 1
del fn
del csv
