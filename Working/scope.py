import math


def get_sphereVolume(radius):
    volume = 4 / 3 * math.pi * radius ** 3
    return volume


def main():
    user_radius = float(input("Enter the radius:"))
    vol = get_sphereVolume(user_radius)

    print("The volume of a sphere with radius", user_radius, "is", vol)


main()