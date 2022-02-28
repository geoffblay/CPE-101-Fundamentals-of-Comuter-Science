# Project 2 - Moonlander
#
# Name: Geoff Blaylock
# Section: CPE 101-09
# Date: April 17, 2021

from landerFuncs import *


def main():
    vel = 0.00
    time = 0
    rate = 0.00
    touchdown = False

    showWelcome()
    alt = getAltitude()
    fuel = getFuel()
    print("LM state at retrorocket cutoff")

    while not touchdown:
        # starts a while loop that will continue to run as long as the lander has not reached the ground
        if fuel > 0:
            # as long as the lander has fuel in it, the program will display the lander's state and ask for a new fuel
            # rate. When the fuel runs out, the program will set the rate to 0 and display the out of fuel message.
            displayLMState(time, alt, vel, fuel, rate)
            rate = getFuelRate(fuel)
            fuel = updateFuel(fuel, rate)
        else:
            rate = 0
            print("OUT OF FUEL - Elapsed Time:", time, "Altitude:", round(alt, 2), "Velocity:", round(vel, 2))

        acc = updateAcceleration(1.62, rate)
        alt = updateAltitude(alt, vel, acc)
        vel = updateVelocity(vel, acc)

        if alt > 0:
            # checks after every run of the while loop to see if the lander has touched down yet.
            touchdown = False
        else:
            touchdown = True

        time = time + 1

    print("\nLM state at landing/impact")
    displayLMState(time, alt, vel, fuel, rate)
    displayLMLandingStatus(vel)


if __name__ == '__main__':
    main()
