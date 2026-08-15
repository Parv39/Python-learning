# Take the size of the square from the user
n = int(input("Enter size: "))

# Outer loop -> controls the rows
for i in range(1, n + 1):

    # Inner loop -> controls the columns
    for j in range(1, n + 1):

        # Check if the current position is on the border
        # First row    -> i == 1
        # Last row     -> i == n
        # First column -> j == 1
        # Last column  -> j == n
        if i == 1 or i == n or j == 1 or j == n:

            # Print a star without moving to the next line
            print("*", end=" ")

        else:
            # Print a blank space for the middle positions
            print(" ", end=" ")

    # After one complete row is printed,
    # move the cursor to the next line
    print()

'''
      j=1  j=2  j=3

i=1    *    *    *    ← First row → print all stars

i=2    *         *    ← Middle row
        ↑         ↑
    First col  Last col → print stars
    Middle column → leave empty

i=3    *    *    *    ← Last row → print all stars

# end=" " keeps printing on the same line
# so all columns of one row are printed together.

# print() moves to the next line
# after one complete row is printed.
'''