weights_str: str = """a ↦ 26
b ↦ 54
c ↦ 26
d ↦ 47
e ↦ 44
f ↦ 90
g ↦ 92
h ↦ 93
i ↦ 8
j ↦ 27
k ↦ 97
l ↦ 14
m ↦ 75
n ↦ 22
o ↦ 28
p ↦ 36
q ↦ 41
r ↦ 44
s ↦ 56
t ↦ 21
u ↦ 36
v ↦ 56
w ↦ 49
x ↦ 59"""

rows = weights_str.split("\n")
out_list: list[str] = []
for row in rows:
    parts = row.split(" ")
    weight = parts[-1]
    out_list.append(weight)

print((", ").join(out_list))