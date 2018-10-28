# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 14:44:02 2018

@author: Acer
"""
from parseData import parseData;

class Atom:
    def __init__(self, basis, pos):
        (self.charge, self.orbital) = basis;     
        self.pos = pos;
    
    def getOrbital(self, index=0):
        return self.orbital[index][1];
    
    def getOrbitalType(self, index=0):
        return self.orbitalType[index][0];
    
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
    
def buildAtomListSTO3G(basisFile, allData):
    """
    allData will be in the form of a list, where each element is given as
    a tuple (AtomType, AtomCoord)
    E.g. ('H', (0,0,1))
    """
    atomList = [];
    allBasis = parseData(basisFile, "STO-3G");
    for i in range(len(allData)):
        (AtomType, AtomPos) = allData[i];
        basis = allBasis[AtomType];
        atom = Atom(basis, AtomPos);
        atomList.append(atom);
    return atomList;
            
        