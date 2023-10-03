# CMPS 2200 Assignment 2

**Name:**__kayla willis_______________________

In this assignment we'll work on applying the methods we've learned to analyze recurrences, and also see their behavior in practice. As with previous assignments, some of of your answers will go in `main.py` and `test_main.py`. You should feel free to edit this file with your answers; for handwritten work please scan your work and submit a PDF titled `assignment-02.pdf`and push to your github repository.

1. Derive asymptotic upper bounds of work for each recurrence below.
  * $W(n)=2W(n/3)+1$
.  since f(n)=1, time complexity is O(n)
the root is f(n) which is 1, level 1 is 2*(n/3)+1 showing geometric shrinking at each level, so it's root dominated. we have 2^i subproblems and height is log_3(n) so work=2^1+2^2...2^(height=log_3(n)+1) so we can simplify to 3^(log_3(n))=n and using log rules get that the complexity is O(n)
.  
.  
.  
.  
  * $W(n)=5W(n/4)+n$
.  here f(n)=n is the root and level 1 is 5*(n/4), showing geometric growth and therefore is leaf dominated. work of each level is 5^i and the height is when n=4^h, so h=log_4(n). since its geometric, we get that (5^(log_4(n)))=>O(n^log_4(5))
.  
.  
.  
.  
  * $W(n)=7W(n/7)+n$
.  root is n and level 1 is 7*(n/7) which is also n. this pattern continues so it is balanced and the max of each level will be n. our work is n*i so i=log_7(n) and n=n, so work is O(nlog_7n)
.  
.  
.  
.  
  * $W(n)=9W(n/3)+n^2$
.  root is n^2, level 1 is 9*(n/3)^2=n^2 making it balanced and the max cost per level is n^2. num levels is log_3(n) so n^2*log_3(n) so O(n^2log_3(n))
.  
.  
.  
.  
  * $W(n)=8W(n/2)+n^3$
.  root is n^3, level 1 is 8*(n/2)^3 simplifying to n^3, making it balanced. max cost per level is thus n^3 and num levels is lg(n) so O(n^3lg(n))
.  
.  
.  
.  
  * $W(n)=49W(n/25)+n^{3/2}*log n$
.  root is n^(3/2)logn, level 1 is 49*((n/25)^(3/2)*log(n/25)) since we have to plug n/25 into both instances of n in n^2/3*logn. simplifying: 49*(n^(2/3)/125)log(n/25)=>(49/125)(n^(2/3))(logn/25). this shows decreasing leafs, so it is root dominated so O(n^(3/2)log(n)) 
.  
.  
.  
.  
  * $W(n)=1W(n-1)+2$
.  root is 2, level 1 is 2*(n-1)+2 which is 2*1+2=4. there are n levels because it is linear growth and it is growing geometrically and the time complexity is thus also O(n)
.  
.  
.  
.  
  * $W(n)= W(n-1)+n^c$, with $c>= 1$
.  root is n^c, level 1 is (n-1)^c. This turns into: W(n-1)+n^c
W(n-1-1)+(n-1)^c+n^c
W(n-1-1-1)+(n-2)^c+(n-1)^c+n^c...W(1)+(n-1)^c+(n-2)^c...+2^c+1^c showing the base case plus the recursive step until it reaches the end. thus we can find the upper bound by adding the base (W(1)) to a summation where k eventually reaches n:
W(n)=W(n-k)+k(n^c) => W(n-n)+n(n^c) => 1+n^(1+c) so O(n^1+c)
.  
.  
.  
  * $W(n)=1W(sqrt{n})+1$
root is 1, level 1 is 1+sqrt(n), level 2 is 1+1+(n^1/4)...work will be n^1/2i and stops when n reaches 2. set up the equality: n^(1/2^i)=2 => lg(n^(1/2^i))=lg2 => (1/2^i)*lgn=1 => lgn = 2^i => i=lglg(n) so O(lglg(n))

2. Suppose that for a given task you are choosing between the following three algorithms:

  * Algorithm $\mathcal{A}$ solves problems by dividing them into
      five subproblems of half the size, recursively solving each
      subproblem, and then combining the solutions in linear time.
    
  * Algorithm $\mathcal{B}$ solves problems of size $n$ by
      recursively solving two subproblems of size $n-1$ and then
      combining the solutions in constant time.
    
  * Algorithm $\mathcal{C}$ solves problems of size $n$ by dividing
      them into nine subproblems of size $n/3$, recursively solving
      each subproblem, and then combining the solutions in $O(n^2)$
      time.

    What are the asymptotic running times of each of these algorithms?
    Which algorithm would you choose?


3. Now that you have some practice solving recurrences, let's work on implementing some algorithms. In lecture we discussed a divide and conquer algorithm for integer multiplication. This algorithm takes as input two $n$-bit strings $x = \langle x_L, x_R\rangle$ and $y=\langle y_L, y_R\rangle$ and computes the product $xy$ by using the fact that $xy = 2^{n/2}x_Ly_L + 2^{n/2}(x_Ly_R+x_Ry_L) +
  x_Ry_R.$ Use the
  stub functions in `main.py` to implement Karatsaba-Ofman algorithm algorithm for integer
  multiplication: a divide and conquer algorithm that runs in
  subquadratic time. Then test the empirical running times across a
  variety of inputs in `test_main.py` to test whether your code scales in the manner
  described by the asymptotic runtime. Please refer to Recitation 3 for some basic implementations, and Eqs (7) and (8) in the slides https://github.com/allan-tulane/cmps2200-slides/blob/main/module-02-recurrences/recurrences-integer-multiplication.ipynb
 
