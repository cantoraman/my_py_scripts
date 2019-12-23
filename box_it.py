#!/usr/bin/env python
import sys

#only works for piped input...
#echo "Hello World!\nIt is a beautiful day\nisn't it?" | python box_it.py
#TODO: write a script that takes arguments

if __name__ == "__main__":
    pipe = u'\u2503'
    max_size = 0
    text = ""
    line_count = 0
    for line in sys.stdin.readlines():
        max_size = len(line)-1 if len(line) > max_size else max_size
        new_line = pipe + line.strip()
        text = "".join(text+new_line+"\n")
        line_count += 1

    new_text = ""
    for line in text.split("\n"):
        if len(line) == 0:
            continue
        if (len(line) < max_size):
            new_line = line + " "*(max_size-len(line)+1) + pipe
        else:
            new_line = line + pipe
        new_text = "".join(new_text+new_line+"\n")

    top_line = u'\u250F' + (u'\u2501')*max_size + u'\u2513' + "\n"
    bottom_line = u'\u2517' + (u'\u2501')*max_size + u'\u251B' + "\n"
    text = top_line + new_text + bottom_line
    print(text)
