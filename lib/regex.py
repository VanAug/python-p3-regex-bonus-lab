import re

my_pattern = (
    r"[A-Z][^.!?]*\b(?:today|today['’]s)\b[^.!?]*[.?]"
)
my_regex = re.compile(my_pattern)
