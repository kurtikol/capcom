# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: TaskPulse
def backup_data_file(data_file_path, backup_dir="backups"):
    import os
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, "data_backup_" + timestamp + ".json")
    try:
        with open(data_file_path, "r", encoding="utf-8") as src, open(backup_path, "w", encoding="utf-8") as dst:
            dst.write(src.read())
        print(f"[OK] Backup saved to {backup_path}")
    except Exception as e:
        print(f"[ERR] Backup failed: {e}")
