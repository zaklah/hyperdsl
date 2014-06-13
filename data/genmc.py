#! python

import numpy
import random
import argparse

def main():
  parser = argparse.ArgumentParser(description="Generate matrix for matrix completion problem.")
  parser.add_argument("n", type=int, help="size of matrix")
  parser.add_argument("p", type=int, help="rank")
  parser.add_argument("nnz", type=int, help="number of nonzero entries")
  args = parser.parse_args()

  l = numpy.random.randn(args.n, args.p)
  r = numpy.random.randn(args.p, args.n)
  x = numpy.dot(l, r)

  omg = random.sample([(i, j) for i in xrange(args.n) for j in xrange(args.n) if i <= j], args.nnz)

  for (i,j) in omg:
    print "%d %d %f" % (i, j, x[i,j])
    if(i != j):
      print "%d %d %f" % (j, i, x[i,j])


if __name__ == "__main__":
  main()