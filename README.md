# Overview

This is a markdown (.md) file. In VSCode you can view it in its formatted version by hitting SHIFT-CMD/CTRL-V. The rest of this file explains what the files are in this directory.

.devcontainer is a directory containing the files that (1) tell Docker how to build the operating system "container" that contains all the Python and operating system software to make this whole thing work; and (2) tell VSCode what extensions to load automatically and a few other things, including what Dockerfile to use to build this container. 

Graph.py is a Python program. Graph.ipynb is the same program in the form of a Jupyter notebook. For exploratory data analysis I suggest using Jupyter notebooks. Jupyter is great because you can mix Python code and documentation written using Markdown for nice formatting.

The requirements.txt file lists Python libraries that are needed for all of this to work. You can add a library by adding its name to the end of this file and then rebuild this container (CMD/CTRL-SHIFT-P then Rebuild Container). 

The data.csv file is just a tiny file with two columns of data, to play around with. It's what the Python programs use as input to produce Seaborn graphs.

To learn how to use Seaborn, I suggest watching a few YouTube tutorials.