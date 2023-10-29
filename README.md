# Project Organization

This is a markdown (.md) file. In VSCode you can view it in its formatted version by hitting SHIFT-CMD/CTRL-V.

## Adding Python Library Dependencies

- Add library dependencies (the names of Python libraries you want to be installed) to requirements.txt.
- Use pip install -r requirements.txt to install required libraries from this file.
- Use pip freeze to obtain a requirements.txt file for the current environment.

## The movies.py Program

This file reads, provides an opportunity to change, and writes Excel files, by way of Pandas data frames. In particular, it reads movies.xls,
an Excel spreadsheed with several thousand records of data on movies.

## The graph.py and graph.ipynb Programs

Graph.py is a Python program. Graph.ipynb is the same program in the form of a Jupyter notebook. For exploratory data analysis I suggest using Jupyter notebooks. In Jupyter you can mix Python code and documentation written and formatted using simple Markdown markup notations.

## The .devcontainer Directory

This directory contains files that tell Docker how to build the operating system "container" that contains all the Python and operating system software to make this whole thing work; and tell VSCode what extensions to load and what Dockerfile to use to build this container.

## Data Files

The data.csv file is a tiny file with two columns of data to play around with. It's what the Graph programs use as input to produce Seaborn graphs.
The movies.xls file is several thousand lines of data on movies. We thank the sources of this data and the available teaching videos online.

## Data Plotting Using Seaborn

Watch a few YouTube tutorials and test out the ideas in the files we provide. Level of difficulty: low.

## Installation

### On Mac

You need a display manager on your local host machine. I believe I installed XQuartz.
