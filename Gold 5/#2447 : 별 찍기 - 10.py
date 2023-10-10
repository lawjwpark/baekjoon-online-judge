def star(n):
    if n == 1:
        return ["*"]
    
    mother = []
    daughter = star(n // 3)
    
    for line in daughter:
        mother.append(line * 3)

    for line in daughter:
        mother.append(line + " " * (n // 3) + line)

    for line in daughter:
        mother.append(line * 3)

    return mother

N = int(input())
for line in star(N):
    print(line)