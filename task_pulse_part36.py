# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: TaskPulse
def repair_data(data):
    """Repair simple integrity issues: empty task, duplicate id, invalid priority."""
    if not data.get("tasks"):
        data["tasks"] = []
    for i in range(len(data["tasks"])):
        t = data["tasks"][i]
        if "id" not in t or not isinstance(t["id"], int):
            t["id"] = len(data["tasks"]) + 1
        if "priority" not in t or t["priority"] not in (1, 2, 3):
            t["priority"] = 2
        if "status" not in t:
            t["status"] = "pending"
    return data

def check_integrity(data):
    """Return list of integrity issues found."""
    issues = []
    if not isinstance(data, dict) or "tasks" not in data:
        issues.append("missing tasks key")
        return issues
    seen_ids = set()
    for i, t in enumerate(data["tasks"]):
        if not isinstance(t, dict):
            issues.append(f"task {i} is not a dict")
            continue
        if "id" not in t:
            issues.append(f"task {i} missing id")
        elif t["id"] in seen_ids:
            issues.append(f"duplicate task id {t['id']} at index {i}")
        else:
            seen_ids.add(t["id"])
        if "priority" not in t or t["priority"] not in (1, 2, 3):
            issues.append(f"task {i} invalid priority")
    return issues

def fix_and_report(data):
    """Apply repairs and return both fixed data and a list of repaired items."""
    issues = check_integrity(data)
    if not issues:
        return data, []
    for issue in issues:
        print(f"  [REPAIR] {issue}")
    repaired_data = repair_data(data)
    return repaired_data, issues
