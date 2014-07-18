#!/usr/bin/env python
from __future__ import print_function, division

import numpy
import numpy.random
import argparse

def main():
  parser = argparse.ArgumentParser(description="Generate random data for DC1 app.")
  parser.add_argument("n", type=int, help="dimension of variables")
  parser.add_argument("m", type=int, help="rank of underlying matrix")
  parser.add_argument("d", type=float, help="density of matrix")

  args = parser.parse_args()

  # generate problem matrix by first generating a PSD matrix, then discarding some number of
  # the entries so that the matrix is sparse
  u = numpy.random.randn(args.n, args.m)

  l = numpy.random.rand(args.n, args.n)
  l = numpy.minimum(l, l.T)

  with open("a.dat", "w") as f:
    for i in range(args.n):
      for j in range(args.n):
        if (i < j):
          if(numpy.random.rand() <= args.d):
            uij = numpy.dot(u[i,:], u[j,:])
            print("%d %d %f" % (i+1, j+1, uij), file=f)
            print("%d %d %f" % (j+1, i+1, uij), file=f)
        elif (i == j):
          if(numpy.random.rand() <= args.d):
            uij = numpy.dot(u[i,:], u[j,:])
            print("%d %d %f" % (i+1, j+1, uij), file=f)

  y0 = numpy.random.randn(args.n)

  with open("y0.dat", "w") as f:
    for i in range(args.n):
      print("%f" % y0[i], file=f)

if __name__ == "__main__":
  main()
