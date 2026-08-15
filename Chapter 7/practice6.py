a = int(input("Enter No.:"))
p = 1
for i in range (1, a+1):
    p = p*i

print(f"Factorial {a} is {p}")

"""
| Iteration | `i` | Calculation (`p = p * i`) | New `p` |
| --------- | --: | ------------------------- | ------: |
| Start     |   - | -                         |       1 |
| 1         |   1 | `1 × 1`                   |       1 |
| 2         |   2 | `1 × 2`                   |       2 |
| 3         |   3 | `2 × 3`                   |       6 |
| 4         |   4 | `6 × 4`                   |      24 |
| 5         |   5 | `24 × 5`                  |     120 |
"""