==============
Zombie Dev Log
==============

`Code sleeps here <https://github.com/radustoenescu/zombie-dev>`_

Day 1 (Optimal matrix chain multiplication)
-------------------------------------------

Because I know pretty well the Hanoi tower problem, I started with
`Day 2 <https://medium.com/100-days-of-algorithms/day-2-matrix-chain-multiplication-3ae6349c34ab>`_.

The `Matrix chain multiplication <https://en.wikipedia.org/wiki/Matrix_chain_multiplication>`_
problem is a quite straightforward example of `Dynamic programming <https://en.wikipedia.org/wiki/Dynamic_programming>`_.

I implemented the basic algorithm. Wikipedia also points to a better algorithm, which I only skimmed over since
it's quite complex and well beyond what I'm doing here.

It took me:

    - thinking: 2m
    - coding: 17m
    - debugging: 9m
    - total: 28m

In future I think I can limit debugging greatly since I made some noob mistakes which required quite a bit of
looking around the code to fix, but the coding went smooth and I didn't search the documentation that much.

You can find the code in the `usual place <https://github.com/radustoenescu/zombie-dev>`_. Nothing fancy. Maybe
the ``@functools.lru_cache`` decorator is quite nice to check out since it makes memoization a lot easier to add.
