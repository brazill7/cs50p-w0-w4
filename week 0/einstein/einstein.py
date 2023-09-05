def emcsq(mass: int):
    spdl = pow(300000000, 2)
    energy = mass * spdl
    return energy

massInp = int(input("mass: "))

print(emcsq(massInp))