#GArbage collection class to make sure the unused objects are deleted 

import gc

# always True
print(gc.isenabled())

# to disable gc 

gc.disable()

print(gc.isenabled())  #to check

# to enable

gc.enable()

print(gc.isenabled())