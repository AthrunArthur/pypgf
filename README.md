pypgf -- A light weight python frontend for PGFPlots
==================
###What is pypgf?

It's a light weight python frontend for PGFPlots. As a frontend, it can do

    1. coding with python, like processing your data;
    2. plotting your data via converting it to PGFPlots figures.

However, as a light weight frontend, it *won't* generate the visible figure (like PDF) for you. 
All pyplot tries to do is generating a tex file for you, and it's your job to compile it with latex.

###Why pypgf?

First of all, I hope you like plotting with PGFPlots and processing your data with python. If you are not, forget pypgf.

The idea behind pypgf is that we always need some customization when we use PGFPlots. We may customize some fonts for our figures, use some customized commands, even some symbols. So we decide leave pypgf as light as possible since you may need to modify the tex file directly.

A way we prefer is to include the PGFPlots figures' tex files directly. In this case, it's free to use any customized thing, like fonts or commands. So we just need a frontend tool help us generating the tex file.

###Use it!

pypgf is just a simple python package. Everything is just intuitive.


###Contact me!
If you have any questions, including bugs, documents and suggestions. Please send me email and let me know via xuepeng_fan@163.com. 

Have fun!
