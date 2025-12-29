import re

def split_sentences(post):
    # return the result of re.split
    return re.split(r"[.?!]", post)

post1 = (
    "Today I started learning how to split sentences in Python. "
    "It feels exciting to see how regular expressions can break text into smaller parts. "
    "I wrote a simple function that uses re.split to separate sentences. "
    "Right now it splits on periods, question marks, and exclamation points. "
    "Next, I want to improve the pattern so it ignores abbreviations like Dr. "
    "or U.S.A. I will also print each sentence on its own line to make the output "
    "easier to read. This small exercise is helping me understand strings and pattern "
    "matching better. I am proud of the progress I am making as a programmer."
)

sentences = split_sentences(post1)

for s in sentences:
    if s.strip():          # skip empty strings
        print(s.strip())
