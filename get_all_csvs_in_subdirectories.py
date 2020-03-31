import os
import os.path

files = []
for dirpath, dirnames, filenames in os.walk("."):
    for filename in [f for f in filenames if f.endswith(".csv")]:
        files.append(os.path.join(dirpath, filename))
        
frames = []

for i in files:
    df = pd.read_csv(i)
    frames.append(df)
