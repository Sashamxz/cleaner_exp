#! python3
#  Password manager

import pyperclip
text = pyperclip.paste()

# разделиь строки звездочками

lines =text.split('\n')
#print(lines)
for i in range(len(lines)):
    lines[i] = "* " + lines[i]

text = '\n'.join(lines)
pyperclip.copy(text)

