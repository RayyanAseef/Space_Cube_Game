
import time

test = True

# If Else Statement

start = time.time(  )

if test: value = True
else: value = False

if test: value = True
else: value = False

if test: value = True
else: value = False

if test: value = True
else: value = False

if test: value = True
else: value = False

end = time.time(  )

print( f"Seconds: {end-start}" )

# Ternary Opeator

start = time.time(  )

value = True if test else False
value = True if test else False
value = True if test else False
value = True if test else False
value = True if test else False

end = time.time(  )

print( f"Seconds: {end-start}" )
