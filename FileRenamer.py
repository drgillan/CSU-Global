import os
os.chdir('.')
i=1
for file in os.listdir():
  src=file
  dst="2019_"+str(i)+".docx"
  os.rename(src,dst)
  i+=1
