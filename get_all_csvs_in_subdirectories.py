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

n = 0
for i in names:
    print(n,i)
    n+=1

name_list = []
lens = []
space = " "
for i in range(len(names)):
    lens.append(len(frames[i]))
    name_list.append(names[i])
    
# intialise data of lists. 
data = {'length':lens, 'filename':name_list} 
  
# Create DataFrame 
df = pd.DataFrame(data) 
df = df.sort_values(by="length",ascending=False)
