import os
import os.path

files = []
for dirpath, dirnames, filenames in os.walk("."):
    for filename in [f for f in filenames if f.endswith(".csv")]:
        files.append(os.path.join(dirpath, filename))

frames = []
names = []
try:
    os.mkdir("output")
except:
    print("file exists")

for i in files:
    name =i.split("/")[-1]
    names.append(name)
    df = pd.read_csv(i)
    df.to_csv("output//"+name)
    frames.append(df)
