
import os
for filename in sorted(os.listdir("C:/Users/Paulo/Pictures/Saved Pictures"))[:1]:
    filename_relPath = os.path.join("C:/Users/Paulo/Pictures/Saved Pictures",filename)
    os.remove(filename_relPath)