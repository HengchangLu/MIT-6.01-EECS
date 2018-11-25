import lib601.sf as sf
import lib601.poly as poly
import lib601.sig as sig
import lib601.ts as ts

s1 = sf.SystemFunction(poly.Polynomial([1]), poly.Polynomial([1, -5.0/6, -1]))
print 's1.differenceEquation', s1.differenceEquation()
print 's1.dominantPole():', s1.dominantPole()

# -1.5
# stable no
# oscillatory  yes

s2 = sf.SystemFunction(poly.Polynomial([1]), poly.Polynomial([1, 5.0/4, 3.0/8]))
print 's2.differenceEquation', s2.differenceEquation()
print 's2.dominantPole():', s2.dominantPole()
# -2.0
# stable no
# oscillatory  yes

s3 = sf.SystemFunction(poly.Polynomial([1]), poly.Polynomial([1, 3.0/2, 9.0/8]))
print 's3.differenceEquation', s3.differenceEquation()
print 's3.dominantPole():', s3.dominantPole()

# (-0.666666666667+0.666666666667j)
# stable yes
# oscillatory  no

s4 = sf.SystemFunction(poly.Polynomial([1]), poly.Polynomial([1, 1, 1.0/2]))
print 's4.differenceEquation', s4.differenceEquation()
print 's4.dominantPole():', s4.dominantPole()

# (-1+1j)
# stable no
# oscillatory  yes

s5 = sf.SystemFunction(poly.Polynomial([1]), poly.Polynomial([1, -13.0/8, 42.0/64]))
# 3/
s6 = sf.SystemFunction(poly.Polynomial([1]), poly.Polynomial([1, 13.0/8, 42.0/64]))
# 1/
s7 = sf.SystemFunction(poly.Polynomial([1]), poly.Polynomial([1, 16.0/8, 63.0/64]))
# 1/
s8 = sf.SystemFunction(poly.Polynomial([1]), poly.Polynomial([1, -2.0/8, -63.0/64]))


def plotOutput(s):
    """Plot the output of the given SF, with a unit-step signal as input"""
    smModel = s.differenceEquation().stateMachine()
    outSig = ts.TransducedSignal(sig.UnitSampleSignal(), smModel)
    outSig.plot()


plotOutput(s3)
