edge_str: str = """a,a*,b,b*,c,c*,d,d*,e,e*,f,f*,g,g*,h,h*,i,i*"""

replace_tuple = (',', '", "')
out_str = f'"{edge_str.replace(*replace_tuple)}"'
print(out_str)
print(edge_str)
rows = edge_str.split(",")
rows_filtered = [row for row in rows if row[-1] != "*"]
print(rows_filtered)
out_list: list[str] = []
for row in rows_filtered:
    temp_str: str = f'"{row}" -> "{row}*", "{row}*" -> "{row}"'
    out_list.append(temp_str)
print(",\n".join(out_list))

omega_cycles_str = """The ordering of edges around vertex 1 is: h* ↦ e* ↦ a ↦ h*.
The ordering of edges around vertex 2 is: a* ↦ b ↦ i ↦ f* ↦ a*.
The ordering of edges around vertex 3 is: c ↦ b* ↦ c.
The ordering of edges around vertex 4 is: c* ↦ g* ↦ d ↦ f ↦ h ↦ i* ↦ c*.
The ordering of edges around vertex 5 is: e ↦ d* ↦ g ↦ e."""

omega_rows = omega_cycles_str.split("\n")
omega_list: list[str] = []
for row in omega_rows:
    useful = row.split(":")[-1].strip(".")
    parts = useful.split(" ↦ ")
    temp_omega: list[str] = []
    for part in parts[:-1]:
        temp_omega.append(part)
    temp_omega_str: str = '{"'+f'{('", "').join(temp_omega)}'+'"}'
    omega_list.append(temp_omega_str)
print(",\n".join(omega_list))