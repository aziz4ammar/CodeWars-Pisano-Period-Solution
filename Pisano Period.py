def pisano(n):
    previous, current = 0, 1
    period = 0

    for i in range(n * n):
        previous, current = current, (previous + current) % n
        if previous == 0 and current == 1:
            period = i + 1
            break

    return period