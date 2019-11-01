#!/usr/bin/env python3.7

import os
import sys

readme = os.path.realpath(f"{__file__}/../../README.md")

is_reading_table = False
tools = []
with open(readme, 'r') as f:
    lineno = 0
    for l in f:
        lineno += 1
        line = l.strip()
        if not is_reading_table:
            is_reading_table = line == "<table>"
        elif line == "</table>":
            break
        else:
            if "<td><code>" in line:
                start = line.index("<td><code>")
                end = line.index("</code>")
                tool_name = line[start + 10:end]
                tools.append((tool_name, lineno))

sorted_tools = list(sorted([t[0] for t in tools], key=str.casefold))

for expected, actual in zip(sorted_tools, tools):
    tool_name = actual[0]
    if expected != tool_name:
        lineno = actual[1]
        expected_order = "\n   ".join(sorted_tools)
        print(f"Expected order:{expected_order}")
        print()
        print(f"::error file=README.md,line={lineno}::Expected {expected} to appear next in the list, but found {tool_name}")
        print(f"::error ::Tools in README are not sorted alphabetically")
        print()
        exit(1)
