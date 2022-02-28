# Project 2 - Moonlander
#
# Name: Geoff Blaylock
# Section: CPE 101-09
# Date: April 17, 2021

from landerFuncs import *


def main():
    showWelcome()
    alt = getAltitude()
    fuel = getFuel()
    vel = 0
    grav = 1.62
    time = 0
    rate = 0

    while alt > 0:
        if time == 0:
            print("LM state at retrorocket cutoff")
        if fuel > 0:
            displayLMState(time, alt, vel, fuel, rate)
            rate = getFuelRate(fuel)
            fuel = updateFuel(fuel, rate)
        else:
            rate = 0
            print("OUT OF FUEL - Elapsed Time:", time, "Altitude:", round(alt, 2), "Velocity:", round(vel, 2))
        acc = updateAcceleration(grav, rate)
        alt = updateAltitude(alt, vel, acc)
        vel = updateVelocity(vel, acc)
        time = time + 1

    print("\nLM state at landing/impact")
    displayLMState(time, alt, vel, fuel, rate)
    displayLMLandingStatus(vel)