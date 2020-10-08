import argparse
parser=argparse.ArgumentParser()
#parser.add_argument("echo", help="echo the string you use here")
#parser.add_argument("square", help="display a square of a given number", type=int)
parser.add_argument("x", help="the base", type=int)
parser.add_argument("y", help="the exponent", type=int)
#parser.add_argument("-v", "--verbosity",help="increase output verbosity",type=int, choices=[0,1,2])
parser.add_argument("-v", "--verbosity",help="increase output verbosity", action="count",default=0)
args=parser.parse_args()

#answer=args.square**2
answer=args.x**args.y

if args.verbosity>=2:
    print(" Running'{}'".format(__file__))
if args.verbosity>=2:
    print(" {} to the power {} equals {}".format(args.x, args.y, answer))
elif args.verbosity>=1:
    print("{}^{} =={}".format(args.x, args.y, answer))
else: 
    print(answer)

