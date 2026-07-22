# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: TaskPulse
import json, os

class ProfileManager:
    def __init__(self):
        self.profiles = {}
        self.active_profile = None
        profile_file = 'profiles.json'
        if os.path.exists(profile_file):
            with open(profile_file) as f:
                data = json.load(f)
                self.profiles = {name: dict(p) for name, p in data.items()}

    def add_profile(self, name, priority='medium', tags=None):
        if not name or len(name.strip()) == 0:
            return False
        if name.lower() in [p.lower() for p in self.profiles]:
            return False
        profile = {'priority': priority, 'tags': tags or []}
        self.profiles[name] = profile
        with open('profiles.json', 'w') as f:
            json.dump(self.profiles, f, indent=2)
        if not self.active_profile:
            self.active_profile = name
        return True

    def switch_profile(self, name):
        lower_name = name.lower()
        for p_name in self.profiles:
            if p_name.lower() == lower_name:
                self.active_profile = p_name
                with open('profiles.json', 'w') as f:
                    json.dump(self.profiles, f, indent=2)
                return True
        print(f"Profile '{name}' not found.")
        return False

    def get_active_profile(self):
        if self.active_profile and self.active_profile in self.profiles:
            return self.profiles[self.active_profile]
        return None

    def list_profiles(self):
        return [{'name': name, **self.profiles[name]} for name in self.profiles]
