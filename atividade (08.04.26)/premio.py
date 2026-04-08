def premio(p, d, b):
    total = p + (d * 2) + (b * 3)
    
    if total >= 150:
        return 'B'
    elif total >= 120:
        return 'D'
    elif total >= 100:
        return 'P'
    else:
        return 'N'


p = int(input())
d = int(input())
b = int(input())

print(premio(p, d, b))