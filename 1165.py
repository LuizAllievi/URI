N = int(input())

entries = []

for i in range(N):
    term = int(input())
    entries.append([term, 0])
    x = 1
    count = 0
    while x <= term:
        if term % x == 0:
            count += 1
        x += 1
    if count <= 2: entries[i][1] = 1

for term in entries:
    if term[1]:
        print("{} eh primo".format(term[0]))
    else:
        print("{} nao eh primo".format(term[0]))
