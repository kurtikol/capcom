# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: TaskPulse
import json, os


APP_CONFIG = {
    "app_name": "TaskPulse",
    "version": 30,
    "max_priority_levels": 5,
    "default_tags": ["urgent", "planning", "done"],
    "daily_log_retention_days": 90,
    "data_dir": os.path.join(os.path.dirname(__file__), "data"),
}

def load_app_config():
    config_file = os.path.join(APP_CONFIG["data_dir"], "config.json")
    if not os.path.exists(config_file):
        with open(config_file, "w", encoding="utf-8") as f:
            json.dump(APP_CONFIG, f, ensure_ascii=False)
    else:
        with open(config_file, "r", encoding="utf-8") as f:
            loaded = json.load(f)
        APP_CONFIG.update(loaded)


def update_app_config(updates):
    APP_CONFIG.update(updates)
    config_file = os.path.join(APP_CONFIG["data_dir"], "config.json")
    with open(config_file, "w", encoding="utf-8") as f:
        json.dump(APP_CONFIG, f, ensure_ascii=False)


if __name__ == "__main__":
    load_app_config()
