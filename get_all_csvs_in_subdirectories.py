import os
import os.path

for dirpath, dirnames, filenames in os.walk("."):
    for filename in [f for f in filenames if f.endswith(".csv")]:
        print(os.path.join(dirpath, filename))
