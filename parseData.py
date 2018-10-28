# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 11:37:51 2018

@author: Acer
"""
AtomDict = {'H': 1, 'He': 2, 'Li': 3};
OrbitalDict = {'S': 0, 'SP' : 1, 'P': 2};

def parseData(inputFile, form="STO-3G"):
    if form == "STO-3G":
        return genBasisSTO3G(parseBasisSTO3G(inputFile));

def parseBasisSTO3G(inputFile):
    """
    This took a text file in nwchem format and parse it to extract the relevant parameters from
    the file.
   
    "The output of the parsing looks like this"
    parseBasis(f) -> [[(1,1,0,[(a,b), (c,d), (e,f)])]]
    The reason this is made so complicated is to facilitate the parsing of data where
    1. Multiple atom species basis functions are present -> in the outer list
    2. A single atom species have multiple basis functions -> in the inner list
    The first number in the inner most tuple corresponds to the atomic number. E.g. H -> 1, He -> 2
    The second number corresponds to the index of orbital, starting from 1
    The third number corresponds to the orbital label E.g. S -> 0, SP -> 1, P -> 2
    The third list corresponds to the three (zeta, coeff) pairs for the gaussians we used to represent a slater
    -type orbital
    
    In order not to complicate the parsed data, do not include unnecessary atoms
    """   
    with open(inputFile, 'r') as rawFile:
        lines = rawFile.readlines();
        lineIndex = 0;
        outputData = [];         
        while(lineIndex < len(lines)):
            line = lines[lineIndex];
            """
            Test if the first marker of BASIS SET is reached
            """
            if "#BASIS SET" in line:
                """
                Get the data for atom (nuclear charge) and orbital
                Specifiation for atom and orbital was on the immediate next line
                after #BASIS SET
                """
                lineIndex = lineIndex + 1;
                """
                Test if the next basis set marker or eof is reached
                """
                atomBasisData = [];
                while ("#BASIS SET" not in lines[lineIndex]):
                    atomData = lines[lineIndex].split();
                    atom = atomData[0];
                    orbital = atomData[1];
                    """
                    Get the coefficient and zeta of the orbitals
                    """
                    param = [];
                    for i in range(3):
                        #increment lineNumber by 1 to move on to the zeta, coeff data region
                        lineIndex = lineIndex + 1;
                        zetaLine = lines[lineIndex].split();
                        zeta, coeff = zetaLine[0], zetaLine[1];
                        param.append((float(zeta), float(coeff)));
                    atomBasisData.append((atom, orbital, param));
                    lineIndex = lineIndex + 1;
                    if ('END' in lines[lineIndex]):
                        break;
                outputData.append(atomBasisData);
            else:
                lineIndex = lineIndex + 1;
    return outputData;
                 
def genBasisSTO3G(allData):
    basisDict = {};
    for i in range(len(allData)):
        orbitalList = [];
        atomType = allData[i][0][0];
        charge = AtomDict[atomType];
        for j in range(len(allData[i])):
            orbitalType = allData[i][j][1];
            orbitalData = allData[i][j][2];
            orbitalList.append((orbitalType, orbitalData));
        basisDict[atomType] = (charge, orbitalList);
    return basisDict;
                
def genBasis(allData, form='STO-3G'):
    if form == 'STO-3G':
        return genBasisSTO3G(allData);