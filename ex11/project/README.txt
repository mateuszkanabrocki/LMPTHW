How to run this:

example:
history | ./tail.py -10 | ./sed.py "s/^[ 0-9]*//g" - | ./cut.py -d ' ' -f 1 - | ./sort.py - | ./uniq.py
