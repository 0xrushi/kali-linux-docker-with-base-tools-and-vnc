#!/usr/bin/python
import sys
import os

m1 = os.environ["M1"]
print("Number of arguments:", len(sys.argv), "arguments.")
print("Argument List:", str(sys.argv), m1, os.listdir("/data/"))
