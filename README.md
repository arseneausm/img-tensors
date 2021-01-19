## img-tensors

The aim of this project is to represent video and image files as tensors and then see what we can do with them. The current roadmap has n steps:

1. Create a function for generating video files of resolution n x n.
2. Create a function that graphs the values of bit (p,q) with p, q =< n. This isn't really a necessary step but hell I just think it'd be kinda cool.
3. Based on that data, compute a discreet Fourier approximation of the data
4. Generate some function f:R^{2+1} -> R^{3} with R^{2+1} referring to (p,q) + time and R^{3} referring to r,g,b.
5. ...
6. Profit
