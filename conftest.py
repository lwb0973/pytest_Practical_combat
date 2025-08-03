import os
import platform
import settings

def to_unicode_escape(s: str) -> str:
    r"""中文字符转成 \uXXXX，英文数字保持不变"""
    return ''.join(f'\\u{ord(c):04x}' if ord(c) > 127 else c for c in s)

def get_run_environment():
    return os.environ.get('ENV', 'unknown')  # 默认值为 unknown

def get_browser_name():
    return os.environ.get('BROWSER', 'Chrome')

def get_os_version():
    return platform.platform()

def write_environment_properties(allure_dir=settings.RESULT_FILE):
    os.makedirs(allure_dir, exist_ok=True)
    env_data = {
        "Environment": get_run_environment(),
        "Browser": get_browser_name(),
        "Version": get_os_version(),
        "Tester": "卢炜飚"
    }
    with open(os.path.join(allure_dir, "environment.properties"), "w", encoding="ascii") as f:
        for k, v in env_data.items():
            f.write(f"{k}={to_unicode_escape(v)}\n")

write_environment_properties()
