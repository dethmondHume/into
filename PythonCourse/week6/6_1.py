def count_holes(n):
    if not isinstance(n, int) and not isinstance(n, str) and not isinstance(n, long):
        return 'ERROR'
    keys = {0:1, 4:1, 6:1, 8:2, 9:1}
    n = abs(int(n))
    n = str(n)
    holes = 0
    for i in n:
        holes = holes + keys.get(int(i), 0)
    return holes

count_holes(-888888888888888888888) 
