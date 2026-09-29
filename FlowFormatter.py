flows_str: str = """a ↦ 14
b ↦ 17
c ↦ 11
d ↦ 6
e ↦ 18
f ↦ 4
g ↦ 22
h ↦ 20
i ↦ 19
j ↦ 16
k ↦ 10
l ↦ 13
m ↦ 9
n ↦ 7
o ↦ 5
p ↦ 12
q ↦ 23
r ↦ 3
s ↦ 2
t ↦ 21
u ↦ 15
v ↦ 8
w ↦ 24
x ↦ 1"""

rows = flows_str.split("\n")
out_list: list[str] = []
for row in rows:
    parts = row.split(" ")
    weight = parts[-1]
    out_list.append(weight)

print((", ").join(out_list))