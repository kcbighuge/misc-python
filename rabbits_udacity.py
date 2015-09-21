def rabbits(n):
    now = 0
    nex = 1
    died = []
    for i in range(n):
        now, nex = nex, now + nex
        if i > 4:
            now -= died[i-5]
            nex -= died[i-5]
        died.append(now)
    return now
