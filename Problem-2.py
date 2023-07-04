def series_number(x):
    series = []
    num = 1
    for _ in range(x):
        series.append(num)
        num += 2
    return series
x = int(input("Enter the value of x: "))
result = series_number(x)
print("Output:", ', '.join(map(str, result)))