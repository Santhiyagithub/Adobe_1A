def detect_hierarchy(elements):
    font_sizes = sorted(set(e["font_size"] for e in elements), reverse=True)
    size_map = {}

    if len(font_sizes) >= 3:
        size_map = {
            font_sizes[0]: "H1",
            font_sizes[1]: "H2",
            font_sizes[2]: "H3"
        }
    elif len(font_sizes) == 2:
        size_map = {
            font_sizes[0]: "H1",
            font_sizes[1]: "H2"
        }
    elif len(font_sizes) == 1:
        size_map = {
            font_sizes[0]: "H1"
        }

    outline = []
    title = ""
    for e in elements:
        lvl = size_map.get(e["font_size"])
        if not title and lvl == "H1":
            title = e["text"]
        if lvl:
            outline.append({
                "level": lvl,
                "text": e["text"],
                "page": e["page"]
            })
    return title, outline