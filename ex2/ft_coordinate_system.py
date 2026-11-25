#!/usr/bin/env python3

import math


def get_player_pos() -> tuple[float, float, float]:
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates\n")
    enter_coord = "Enter new coordinates as floats in format 'x,y,z': "

    while True:
        coordinates = input(enter_coord).split(",")
        if len(coordinates) != 3:
            print("Invalid syntax")
        else:
            try:
                x = float(coordinates[0].strip())
                y = float(coordinates[1].strip())
                z = float(coordinates[2].strip())
            except ValueError as e:
                for coordinate in coordinates:
                    try:
                        float(coordinate.strip())
                    except ValueError:
                        print(f"Error in value '{coordinate.strip()}': {e}")
                        break
                continue

            return (x, y, z)


print(get_player_pos())
