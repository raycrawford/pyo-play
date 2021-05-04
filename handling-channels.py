from pyo import *

# Creates a Server with 8 channels
s = Server(nchnls=8).boot()
s.setOutputDevice(4)
amps = [0.05, 0.3, 0.5, 0.2, 0.05, 0.3, 0.35, 0.4]

# Generates 8 sine waves with
# increasing amplitudes
a = Sine(freq=500, mul=amps)

# Sets the output channels ordering
a.out(chnl=[3, 4, 2, 5, 1, 6, 0, 7])
a[7].out(chnl=7)
s.gui(locals())