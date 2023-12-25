import list_module as lm

IndiaStates=lm.indian_states

for i in IndiaStates:
    print(i)
else:
    print("\n")
    print("End")

import platform

x = platform.system()
print(x)

print(platform.architecture())
print(platform.machine())
print(platform.processor())
print(platform.python_build())
print(platform.release())

import os

list_os=dir(os)

for i in list_os:
    print(i)

