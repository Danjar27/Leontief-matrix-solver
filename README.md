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
            

you must create an np.array with this format:

values = [[a1, b1],[a2.,b2]]

rather than 

values = [[a1, a2],[b1, b2]]