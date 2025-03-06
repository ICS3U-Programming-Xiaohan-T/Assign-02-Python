#!/usr/bin/env python3
# Created by: Xiaohan Tian
# Created on: Mar 3, 2025
# This program is to calculate the surface area and volume of trapezoid prism

#import all the information from color.py
import color

def main():
    # print the following to say hi to users in yellow text
    print(
        (str(color.Colors.YELLOW))
        + "Hello, let me help you to find the volume and surface area of trapezoidal prism!"
    )
    print("")
    # blue font, according to the message to guide the user to enter the correct length of information.
    height = float(
        input(str(color.Colors.LIGHT_BLUE) + "Please enter the height (cm): ")
    )
    length = float(
        input(str(color.Colors.LIGHT_BLUE) + "Please enter the length (cm): ")
    )
    long_base = float(
        input(str(color.Colors.LIGHT_BLUE) + "Please enter the long base (cm): ")
    )
    short_base = float(
        input(str(color.Colors.LIGHT_BLUE) + "Please enter the short base (cm): ")
    )
    left_side_length = float(
        input(str(color.Colors.LIGHT_BLUE) + "Please enter the left side length (cm): ")
    )
    right_side_length = float(
        input(
            str(color.Colors.LIGHT_BLUE) + "Please enter the right side length (cm): "
        )
    )
    # the formula of volume and surface area, the result will be printed by light green
    volume = 0.5 * (short_base + long_base) * height * length
    surface_area = (
        (long_base + short_base) * height * 2 * 0.5
        + short_base * length
        + long_base * length
        + left_side_length * length
        + right_side_length * length
    )
    print("")
    print(
        (str(color.Colors.LIGHT_GREEN))
        + "Surface area is {} cm^2.".format(surface_area)
    )
    print((str(color.Colors.LIGHT_GREEN)) + "Volume is {} cm^3.".format(volume))
    # all results are saved to 2 decimal place
    float("{:.2f}".format(surface_area))
    float("{:.2f}".format(volume))


if __name__ == "__main__":
    main()
