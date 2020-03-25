def super_fibonacci(n, m):
    super_list = []
    i = 0
    while len(super_list) < m:
        super_list.extend([1])
    for i in range(m, 35):
        x = 0
        k = i
        for j in range(0, m):
            x = x + super_list[k - 1]
            k = k - 1
        super_list.extend([x])
      
    return super_list[n - 1]

super_fibonacci(35, 17)
