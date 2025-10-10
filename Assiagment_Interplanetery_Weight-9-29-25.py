#Declaration of Name constants

nMERCURY = 0.38
nVENUS = 0.91
nMOON = 0.165
nMARS = 0.38
nJUPITAR = 2.34
nSATURN = 0.93
nURANUS = 0.92
nNEPTUNE = 1.12
nPLUTO = 0.066

#input name from user
sName = input('What is your name: ')

#input Earth weight from user
nEarth_Weight = float (input('What is your Earth weight: ')) 

#calculation of all planet's weight

nMercury = nEarth_Weight * nMERCURY
nVenus = nEarth_Weight * nVENUS
nMoon = nEarth_Weight * nMOON
nMars = nEarth_Weight * nMARS
nJupitar = nEarth_Weight * nJUPITAR
nSaturn = nEarth_Weight * nSATURN
nUranus = nEarth_Weight * nURANUS
nNeptune = nEarth_Weight * nNEPTUNE
nPluto = nEarth_Weight * nPLUTO

#output of all the results


print (f'{sName:<} here are your weights on all the planets of our solar system :')

print(f'{'The weight in Mercury is':35} {nMercury:>10,.2f}')
print(f'{'The weight in Venus is':35} {nVenus:>10,.2f}')
print(f'{'The weight in Moon is':35} {nMoon:>10,.2f}')
print(f'{'The weight in Mars is':35} {nMars:>10,.2f}')
print(f'{'The weight in Jupitar is':35} {nJupitar:>10,.2f}')
print(f'{'The weight in Saturn is':35} {nSaturn:>10,.2f}')
print(f'{'The weight in Uranus is':35} {nUranus:>10,.2f}')
print(f'{'The weight in Neptune is':35} {nNeptune:>10,.2f}')
print(f'{'The weight in Pluto is':35} {nPluto:>10,.2f}')
