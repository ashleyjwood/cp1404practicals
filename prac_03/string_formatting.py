# f-string formatting for guitar info
brand = "Gibson"
model = "L-5 CES"
year_released = int(
    1951)  # Corrected release year https://www.gibson.com/en-US/p/Electric-Guitar/GCPV0006-1978-Custom-L-5-CES/Wine-Red
cost = float(16035.9)
print(f"{year_released} {brand} {model} for about ${cost:,.0f}!")

# print a list of values of 2^n
for i in range(11):
    print(f"2 ^{i:2} is {2 ** i:4}")
