weights_str: str = """a ↦ 16
b ↦ 3
c ↦ 9
d ↦ 13
e ↦ 10
f ↦ 20
g ↦ 12
h ↦ 2
i ↦ 15
j ↦ 11
k ↦ 6
l ↦ 8
m ↦ 5
n ↦ 18
o ↦ 4
p ↦ 7
q ↦ 14
r ↦ 19
s ↦ 17
t ↦ 1"""

rows = weights_str.split("\n")
out: list[str] = []
for row in rows:
    parts = row.split(" ↦ ")
    temp_str: str = f'"{parts[0]}" -> {parts[-1]}'
    out.append(temp_str)
print(",\n".join(out))