import perceval as pcvl
import perceval.components as comp
import numpy as np

def get_CCZ():
    
    T1 = 1/(1+2**(1/3))
    R1 = np.sqrt(1-T1**2)
    T3 = T1**2
    R3 = np.sqrt(1-T3**2)
    p = pcvl.Processor("SLOS",6)
    #Upper Modes 0,2,4
    #p.add(4,pcvl.BS.H())
    p.add([0,1],pcvl.BS.Ry(pcvl.BS.r_to_theta(R1)))
    p.add([2,3],pcvl.BS.Ry(pcvl.BS.r_to_theta(R1)))
    p.add([4,5],pcvl.BS.Ry(pcvl.BS.r_to_theta(R1)))

    p.add([0,1],pcvl.BS.Ry(-pcvl.BS.r_to_theta(R3)))
    p.add([2,3],pcvl.BS.Ry(-pcvl.BS.r_to_theta(R3)))
    p.add([4,5],pcvl.BS.Ry(-pcvl.BS.r_to_theta(R3)))

    p.add([1,2],pcvl.BS.Ry(pcvl.BS.r_to_theta(R1)))
    p.add([3,4],pcvl.BS.Ry(pcvl.BS.r_to_theta(R1)))
    p.add([5],pcvl.PS(np.pi))
    p.add([0,5],pcvl.BS.Ry(pcvl.BS.r_to_theta(R1)))
    p.add([1,2,3,4,5],pcvl.PERM([4,0,1,2,3]))
    
    p.add([5],pcvl.PS(np.pi))

    p.set_postselection(pcvl.PostSelect("[0,1]==1 & [2,3]==1 & [4,5]==1"))
    return p