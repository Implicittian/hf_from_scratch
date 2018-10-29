# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 14:44:02 2018

@author: Acer
"""
from parseData import parseData;
from integral import orbitalIntegral;
import numpy as np;
"""
Class Atom Data Structure:
    charge = nuclear charge
    orbital is a list of tuples in the form of 
    [('S', [(zeta1, coeff1), (zeta2, coeff2), ...])]
    from which we see that the first 
"""
class Atom:
    def __init__(self, basis, pos):
        (self.charge, self.orbitals) = basis;     
        self.pos = pos;
        self._normOrbital();
    
    def getOrbital(self, index=0):
        return self.orbitals[index][1];
    
    def getOrbitalType(self, index=0):
        return self.orbitals[index][0];
    
    def getAllZeta(self, index=0):
        orbital = self.getOrbital(index);
        zeta, _ = zip(*orbital);
        return list(zeta);
    
    def getAllCoeff(self, index=0):
        orbital = self.getOrbital(index)
        _, coeff = zip(*orbital);
        return list(coeff);
    
    def getZeta(self, orbitalIndex, coeffIndex=0):
        allZeta = self.getAllZeta(orbitalIndex);
        return allZeta[coeffIndex];
    
    def getCoeff(self, orbitalIndex, coeffIndex=0):
        allCoeff = self.getAllCoeff(orbitalIndex);
        return allCoeff[coeffIndex];
    
    def getCharge(self, index):
        return self.charge;
    
    def getX(self):
        return self.pos[0];
    
    def getY(self):
        return self.pos[1];
    
    def getZ(self):
        return self.pos[2];
    
    def getPos(self):
        return self.pos;
    
    def setX(self, newX):
        self.pos[0] = newX;
        
    def setY(self, newY):
        self.pos[1] = newY;
        
    def setZ(self, newZ):
        self.pos[2] = newZ;
        
    def setPos(self, pos):
        (x, y, z) = pos;
        self.setX(x);
        self.setY(y);
        self.setZ(z);
    
    def _getOrbitalModulus(self):
        allOrbitalModulus = [];
        for orbitalIndex in range(len(self.orbitals)):
            orbital = self.getOrbital(orbitalIndex);
            orbitalModulus = 0;
            for i in range(len(orbital)):
                for j in range(len(orbital)):
                    orbitalModulus = orbitalModulus + \
                                     orbitalIntegral(orbital[i], orbital[j], self.pos, self.pos);
            allOrbitalModulus.append(np.sqrt(orbitalModulus));
        return allOrbitalModulus;
    
    def _normOrbital(self):
        allOrbitalModulus = self._getOrbitalModulus();
        for orbitalIndex in range(len(self.orbitals)):
            orbitalModulus = allOrbitalModulus[orbitalIndex];
            orbital = self.getOrbital(orbitalIndex);
            for coeffIndex in range(len(orbital)):
                (zeta, coeff) = orbital[coeffIndex];
                orbital[coeffIndex] = (zeta, coeff/orbitalModulus);
                
    def printAtom(self):
        print("The charge is " + str(self.charge) + "\n");
        print("There are " + str(len(self.orbitals)) + " orbitals \n");
        for i in range(len(self.orbitals)):
            orbital = self.getOrbital(i);
            print("The type of orbital is " + self.getOrbitalType(i));
            print("It has " + str(len(orbital)) + " contracted component Gaussians");
            for (zeta, coeff) in orbital:
                print("The zeta of component orbital is " + str(zeta));
                print("The coefficient of component orbital is " + str(coeff));
    
def buildAtomListSTO3G(basisFile, allData):
    """
    allData will be in the form of a list, where each element is given as
    a tuple (AtomType, AtomCoord)
    E.g. ('H',0,0,1)
    """
    atomList = [];
    allBasis = parseData(basisFile, "STO-3G");
    for i in range(len(allData)):
        (AtomType, posX, posY, posZ) = allData[i];
        basis = allBasis[AtomType];
        atom = Atom(basis, (posX, posY, posZ));
        atomList.append(atom);
    return atomList;
            
        