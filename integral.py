# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 13:43:02 2018

@author: Acer
"""

import numpy as np;

# =============================================================================
# def gaussProd(zetaTuple1, zetaTuple2, centre1, centre2):
#     """
#     This function takes four input
#     (zeta1, coeff1), centre1 specifies coeff1*exp(-zeta(x-centre1))
#     (zeta2, coeff2), centre2 specifies coeff2*exp(-zeta(x-centre2))
#     
#     This function returns
#     coeff1*coeff2*exp(-zeta1*zeta2/(zeta1+zeta2)*(centre2-centre1)^2)
#     *exp(-(zeta1+zeta2)*(x-Px))
#     Px = zeta1*centre1+zeta2*centre2/(zeta1+zeta2)
#     represented as (newZeta, newCoeff), newCentre 
#     """
#     (zeta1, coeff1) = zetaTuple1;
#     (zeta2, coeff2) = zetaTuple2;
#     newZeta = zeta1 + zeta2;
#     newCoeff = coeff1*coeff2*np.exp(-zeta1*zeta2/(zeta1+zeta2)*(centre1-centre2)**2);
#     newCentre = zeta1*centre1 + zeta2*centre2/ (zeta1 + zeta2);
#     return (newZeta, newCoeff), newCentre;
# =============================================================================
def orbitalIntegral(orbital1, orbital2, centre1, centre2):
    (zeta1, coeff1) = orbital1;
    (zeta2, coeff2) = orbital2;
    coordinate1 = np.array(centre1);
    coordinate2 = np.array(centre2);
    QDistSquared = (coordinate1 - coordinate2).dot((coordinate1 - coordinate2));
    q = zeta1*zeta2/(zeta1 + zeta2);
    p = zeta1 + zeta2;
    return coeff1*coeff2*np.exp(-q*QDistSquared)*(np.pi/p)**(3/2);
# =============================================================================
# 
# def overlapMatrix(orbitals1, orbitals2, centre1, centre2):
#     
# =============================================================================
