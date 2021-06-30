# use varibles to convert values

kilometer = 12.25
mile = 7.38

mile_to_km = mile * 1.61
km_to_mile = kilometer / 1.61

print("12.25 KMs are",km_to_mile,"miles")
print("7.38 miles are",mile_to_km,"kilometers")
print()
# 2 decimal digit rounded output
print("2 decimal digit rounded output")
print("12.25 KMs are",round(km_to_mile,2),"miles")
print("7.38 miles are",round(mile_to_km,2),"kilometers")
