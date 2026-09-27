inp_str: str = """A ↦ 5
B ↦ 6
C ↦ 9
D ↦ 7
E ↦ 1
F ↦ 8
G ↦ 11
H ↦ 13
I ↦ 2
J ↦ 10
K ↦ 3
L ↦ 12
M ↦ 4
N ↦ 14"""

rows = inp_str.split("\n")
data = []
for row in rows:
    parts = row.split(" ")
    name_num = f'"{parts[0]}" -> {parts[-1]}'
    data.append(name_num)
print(",\n".join((data)))