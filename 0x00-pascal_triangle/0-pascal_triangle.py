def pascal_triangle(n):
    if n < 0:
        return []
    if n == 1:
        return [[1]]
    li = pascal_triangle(n - 1)
    arrlen = len(li[-1])
    temp = [li[-1][0]]
    for i in range(1, arrlen):
        temp.append(li[-1][i - 1] + li[-1][i])
    temp.append(li[-1][-1])
    li.append(temp)
    return li
