import perceval as pcvl
import perceval.components as comp
import numpy as np

def get_CCZ():
    T = pcvl.PS(np.pi/4)
    Tdag = pcvl.PS(-np.pi/4)
    H = pcvl.BS.H()
    cnot = pcvl.catalog["heralded cnot"].build_processor()
    p = pcvl.Processor("SLOS",6)
    p.add([4,5],H)
    p.add([2,3,4,5],cnot)
    p.add([5],Tdag)
    p.add([0,1,4,5],cnot)
    p.add([5],T)
    p.add([2,3,4,5],cnot)
    p.add([5],Tdag)
    p.add([0,1,4,5],cnot)
    p.add([5],T)
    p.add([3],T)
    p.add([4,5],H)
    p.add([0,1,2,3],cnot)
    p.add([1],T)
    p.add([3],Tdag)
    p.add([0,1,2,3],cnot)
    return p