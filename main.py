from mean_var_std import calculate

result=calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
print("{")
for i, (key, value) in enumerate(result.items()):
    comma = "," if i < len(result) - 1 else ""
    print(f"  '{key}': {value}{comma}")
print("}")