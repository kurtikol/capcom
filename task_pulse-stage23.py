# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: TaskPulse
def print_table(tasks, max_w=40):
    """Компактный вывод списка задач в виде отформатированной таблицы."""
    if not tasks:
        print("Задач нет.")
        return
    cols = ["id", "title", "prio", "tags"]
    aligns = {"id": "<", "title": "<", "prio": "<", "tags": "<"}
    widths = {c: max_w for c in cols}
    rows = []
    for t in tasks:
        row = [str(t.get(c, "")) if hasattr(t, 'get') else getattr(t, c, "") for c in cols]
        tags_str = ", ".join(getattr(t, "tags", [])) if hasattr(t, "tags") and t.tags else ""
        row[3] = tags_str[:widths["tags"]-1] + ("." if len(tags_str) > widths["tags"]-1 else "")
        rows.append(row)

    def pad(s, w, a):
        return s.ljust(w) if a == "<" else s.rjust(w)

    print("\n┌" + "─"*sum(widths.values()) + "┐")
    for c in cols:
        print(f"| {pad(c, widths[c], aligns[c])}")
    print("└" + "─"*sum(widths.values()) + "┘")
    for r in rows:
        line = "".join(pad(r[i], widths[cols[i]], aligns[cols[i]]) for i in range(len(cols)))
        print(f"| {line} |")
