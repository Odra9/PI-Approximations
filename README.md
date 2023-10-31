# π Approximations

This is a personal project. Written in Python.

## Overview

### What

Each file in this repo is a python script which approximates the value of pi using a different method. See [#methods](#methods) for a complete list and description of all methods.

### Why

The only goal I had for this was to have fun creating it. I find exploring different ways to approximate π to be fun.

## Methods

Following is an explanation of how all this files work

### Library

#### ApproxFormatLib.py

This is the only file which does not contain a way to approximate PI. This file is used to standardize the input and output among all the other scripts.

Imports the library sys and numpy.

Contains the following two methods:

##### getN()

All algorithms used are in some way or another iterative. `getN` is used to tell the script how many iterations to go through before stopping.

It defaults to N = 10. This can be either changed by passing the number of iterations as an argument in the terminal

`python3 <script_name> <number_of_iterations>`

or by passing the number of iteration as a variable to the `getN(x)` function (basically changing the default value for that script).

The function also displays to the user what number of iterations is being used.

##### displayApprox(approx)

This function displays in the terminal the approximation of PI (`approx`) that has been reached.

DELTA is defined as |approx - PI|, with PI the constant in the numpy library

err% is defined as $|DELTA/π| \cdot 100$

### Scripts

#### Circle enclosed in a Square.py

If you take a circle enclosed in a square, their respective surfaces will be:  
$sCircle = π \cdot r^2$  
$sSquare = 4r^2$

The ratio between these two surfaces is $sCircle/sSquare = π/4$

Here in this script instead of surface, a set of randomly placed points is used.
Because the points are always inside of the square, the formula to approximate π becomes:  
$π = 4 \cdot pointsInCircle/totalPoints$

See [Square enclosed in a Circle](#square-enclosed-in-a-circlepy)

#### Coprimes.py

The probability of two random numbers being coprime is $\frac{6}{π}$

Thus we can approximate π from the following formula: $π = \sqrt{\frac{(6*totalCouples)}{coprimeCouples}}$

For a detailed explanation see:  
[Matt Parker's video](https://www.youtube.com/watch?v=RZBhSi_PwHU)  
[This Proof](https://www.cut-the-knot.org/m/Probability/TwoCoprime.shtml)

#### Leibniz.py

The Leibniz formula for π is:  
$4 \cdot \sum\limits_{i=0}^{\infty}\frac{(-1)^n}{(2n+1)}$

#### Machin.py

From wikipedia:
>In mathematics, Machin-like formulae are a popular technique for computing π

Here the formula used is $\frac{π}{4} = 4 \cdot arctan\frac{1}{5} - arctan\frac{1}{239}$ with a custom function to compute the arctan of a number using the **MacLaurin series**

#### Si(x).py

Si(x) is defined as the integral of $\frac{sinx}{x}$ from 0 to x.

The integral of $\frac{sinx}{x}$ between `-Inf` and `Inf` is equal to π at the limit.

Here this integral is calculated in the interval `[-WIDTH, WIDTH]` approximating the area under the curve from 0 and WIDTH with trapezoids and then multiplying by two as sin(x) is an even function.

#### Square enclosed in a Circle.py

If you take a square enclosed in a circle, their respective surfaces will be:  
$sSquare = l^2$  
$sCircle = π \cdot (\sqrt{2}/2  \cdot  l)^2 = π \cdot l^2/2$

The ratio between these two surfaces is $sCircle/sSquare = π/2$

Here in this script instead of surface, a set of randomly placed points is used.
Because the points are *not* always inside of the square, the formula to approximate π becomes:  
$π = 4 \cdot pointsInCircle/pointsInSquare$

See [Circle enclosed in a Square](#circle-enclosed-in-a-squarepy)

#### Stirling.py

The Stirling formula to approximate factorials is:  
$n! \approx \sqrt{2 \cdot π \cdot n}(\frac{n}{e})^n$ with $n -> {\infty}$

From which π can be calculated as:  
$π = \frac{n^(\frac{1}{2}-n) \cdot e^n \cdot (n-1)!}{e}$
