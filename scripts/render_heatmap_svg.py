import json

q = chr(34)
PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]

with open("data/contributions.json") as f:
    days = json.load(f)

svg_boxes = []
for i, day in enumerate(days):
    col = i // 7
    row = i % 7
    x = col * 15
    y = row * 15
    color = PALETTE[day["level"]]
    delay = (col + row) * 0.015
    svg_boxes.append(
        f"<rect x={q}{x}{q} y={q}{y}{q} width={q}11{q} height={q}11{q} rx={q}2{q} fill={q}{color}{q} style={q}animation: fadeIn 0.4s ease forwards {delay:.3f}s; opacity: 0;{q}/>"
    )

svg_content = chr(10).join([
    f"<svg width={q}860{q} height={q}125{q} xmlns={q}http://www.w3.org/2000/svg{q}>",
    "<style>",
    "  @keyframes fadeIn {",
    "    from { opacity: 0; transform: translateY(-3px); }",
    "    to { opacity: 1; transform: translateY(0); }",
    "  }",
    "</style>",
    f"<rect width={q}100%{q} height={q}100%{q} fill={q}#0d1117{q} rx={q}6{q} />",
    f"<g transform={q}translate(15, 12){q}>",
    *svg_boxes,
    "</g>",
    "</svg>"
])

with open("contrib-heatmap.svg", "w") as f:
    f.write(svg_content)

print("contrib-heatmap.svg basariyla olusturuldu.")
