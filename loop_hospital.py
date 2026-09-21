# loop_hospital.py

print("--- Patient 1 ---")
# FIXED: range(1, 10) excludes 10 (off-by-one error). Changed upper bound to 11 so range(1, 11) prints 1 through 10.
for i in range(1, 11):
    print(i)

print("\n--- Patient 2 ---")
# FIXED: The variable n was never decremented inside the loop, causing an infinite loop. Added 'n -= 1' inside the loop body.
n = 3
while n > 0:
    print(n)
    n -= 1

print("\n--- Patient 3 ---")
# FIXED: 'total = 0' was placed inside the loop, resetting total to 0 on every iteration. Moved 'total = 0' outside the loop before it starts.
total = 0
for i in range(1, 6):
    total = total + i
print(f"Total: {total}")