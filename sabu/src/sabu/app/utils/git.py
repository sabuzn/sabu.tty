from pathlib import Path

def is_git() -> None:
    cwd: str = Path.cwd()
    
    if any((parent / ".git").exists() for parent in [cwd, *cwd.parents]):
        return "\x1b[93m⑂ .git\x1b[0m"
    return
