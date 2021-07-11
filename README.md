<h1>How to use it</h1>

Use

from leontief import *


Package contains one function: leontief(values,names,demand,new_demand) 

You must replace all four given arguments in order to solve a matrix.

For <b>values</b> you must not use columns but rows of the matrix you want to solve. For instance, if you matrix looks like this:


|   | A  | B  |
|---|----|----|
| A | a1 | b1 |
| B | a2 | b2 |
            

you must create a np.array with this format <b>[[a1, b1],[a2,b2]]</b> rather than [[a1, a2],[b1, b2]]

<b>names</b> use an array of String values for table column's names just like ['A','B']

<b>Demand</b> and <b>New demand</b> are n vectors you can create using np.array [c1,c2,c3 ... ] their dimension must be same as number of rows ther are in values array 
