import re


YT_PATTERN = r'((youtu\.be/|(www\.)?youtube\.com/watch\?v=)(\w{11}))'


def parse_links(text: str) -> list:
    matches = re.findall(YT_PATTERN, text)

    return list(map(lambda match: match[0], matches))
