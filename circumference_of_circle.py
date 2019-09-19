#!/usr/bin/env python3

# Created by: Patrick Gemmell
# Created on: September 12 2019
# This calculates the circumference of a circle

import constants


def main():
    # this function calculates circumference

    radius = int(input("Enter the radius of the circle (mm): "))

    circumference = constants.TAU*radius

    print("")
    print("Circumference is {}mm^2".format(circumference))


if __name__ == "__main__":
    main()
