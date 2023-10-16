import re


def format_string(string: str, pattern: str, replacements: list[str]):
    result = ""
    for idx, text in enumerate(re.sub(pattern, "{+INSERT}", string).split("{+INSERT}")):
        result += text
        if len(replacements) > idx:
            result += replacements[idx]
    return result


def is_empty(string: str):
    return len(string) == 0


def path(*paths: str):
    return "/".join(paths)


def split_path(paths: str):
    return [i for i in re.split(r"[/:]", paths) if i]
