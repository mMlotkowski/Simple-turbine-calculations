# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 12:49:47 2023

@author: mMlotkowski
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 21:22:25 2023

@author: mMlotkowski
"""

import math


#DANE WEJŚCIOWE
PI = 1/3
strm = 40
p01 = 35*10**5
T01 = 1300
kp = 1.33
cp = 1280
R = 320
mi = 1.45e-6

#ZAŁOŻENIA PROJEKTOWE
et = 0.9
psi = 1.3
alf1 = 3*0.0174532925
Mwl = 0.4
alf3 = 5*0.0174532925

#OBLICZENIA WSTĘPNE
T03s = (PI**((kp-1)/kp))*T01
T03 = et*(T03s-T01)+T01
l2_3 = cp*(T03-T01)
u = (abs(l2_3)/psi)**(1/2)

p1 = (p01/(1+((kp-1)/2)*Mwl**2)**(kp/(kp-1)))
T1 = T01/(1+((kp-1)/2)*Mwl**2)
ro1 = p1/(R*T1)

#KINEMATYKA
c1 = Mwl*(kp*R*T1)**(1/2)
c1u = c1*math.sin(alf1)
c1m = c1*math.cos(alf1)
c3m = c1m
c3 = c3m/(math.cos(alf3))
c3u = c3*math.sin(alf3)*(-1)
w3m = c1m
w3u = c3u-u
w3 = (((w3u)**2)+((c1m)**2))**(1/2)

"etta2 = math.asin(w3u/w3m)" #cos nie działa

T3 = T03-((c3**2)/(2*cp))
M3 = (((T03/T3)-1)*(2/(kp-1)))**(1/2)
Mw3 = w3/(kp*R*T3)**(1/2)
p3 = ((p01/PI)/(1+((kp-1)/2)*(M3**2))**(kp/(kp-1)))

c2u = c3u-(l2_3/u)
c2m = c3m
c2 = ((c2u**2)+(c2m**2))**(1/2)
##alf2 = math.atan(c2m/c2u)
T02 = T01
T2 = T02-((c2**2)/(2*cp))
M2 = c2/(kp*R*T2)**(1/2)
p02 = p01
p2 = (p02/(1+((kp-1)/2)*M2**2)**(kp/(kp-1)))
ro02 = p02/(R*T02)
ro2 = ro02*(1+((kp-1)/2)*M2**2)**(-1/(kp-1))
ro01 = p01/(R*T01)

HT=0.6
rt1=(strm/(3.14*c1m*ro1*(1-(HT**2))))
rh1 = HT*rt1
R_mean = (rt1+rh1)/2
