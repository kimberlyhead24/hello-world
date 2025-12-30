#!/usr/bin/env python3

import csv, re

OLD, NEW = "abc.edu", "xyz.edu"
pattern = re.compile(rf"@{OLD}$")

with open("/home/student/data/user_emails.csv", newline="") as f:
    rows = list(csv.reader(f))

i = rows[0].index(" Email Address")
for r in rows[1:]:
    r[i] = pat.sub(f"@{NEW}", r[i])

with open("/home/student/data/updated_user_emails.csv", "w", newline="") as f:
    csv.writer(f).writerows(rows)
