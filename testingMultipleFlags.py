
"""
# 
# Author: l33tH@x0rxxGh0u1
# Title: Passing Multiple Flags
#
# Description:  Pass multiple conditions in a elif statement
# 
#
"""

### First Example

x, y, z = 0,1,0

## Single Assignment
if x==1 or y==1 or z==1:
    print('passed')

## Multiple Assignment
if 1 in (x,y,z):
    print('passed')
# Assigning multiple variables to a condition at once
# NOTE: This is asking python if 1 is in the TUPLE (x,y,z)




## Example Two

# Test only if TRUE
# Basic use would be say you have a bunch of flag variables in a game to signal the end of
# the game upon different conditions. I.e You can either quit the game by dying or pausing and quiting the game 
# or pressing the xbox button and straight to your systems home

# So you have x, y, and z that represent game quit

# Single Ass.
if x or y or z:
    print('passed')

# Multiple Ass.
if any((x,y,z)):
    print('passed')
