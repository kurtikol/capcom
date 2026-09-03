# === Stage 45: Добавь восстановление из резервной копии ===
# Project: TaskPulse
def restore_from_backup(file_path, backup_file):
    with open(backup_file, 'r') as f:
        data = json.load(f)
    with open(file_path, 'r') as f:
        existing = json.load(f)
    existing.update(data)
    with open(file_path, 'w') as f:
        json.dump(existing, f, indent=2)
    print(f"Backup restored from {backup_file}")
