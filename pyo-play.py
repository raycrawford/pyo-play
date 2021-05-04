from pyo import *
s = Server().boot()
s.start()

# miccheck = Input().play().out() 
miccheck = Input()
d = SDelay(miccheck, delay=1).out()

#a = Sine(mul=0.5).out()
s.gui(locals())
