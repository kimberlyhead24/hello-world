import re
def extract_pid(log_line):
  regex = r"\[(\d+)\]"
  result = re.search(regex, log_line)
  if result is None:
    return ""
  return result[1]

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
print(extract_pid(log))
