inp_str: str = """edge0 ↦ {vertex4,vertex0}
edge1 ↦ {vertex6,vertex3}
edge2 ↦ {vertex4,vertex2}
edge3 ↦ {vertex5,vertex4}
edge4 ↦ {vertex0,vertex1}
edge5 ↦ {vertex3,vertex1}
edge6 ↦ {vertex1,vertex4}
edge7 ↦ {vertex6,vertex0}
edge8 ↦ {vertex5,vertex3}
edge9 ↦ {vertex5,vertex2}
edge10 ↦ {vertex5,vertex1}
edge11 ↦ {vertex2,vertex3}
edge12 ↦ {vertex6,vertex1}
edge13 ↦ {vertex4,vertex6}
edge14 ↦ {vertex5,vertex0}
edge15 ↦ {vertex3,vertex0}
edge16 ↦ {vertex6,vertex5}
edge17 ↦ {vertex2,vertex6}"""
rows = inp_str.split("\n")
data: list[str] = []
for row in rows:
    parts = row.split("{")[-1].split("}")[0].split(",")
    edges = []
    for part in parts:
        edges.append(part[-1])
    out_row: str = r"\[UndirectedEdge]".join(edges)
    data.append(out_row)
print(",\n".join(data))