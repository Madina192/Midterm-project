# Midterm-project
# Rules

Each cell can be in one of four states:
empty
conductor
electron head
electron tail

The simulation proceeds in discrete steps. Each step changes the cells in the following ways:

#__empty → empty
#__electron head → electron tail
#__electron tail → conductor
#__conductor → Electron head if one or two neighboring cells are electron heads, else it remains a conductor. 
A cell neighbors another if it is orthogonally or diagonally adjacent (Moore neighborhood).

Run worldwire.py to start it. Requires Python 3.

Conductor cells are yellow, electron heads are blue and electron tails are red.
