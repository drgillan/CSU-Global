import os
os.chdir('YOURPATH')
i=1
for file in os.listdir():
  src=file
  dst="YOURSTRING"+str(i)+".YOURFILEEXTENSION"
  os.rename(src,dst)
  i+=1
