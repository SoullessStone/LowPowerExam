def dynamic_power_dissipation(na, fclk, cTot, vdd):
    return na * fclk * cTot * pow(vdd, 2)
