weights_str: str = """a ↦ 2
b ↦ 20
c ↦ 14
d ↦ 7
e ↦ 4
f ↦ 19
g ↦ 12
h ↦ 8
i ↦ 1
j ↦ 13
k ↦ 16
l ↦ 5
m ↦ 17
n ↦ 15
o ↦ 18
p ↦ 9
q ↦ 10
r ↦ 3
s ↦ 11
t ↦ 6"""

rows = weights_str.split("\n")
out: list[str] = []
for row in rows:
    parts = row.split(" ↦ ")
    temp_str: str = f'"{parts[0]}" -> {parts[-1]}'
    out.append(temp_str)
print(",\n".join(out))