import cowsay
import sys
if len(sys.argv)==2:#we can not usd sys and arg and there is no command arguement in jupyter notebook
    cowsay.trex("Hello I am " + sys.argv[1])