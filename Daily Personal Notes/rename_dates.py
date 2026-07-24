import os
import re

for filename in os.listdir("."):
    match = re.match(r"(\d{1,2})\.(\d{1,2})\.(\d{2})(.*)\.md$", filename)

    if match:
        month, day, year, extra = match.groups()

        new_name = f"20{year}-{int(month):02d}-{int(day):02d}{extra}.md"

        print(f"{filename} -> {new_name}")
        os.rename(filename, new_name)
