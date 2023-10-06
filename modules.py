# module = a file containing python code, May contain functions, classes, etc.
# Used with modular programming, which is to separate a program into parts

import messages
import messages as msg
import messages as m
from messages import hello, bye

messages.hello()
messages.bye()

msg.hello()
msg.bye()

m.hello()
m.bye()

hello()
bye()

# from messages import * (this one is dangerous)

help("modules")
