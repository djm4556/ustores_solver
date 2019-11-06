"""
UStores Solver: A semi-automatic solver for the
Keep Talking and Nobody Explodes modded module
UltraStores (ktane.timwi.de/HTML/UltraStores.html)

:author: mythers45#1807 (Discord username)
"""
from sys import argv  # For interface customization?
from src.functions import b_36, mono, poly  # Helper imports


def main() -> None:
    """
    The main function, which solves the UltraStores module.
    :return: None
    """
    a = [0, 0, 0, 0, 0]  # Storage for A, B, C, D values
    b = [0, 0, 0, 0, 0]  # (a4 always = 0)
    c = [0, 0, 0, 0, 0, 0]
    d = 0
    stage_list = {0: a, 1: b, 2: c}  # Dict defining each stage's list

    ser = list(input("Enter the bomb's serial number: ").upper())
    while len(ser) != 6:  # Gets the serial number (SN), ensuring it's six characters long
        ser = list(input("Invalid serial number. Re-enter it:\n(six characters with no spaces): ").upper())
    for i in range(0, len(ser)):  # Iterates through the SN's characters, first validating...
        if not ser[i].isalnum():  # (All characters should be alphanumeric)
            print("DANGER: Non-alphanumeric character encountered at character " + str(i + 1))
            print("Such characters CANNOT appear in the serial number. Exiting...")
            exit(1)  # If a non-alphanumeric character appears, exit immediately
        elif ser[i].isdigit() and (i == 3 or i == 4):  # Chars 4 and 5 should be letters
            print("WARNING: Number encountered at character " + str(i + 1))
            print("Characters 4 and 5 should always (?) be letters.")
        elif ser[i].isalpha() and (i == 2 or i == 5):  # Chars 3 and 6 should be numbers
            print("WARNING: Letter encountered at character " + str(i + 1))
            print("Characters 3 and 6 should always (?) be numbers.")
        ser[i] = b_36.index(ser[i])  # Then translating the current SN character...
        d += ser[i]  # into base 36, while accumulating d with each one
    a[0] = (ser[2] * 36 + ser[3]) % 365  # Characters 3 and 4
    b[0] = (ser[4] * 36 + ser[5]) % 365  # Characters 5 and 6
    c[0] = (ser[0] * 36 + ser[1]) % 365  # Characters 1 and 2

    # Now the program has all required serial number data and can get rotations
    for STAGE in range(0, 3):  # For each of the 3 stages of the mod...
        for n in range(1, STAGE + 4):  # For each rotation...
            # Note on the +4: The first stage has 3 rotations, but that's STAGE = 0, so
            # 3 needs to be added, and the end of range is exclusive, so add 3+1, or 4.
            valid = False  # Stores validity of a given stage's input
            rots = []  # Variable to store list of sub-rotations
            while not valid:  # Prompt until valid
                rots = input("Enter rotation number " + str(n) + " of stage " + str(STAGE + 1)
                             + ":\n(separate sub-rotations with spaces): ").upper().split(" ")
                valid = validate_rots(rots)  # Gets a rotation and tests it for validity

            if len(rots) == 1:  # If there's only 1 rotation, use it to calculate the next value
                stage_list[STAGE][n] = mono[rots[0]][STAGE](stage_list[STAGE][n-1], d, n, a[n-1], b[n-1])
            elif len(rots) == 2:  # Otherwise, if there are 2 rotations, check the unused ones
                axes = ["X", "Y", "Z", "U", "V", "W"]  # List of axes
                func = ["X", "Y", "Z"]  # List of axes with functions
                axes.remove(rots[0][0])  # (and axes for function X!)
                axes.remove(rots[0][1])  # Removes the used axes...
                axes.remove(rots[1][0])  # To find the two...
                axes.remove(rots[1][1])  # unused ones.
                index = 0  # Index of the function
                for part in axes:  # For each axis not in XYZ, increment the function index
                    if part not in func:  # (Resulting function: Z if 0 in, Y if 1 in, X if 2 in)
                        index += 1  # Then calculate the next value without a 3rd rotation...

                stage_list[STAGE][n] = poly[func[index]][STAGE](  # (it's unused in X, Y, and Z anyway)
                    rots[0], rots[1], None, stage_list[STAGE][n - 1], d, n, a[n - 1], b[n - 1])
            # End of double rotation calculation
            else:  # Otherwise, there must be 3 rotations, so check if they all have an axis from XYZ
                # If that's the case, they all must map XYZ to UVW or vice versa, as all six axes are used once
                func = ["X", "Y", "Z"]  # Stores the X, Y, and Z axes in a list for easy function use
                form = "W"  # Stores the formula to use, chosen by a test of each sub-rotation
                for part in rots:  # For each sub-rotation, if neither of the axes is XYZ...
                    if part[0] not in func and part[1] not in func:  # The test fails...
                        form = "V"  # So use function V instead of W in calculating
                        break  # Maybe the world's smallest optimization effort
                stage_list[STAGE][n] = poly[form][STAGE](  # Uses the result formula of the test
                    rots[0], rots[1], rots[2], stage_list[STAGE][n - 1], d, n, a[n - 1], b[n - 1])
            # End of triple (and all) rotation calculation
        # End of rotation (n) loop
        ans = stage_list[STAGE][STAGE + 3]  # The answer! (+3 similar to +4 in rotation loop)
        print("Stage " + str(STAGE + 1) + "'s answer is " + str(ans) + "! Now to input it.")
        print("Press the center button to enter input mode.")
    # End of stage loop


def validate_rots(rots: list) -> bool:
    """
    Takes a list of sub-rotations comprising one rotation and tests its validity.
    For a rotation to be valid, it must have 1, 2, or 3 sub-rotations, all defined
    in the dictionary of single rotations, without using any axis more than once.
    :param rots: The rotation (a.k.a. list of sub-rotations) to validate
    :return: The validity of the rotation by the above tests
    """
    valid = True  # Assume valid until tested
    axes = []  # List for storing used axes (which should be unique)
    if not 1 <= len(rots) <= 3:  # If the rotation has 0 or 4+ sub-rotations...
        print("Invalid number of sub-rotations (should be 1, 2, or 3)")
        return False  # It's invalid, and skip other tests.
    for part in rots:  # Next, iterate through the sub-rotations...
        if part not in mono:  # If one's not in the dictionary, it's invalid...
            print("Invalid sub-rotation " + part + " (should have 2 of X Y Z W V U)")
            valid = False  # But keep checking other sub-rotations for validity.
        else:  # Otherwise, check for duplicate axes.
            if part[0] in axes:  # If the first axis is already used...
                print("Axis " + part[0] + " used multiple times (axes should be unique)")
                valid = False  # The rotation is invalid.
            if part[1] in axes:  # The same goes for the second axis,
                print("Axis " + part[1] + " used multiple times (axes should be unique)")
                valid = False  # After checking if the axes were used before...
            axes.extend(list(part))  # Add them to the list so they're marked as used next time.
    return valid  # Finally, return the validity (False if any tests failed, else True).


if __name__ == '__main__':
    main()
