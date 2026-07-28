# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: TaskPulse
TEMPLATE_REGISTRY = {
    "daily_checkin": {"fields": ["title", "notes"], "defaults": {"priority": 3, "tags": [], "status": "todo"}},
    "bug_report": {"fields": ["title", "description", "severity"], "defaults": {"priority": 1, "tags": ["bug"], "status": "backlog"}},
    "feature_request": {"fields": ["title", "description", "impact"], "defaults": {"priority": 3, "tags": [], "status": "backlog"}}
}

def create_from_template(name, user_input=None):
    if name not in TEMPLATE_REGISTRY:
        raise ValueError(f"Unknown template: {name}. Available: {list(TEMPLATE_REGISTRY.keys())}")
    tpl = TEMPLATE_REGISTRY[name]
    record = dict(tpl["defaults"])
    for field in tpl["fields"]:
        value = user_input.get(field) if user_input else None
        record[field] = value if value is not None else input(f"  {field}: ")
    return Task(record)
