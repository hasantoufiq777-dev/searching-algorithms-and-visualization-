
def trapezoid(x, a, b, c, d):
    if x <= a or x >= d:
        return 0
    elif b <= x <= c:
        return 1
    elif x < b:
        return (x - a) / (b - a)
    else:
        return (d - x) / (d - c)


def triangle(x, a, b, c):
    if x == b:
        return 1
    elif x <= a or x >= c:
        return 0
    elif x < b:
        return (x - a) / (b - a)
    else:
        return (c - x) / (c - b)


# Input values
temperature = 28
humidity = 70


# 1. FUZZIFICATION

cold = triangle(temperature, 0, 0, 20)
warm = triangle(temperature, 10, 20, 30)
hot = triangle(temperature, 20, 40, 40)

low = triangle(humidity, 0, 0, 60)
high = triangle(humidity, 40, 100, 100)

print("FUZZIFICATION")
print("Cold =", cold)
print("Warm =", warm)
print("Hot =", hot)
print("Low =", low)
print("High =", high)


# 2. RULE EVALUATION

R1 = min(hot, high)
R2 = warm
R3 = max(cold, low)

print("\nRULE FIRING STRENGTHS")
print("R1 (Fast) =", R1)
print("R2 (Medium) =", R2)
print("R3 (Slow) =", R3)


# 3. CLIPPING AND AGGREGATION

x = range(101)
aggregated = []

for i in x:
    slow = min(R3, triangle(i, 0, 0, 50))
    medium = min(R2, triangle(i, 25, 50, 75))
    fast = min(R1, triangle(i, 50, 100, 100))

    aggregated.append(max(slow, medium, fast))


# 4. DEFUZZIFICATION

numerator = 0
denominator = 0

for i in range(len(aggregated)):
    numerator += i * aggregated[i]
    denominator += aggregated[i]

if denominator != 0:
    crisp_speed = numerator / denominator
else:
    crisp_speed = 0

print("\nDEFUZZIFICATION")
print("Crisp Fan Speed =", crisp_speed)
