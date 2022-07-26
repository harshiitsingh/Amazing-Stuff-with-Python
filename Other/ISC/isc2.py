import math
from scipy import constants

print("1. To calculate the FREE SPACE PATH LOSS, FSPL ")
r = eval(input("\nEnter the value of distance: "))
f = eval(input("Enter the value of frequency: "))
value = 32.4 + 20 * math.log(r) + 20 * math.log(f)
print(f"The value of FSPL is {value} dB\n\n")

print("2. To calculate the NOISE DENISTY, N0")
Ts = eval(input("\nEnter the value of System Noise Temperature for ground station receiver, Ts : "))
value = -228.6 + 10 * math.log(Ts)
print(f"The value of Noise Density is {value} dB\n\n")

print("3. To calculate RECEIVER ANTENNA GAIN (Ground Station), Gr")
n = eval(input("Enter the value of Efficiency : "))
D = eval(input("Enter the Diameter of Ground station Antenna : "))
Gr = n * math.pow(10.472 * f * D, 2)
print(f"The value of Gr is {Gr} dB\n\n")

print("4. To calculate the GAIN TO NOISE TEMPERATURE, G/T")
G_T = Gr - Ts
print(f"The value of G/T is {G_T} dB/K\n\n")

print("5. To calculate EFFECTIVE ISOTROPIC RADIATED POWER, EIRP")
GT = eval(input("Enter the value of Gain of the transmitting antenna, GT : "))
PT = eval(input("Enter the Transmitted Power, PT : "))
EIRP = GT + PT
print(f"The value of EIRP is {EIRP} dB\n\n") # UNIT?

print("6. To calculate RECEIVED POWER TO NOISE RATIO, PR/N0")
losses = eval(input("Enter the value of losses :"))

P_N = EIRP + G_T - losses - constants.Boltzmann # OR CONSTATNTS.k
print(f"The value of PR/N0 is {P_N} dB\n\n") # CHECK UNITS?

print("7. To calculate ENERGY TO NOISE RATIO, Eb/N0")

'''
neta= efficiency
D = GS Antenna diameter
5) EIRP = GT + PT (BOTH ARE PROVIDED BY USER)
6) Received Power to noise ratio = Effective isotropic radiated power + G/T - LOSSES(BY USER) - K (BOLTZMANN CONT)
7) = .... - BIT RATE(BY USER)
8) 
9) REQUIRED (BY USER)'''