def hash_counter(i, j, world):
    cnt = 0

    for k in range(i-1,i+2):

        for l in range(j-1, j+2):
            if not (k == i and l == j):
                row = world[k]

                if row[l] == "#":

                    cnt += 1
    return cnt-1
def move(world, n, m):
    for i in range(1,n-2):
        for j in range(1,m-2):
            count = hash_counter(i,j,world)
            row = world[i]
            if row[j] == "#":
                if count>3:
                    new_row = row[:j - 1] + " " + row[j + 1:]

                    world = world[:i-1] + tuple(new_row) + world[i+1:]
                elif count<2:

                    new_row = row[:j-1] +" "+row[j+1:]

                    world = world[:i-1] + tuple(new_row) + world[i+1:]
            else:
                if count == 3:
                    new_row = row[:j - 1] + "#" + row[j + 1:]
                    world = world[:i-1] + tuple(new_row) + world[i+1:]



def evolve(world, steps):
    n = len(world)
    m = len(world[1])-2
    for r in range(steps):
        move(world, n, m)

    return world


field = (
    "--------------",
    "|            |",
    "|   ###      |",
    "|   #        |",
    "|    #       |",
    "|            |",
    "--------------"
)
steps = 4
print(evolve(field,1))
#result, alive_cells = evolve(field, steps)

#print(f"Game of Life after {steps} moves:")
#for row in result:
    #print(row)
#print(f"{alive_cells} are alive.")

"""The provided game world is valid if:

    ... it is a tuple of strings
    ... it only contains the defined characters ("-", "|", "#", " ") and only at the right positions as described above.
    ... each line has the same length.
    ... it has a sensible size (both dimensions of the world including the frame are greater than 2 - otherwise there would be no game cells).
    The provided number of evolutionary steps is a positive integer."""
