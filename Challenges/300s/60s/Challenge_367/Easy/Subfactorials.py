def derangement(n):
    if n == 0:
        return 1
    elif n == 1:
        return 0

    return (n-1) * (derangement(n-1) + derangement(n - 2))

print(f'!6  -> {derangement(6)}')
print(f'!9  -> {derangement(9)}')
print(f'!14 -> {derangement(14)}')
