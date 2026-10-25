def towerOfHanoi(n, source, destination, auxiliary):
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return

    towerOfHanoi(n-1, source, auxiliary, destination)
    print("Move disk", n, "from", source, "to", destination)
    towerOfHanoi(n-1, auxiliary, destination, source)

n = 3
towerOfHanoi(n, 'A', 'C', 'B')
