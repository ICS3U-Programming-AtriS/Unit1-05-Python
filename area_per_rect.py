#!/usr/bin/env python3
# Created By: Atri Sarker
# Date: Feb 18, 2025
# Calculates the Perimeter and Area of a rectangle with set dimensions


def main():
    length = 11
    width = 22
    print("\033[1m")  # BOLDS THE OUTPUT
    print("If a rectangle has the dimensions:")
    print(f"{length}cm x {width}cm")
    print("")
    print(f"The Area is {length*width}cm\u00b2")
    print(f"The Perimeter is {2*(length+width)}cm")


if __name__ == "__main__":
    main()
