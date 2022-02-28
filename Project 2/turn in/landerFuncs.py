# Project 2 - Moonlander
#
# Name: Geoff Blaylock
# Section: CPE 101-09
# Date: April 17, 2021

def showWelcome():
    # takes no input
    # outputs a printed welcome message to the user
    print("Welcome aboard the Lunar Module Flight Simulator\n\n\tTo begin you must specify the LM's initial "
          "altitude\n\tand fuel level.  To simulate the actual LM use\n\tvalues of 1300 meters and 500 liters, "
          "respectively.\n\n\tGood luck and may the force be with you!")


def getFuel():
    # takes no input
    # prompts user to enter initial fuel, correcting the user if they enter an invalid value, returns fuel
    # return value is of type float
    fuel = float(input("Enter the initial amount of fuel on board the LM "
                       "(in liters):"))
    while fuel <= 0:
        print("ERROR: Amount of fuel must be positive, please try again")
        fuel = input("Enter the initial amount of fuel on board the LM "
                     "(in liters):")
    return fuel


def getAltitude():
    # takes no input
    # prompts user to enter initial altitude, correcting the user if the enter an invalid value, returns altitude
    # return value is of type float
    altitude = float(input("Enter the initial altitude of the LM (in meters):"))
    while altitude < 1 or altitude > 9999:
        print("ERROR: Altitude must be between 1 and 9999, inclusive, please try again")
        altitude = input("Enter the initial altitude of the LM (in meters):")
    return altitude


def displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate):
    # inputs are of type double and int
    # prints the status of the LM's landing process
    print("Elapsed Time:", elapsedTime, "s")
    print("        Fuel:", fuelAmount, "l")
    print("        Rate:", fuelRate, "l/s")
    print("    Altitude:", round(altitude, 2), "m")
    print("    Velocity:", round(velocity, 2), "m/s")
    print("")


def getFuelRate(currentFuel):
    # input is of type int
    # prompts user for a value for the fuelrate, correcting the user if they enter an invalid value, returns lower
    # of the user input or the passed in parameter
    # output is of type int

    fuelrate = int(input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))
    while fuelrate < 0 or fuelrate > 9:
        print("ERROR: Fuel rate must be between 0 and 9 inclusive")
        fuelrate = int(input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))
    if fuelrate < currentFuel:
        return fuelrate
    else:
        return currentFuel


def updateAcceleration(gravity, fuelRate):
    # input is of type float and int
    # calculates current acceleration with the given formula
    # return value is of type double
    acceleration = gravity * ((fuelRate / 5) - 1)
    return acceleration


def updateAltitude(altitude, velocity, acceleration):
    # input is of type float
    # calculates current altitude, if the value is less than 0 it returns 0
    # return value is of type float
    newAlt = altitude + velocity + (acceleration / 2)
    if newAlt <= 0:
        return 0
    else:
        return newAlt


def updateVelocity(velocity, acceleration):
    # input is of type float
    # calculates current velocity
    # return value is of type float
    newVel = velocity + acceleration
    return newVel


def updateFuel(fuel, fuelRate):
    # input is of type int
    # calculates current remaining fuel
    # return value is of type int
    newFuel = fuel - fuelRate
    if newFuel < 0:
        return 0
    else:
        return newFuel


def displayLMLandingStatus(velocity):
    # input is of type float
    # prints a message based on the velocity of the LM at time of landing
    if -1 <= velocity <= 0:
        print("Status at landing - The eagle has landed!")
    elif -10 < velocity < -1:
        print("Status at landing - Enjoy your oxygen while it lasts!")
    elif velocity <= -10:
        print("Status at landing - Ouch - that hurt!")
