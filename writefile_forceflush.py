import os

# Open a file with default line-buffering.
f = open('myfile.txt', 'w')

# No newline character, so not written to disk immediately
f.write('Write me to a file, please!')

# Force output buffer to be written to disk
f.flush()
os.fsync(f.fileno())
