# **Python Basics!**

For all those looking to learn python from scratch , you can begin with the material given below, while those of you who are already familiar with python and are just looking to revise can go through [this notebook](https://github.com/Agam9427/WiDS-2022-23/blob/main/Week%201/Python_review.ipynb).  

For the first week we will be covering some basic topics:
* [Getting Started](#getting-started)
* [Introduction to Data Types and Data Structures in Python](#introduction-to-data-types-and-data-structures-in-python)
* [Operators in Python](#operators-in-python)
* [Conditions and Loops](#conditions-and-loops)
* [Python Functions](#functions)
* [Scope of Variables](#scope-of-variables)
* [Recursion](#recursion)
* [Python Modules and Packages](#modules-and-packages)
* [Some Standard libraries of python](#some-standard-libraries-of-python)
* [Classes and Objects](#classes-and-objects)
* [File Handling (Optional)](#file-handling-optional)
* [Assignment](#assignment)

Then we'll go through some data science libraries.
# Data Science Libraries!

Now, we will look at Applications of Python in Data Analysis fields and will cover various python libraries used for this namely :
* [Numpy](#Numpy)
* [Pandas](#Pandas)
* [Matplotlib](#Matplotlib)
* [Seaborn](#Seaborn)
* [Scikit-learn](#Scikit-learn)

 And Finally, we'll start with a basic introduction of Machine Learning
 
 # Getting Started With Machine Learning
 
 The two main and the most time consuming steps(which include a bunch of substeps) of machine learning will be taken care of in this week namely :
 * [Data Collection](#Data Collection)
 * [Data Preparation](#Data Preparation)

Let's get this party started!

Python is the most diverse language with very varied applications in different fields such as Research, Machine Learning, Backend Web Development, Data Visualisation, Web Scraping and much more, and this is possible only because of the different libraries and frameworks available for Python.In subsequent weeks we will be covering some amazing applications of python.
Let's get started!
## **Getting Started**

### **Installation and Setup**

Visit this link for a detailed guide on installing and setting up Python - [Python Installation and Setup](https://wiki.python.org/moin/BeginnersGuide/Download)

### **Introduction to Jupyter Notebooks**

Jupyter notebook is a web based notebook environment which is widely used for interactive programming, that is, code execution combined with rich markdown text and much more. The Jupyter notebook runs a local Ipython kernel on your machine and launches in your web browser. These notebooks are also called as Ipython notebooks, and have a '.ipynb' extension instead of traditional '.py' extension for Python files. All the assignments for this course are made in Jupyter notebooks and you are expected to complete them in the notebook itself. Hence, it is important for you to get aquainted with Jupyter notebooks.

Visit this link for installing and setting up a basic notebook - [Setting up Jupyter Notebook](https://realpython.com/jupyter-notebook-introduction/). The link also teaches you to write and execute a basic Python code in a Notebook cell.

### **Google Colab**
Google Colab is a platform provided by Google, which runs a Jupyter notebook in the cloud. While it is a convenient way to get set up, there are some caveats you would like to know before it.
The setup is platform agnostic i.e. all you need is a browser. The recommended way to get started is first logging in to Google. Sign in > Head to the home page for Google Colab [here](https://colab.research.google.com/notebooks/intro.ipynb#recent=true) > click on New Notebook.
From this point, everything is basically the same as a Jupyter notebook.


### Instructions on downloading and using notebooks

1. Open the respective `.ipynb` file on GitHub
2. In the upper right corner, there are several buttons and icons including the ones shown below. Click on the Raw Button.
       Raw | Blame
      --- | ---
      
3. The python notebook opens as raw text in browser. Right click->Save as OR just press CTRL + S. Save the notebook, open it using Jupyter Notebook you just installed and start learning! 


## **Introduction to Data Types and Data Structures in Python**
Once you have set up the environment for writing your code, we now begin with coding in Python. Let's get started.

Head over to this link - [Introduction to Python Data Types](https://www.learnpython.org/en/Welcome) and start with the topics in the 'Learn the Basics' sections one by one (till 'Basic String Operations'). These are official tutorials from the Python organisation which are well curated for beginners and contain an inbuilt Ipython shell for writing and executing your code there itself.

If you are not of the reading kind, checkout this [Youtube playlist](https://www.youtube.com/playlist?list=PLzMcBGfZo4-mFu00qxl0a67RhjjZj3jXm) for step-by-step tutorials on Python basics (Tutorials #1 - #11 except #6, #7, #9). But make sure that you are following alongside with the video, otherwise things won't make sense later in the course.

You can also read these concepts from GeeksForGeeks. They explain each concept in good detail along with examples.

Irrespective of where you choose to read/watch from, you should be familiar with the following topics:
* [Strings](https://www.geeksforgeeks.org/python-strings/?ref=lbp)
* [Lists](https://www.geeksforgeeks.org/python-list/?ref=lbp)
* [Tuples](https://www.geeksforgeeks.org/python-tuples/?ref=lbp)
* [Sets](https://www.geeksforgeeks.org/python-sets/?ref=lbp)
* [Dictionary](https://www.geeksforgeeks.org/python-dictionary/?ref=lbp)
* [Arrays](https://www.geeksforgeeks.org/python-arrays/?ref=lbp)

## **Operators in Python**
Now that you have a basic idea about different variable data types and data structures, let us now explore how you can work with multiple variables at once in order to get your desired output. This is done using Operators.

Operators in a programming language mean the same thing as operators in maths (almost), so the only thing you need to be concerned about is the syntax of working with operators.

Head over to this link - [Python Operators](https://www.geeksforgeeks.org/python-operators/?ref=lbp) for a detailed description of different operators in Python. Then check out the tabs in the navigation bar on the left and read about all the operators one by one.
These are extremely important as some of the concepts explained here will be used to define other concepts later on, and to understand any piece of code analytically, you should know what each line of code is doing.
You can also checkout this [video tutorial](https://www.youtube.com/watch?v=4XA9CKJJbr4&list=PL0-84-yl1fUnRuXGFe_F7qSH1LEnn9LkW&index=4) based on the book [Automate the Boring Stuff with python](https://automatetheboringstuff.com/2e/). 
You should be familiar with the following Python operators:

* Arithmetic Operators
* Relational Operators
* Logical Operators
* Bitwise Operators
* Assignment Operators
* Identity Operators
* Membership Operators

## **Conditions And Loops**
Conditions and Loops are a core part of any program written in any programming language. You use loops whenever you want to perform a particular task repeatedly over many iterations, given a condition is satisfied. Conditions are also used without loops, as if-else conditions.

Checkout this link for a detailed article on Conditions and Loops - [Conditions](https://www.learnpython.org/en/Conditions) and [Loops](https://www.learnpython.org/en/Loops)
You can also refer to this link from GeeksForGeeks - [Conditions and Loops](https://www.geeksforgeeks.org/python-if-else/?ref=lbp) (Checkout all the tabs in the navigation bar on the left)
Again, if you prefer videos instead, refer to this [Youtube Playlist's Tutorial](https://www.youtube.com/playlist?list=PLzMcBGfZo4-mFu00qxl0a67RhjjZj3jXm) #6, #7 and #9.

Make sure you have covered the following topics -

* For loop
* while loop
* break statement
* continue statement
* If-else condition ( normal, nested, if-elif)


## Functions
Functions are the named blocks of code that are designed to do one specific job. When you want to perform a particular task that you’ve defined in a function, you call the name of that function responsible for it. If you need to perform that task multiple times throughout your program, you don't need to type all the code for the same task again and again; you just call the function dedicated to handling that task, and the call tells Python to run the code inside the function. You’ll find that using functions makes your programs easier to write, read, test, and fix.
You can see [this notebook](https://github.com/Agam9427/WiDS-2022-23/blob/main/Week%201/Functions.ipynb) which covers some details about the functions.  
If you prefer to watch videos to learn you can head over to [this link](https://www.youtube.com/watch?v=1OuRhD7FmTA&list=PLzMcBGfZo4-mFu00qxl0a67RhjjZj3jXm&index=12).

## **Scope of a Variable**
The location where we can find a variable and also access it if required is called the scope of a variable. Variables that are defined inside a function body have a local scope, and those defined outside have a global scope. This means that local variables can be accessed only inside the function in which they are declared, whereas global variables can be accessed throughout the program body by all functions.

If you want to learn more about functions and scope you can visit [this](https://automatetheboringstuff.com/2e/chapter3/) link.

## Recursion
Python also accepts function recursion, which means a defined function can call itself.
Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amount of memory or processor power. However, when written correctly, recursion can be a very efficient and mathematically-elegant approach to programming.
You can go through [this link](https://realpython.com/python-recursion/) to learn about recursion and see some implementations of recursion. 

If you prefer to watch videos you can go through [this video](https://www.youtube.com/watch?v=zbfRgC3kukk).

## **Python Modules and Packages**
One advantage of functions is the way they separate blocks of code from your main program. By using descriptive names for your functions, your main program will be much easier to follow. You can go a step further by storing your functions in a separate file called a module and then importing that module into your main program.
Storing your functions in a separate file allows you to hide the details of your program’s code and focus on its higher-level logic. It also allows you to re-use functions in many different programs. When you store your functions in separate files, you can share those files with other programmers without having to share your entire program. Knowing how to import functions also allows you to use libraries of functions that other programmers have written.

You can go through [this notebook](https://github.com/Agam9427/WiDS-2022-23/blob/main/Week%201/Modules%26Packages.ipynb) to learn about modules and packages.

## **Iterators**
Iterator in python is any python type that can be used with a ‘for in loop’. Python lists, tuples, dicts and sets are all examples of inbuilt iterators. These types are iterators because they implement following methods.In fact, any object that wants to be an iterator must implement following methods.

__ iter__ method that is called on initialization of an iterator. This should return an object that has a next or __ next__ (in Python 3) method.

next ( __ next__ in Python 3) The iterator next method should return the next value for the iterable. When an iterator is used with a ‘for in’ loop, the for loop implicitly calls next() on the iterator object. This method should raise a StopIteration to signal the end of the iteration.

To read more about Iterators refer [this](https://www.geeksforgeeks.org/iterators-in-python/)

## Some Standard libraries of python

In python, a collection of predefined modules and packages is called a library. There are a lot of useful and interesting libraries available in python. Using such libraries often helps in reducing the effort and saves time in a number of places. Here, we will learn about some of the standard library modules:

_Note: Don’t forget to first import the module using statements like “import math” which was covered in modules and packages!!!!_ 
- The math Library: Python has a built-in module that you can use for mathematical tasks.The math module has a set of methods and constants. Some of these methods often come in handy. You go to [this](https://docs.python.org/3/library/math.html) link to learn about the methods and constants in the math module. It's beneficial to know about some of the basic trigonometric, exponential, logarithmic functions and some numeric ones like factorial, fabs, floor, ceil etc. They are used quite frequently.  
- The random library:  This module implements pseudo-random number generators for various distributions. Some of the functions that you should be familiar with are seed(), randrange(), randint(), choice(), choices(), sample(), random(), uniform(). You head over to [this](https://docs.python.org/3/library/random.html) link to learn about this library.
- The time library: This module provides various time-related functions. You should know about the terms epoch, seconds since epoch, local time, UTC, struct_time and also  about functions used in conversions from struct_time to seconds since epoch etc. You can head over to [this](https://realpython.com/python-time-module/) link and learn about these. 
- The datetime library:  The datetime module supplies classes for manipulating dates and times.You should have a basic idea about creating a date and datetime objects and know about some of the methods. You can head over to [this](https://www.geeksforgeeks.org/python-datetime-module-with-examples/) link to learn about them. 

Important thing to note here is you don’t really need to remember all of these functions/methods. Instead you should just be familiar with the module, know about what kind of methods and constants are there in it. Whenever you are working and need to use any function/method from a module but don’t remember the exact syntax you can just head over to that module’s documentation.

## Classes and Objects
**Object-oriented programming** is one of the most effective approaches to writing software. In object-oriented programming you write classes that represent real-world things and situations, and you create objects based on these classes. You can think of a class as a collection of many different functions and attributes (variables) that can be accessed by an object of that class. These methods inside a class are defined almost in the same way normal Python functions are defined, with a major difference being the '_self_' argument and some special methods only found in a class body, for example:- the '_\_\_init___' method, '_\_\_add___' method, etc.

When you write a class, you define the general behavior that a whole category of objects can have. When you create individual objects from the class, each object is automatically equipped with this general behavior; you can then give each object whatever unique traits you desire.

Making an object from a class is called _instantiation_, and you work with _instances_ of a class. You’ll specify the kind of information that can be stored in instances, and you’ll define the actions that can be taken with these _instances_.

You can visit [this notebook](https://github.com/Agam9427/WiDS-2022-23/blob/main/Week%201/Classes.ipynb) to learn about classes and objects.   
You can also go through [this video](https://www.youtube.com/watch?v=jQiUOV15IRI&list=PLzMcBGfZo4-l1MqB1zoYfqzlj_HH-ZzXt&index=2).


## *File Handling (Optional)*
Since we have covered a good number of topics , we are keeping File Handling as optional.Those who are interested in learning this can go through the article below.

Files are named locations on disk to store related information. They are used to permanently store data in a non-volatile memory (e.g. hard disk). Since Random Access Memory (RAM) is volatile (which loses its data when the computer is turned off), we use files for future use of the data by permanently storing them. When we want to read from or write to a file, we need to open it first. When we are done, it needs to be closed so that the resources that are tied with the file are freed.

Hence, in Python, a file operation takes place in the following order:

* Open a file
* Read or write (perform operation)
* Close the file

To read more about File Handling refer [this](https://www.geeksforgeeks.org/file-handling-python/)


This brings us to the end of this week's material. By now you should  be familiar with the basics of python. You should have a good enough idea about concepts like data types, loops, operators, iterators, functions, modules and packages, classes in python. Do go through the assignment after finishing the reading material. It will give you a chance to apply these concepts and practice your skills. Next week we will learn to use python in the field of data analysis. 

## Assignment

You should now be able to complete the snippet of code designed to read a particular piece of text and answer user's queries about certain words by printing the context in which these words appeared in the text. You can find it as a Jupyter Notebook [here](https://github.com/Agam9427/WiDS-2022-23/blob/main/Week%201/Assignment.ipynb).

**Optional Assignment** : Think Completing the Snippet was a piece of cake for you? Learn about the Goodstein Function from [here](https://en.wikipedia.org/wiki/Goodstein%27s_theorem#Goodstein_sequences), then try to implement a function which calculates the the kth term of G(m). 


## Numpy
### What is NumPy?
NumPy stands for Numerical Python. One of the most fundamental packages in Python, NumPy is a general-purpose array-processing package.It is a Python library used for working with arrays.It provides high-performance multidimensional array objects and tools to work with the arrays. NumPy is an efficient container of generic multi-dimensional data.
NumPy’s main object is the homogeneous multidimensional array where their dimensions are called axes and the number of axes is called rank. NumPy’s array class is called ndarray aka array.To read more about NumPy head over to this [link](https://numpy.org/doc/stable/user/whatisnumpy.html)

### Installation of Numpy
For installation you can refer [this](https://www.w3schools.com/python/numpy/numpy_getting_started.asp)
Once you are done with the installation part , you can use it by importing it in your applications by adding **import** keyword. 
  
### Getting Started With Numpy

Check this [notebook](https://github.com/Agam9427/WiDS-2022-23/blob/main/Week%201/Numpy.ipynb) to get basic knowledge of Numpy.Relevant links to websites and documentations have been provided in the notebook itself.  




## Pandas
Pandas is an open-source Python package that provides high-performance, easy-to-use data structures and data analysis tools for the labeled data in Python programming language. Pandas stand for **Python Data Analysis Library**.
**When to use?**
Pandas is a perfect tool for data wrangling or munging. It is designed for quick and easy data manipulation, reading, aggregation, and visualization.
Pandas take data in a CSV or TSV file or a SQL database and create a Python object with rows and columns called a data frame. The data frame is very similar to a table in statistical software, say Excel or SPSS.

### What can you do with Pandas?
* Indexing, manipulating, renaming, sorting, merging data frame
* Update, Add, Delete columns from a data frame
* Impute missing files, handle missing data or NANs
* Plot data with histogram or box plot

### Getting Started With Pandas

Check this [notebook](https://github.com/Agam9427/WiDS-2022-23/blob/main/Week%201/Pandas.ipynb) to get basic knowledge of Pandas .Relevant links to websites and documentations have been provided in the notebook itself.  




## Matplotlib
Matplotlib is a data visualization library and 2-D plotting library of Python.It is a close resemblance to MATLAB embedded in Python programming language.
Histogram, bar plots, scatter plots, area plot to pie plot, Matplotlib can depict a wide range of visualizations. With a bit of effort and tint of visualization capabilities, with Matplotlib, you can create just any visualizations.
Matplotlib also facilitates labels, grids, legends, and some more formatting entities with Matplotlib. Basically, everything that can be drawn!

### Installation of Matplotlib
For installation you can refer [this](https://www.w3schools.com/python/matplotlib_getting_started.asp)
Once you are done with the installation part , you can use it by importing it in your applications by adding **import** keyword.

### Getting Started With Matplotlib

Check this [notebook](https://github.com/Agam9427/WiDS-2022-23/blob/main/Week%201/Matplotlib.ipynb) to get basic knowledge of Pandas .Relevant links to websites and documentations have been provided in the notebook itself.  

 
 
 
## Seaborn
Check out [this](https://www.w3schools.com/python/numpy/numpy_random_seaborn.asp) or [this](https://www.datacamp.com/community/tutorials/seaborn-python-tutorial).
You can also look at [Seaborn documenation](http://seaborn.pydata.org/introduction.html) to know more about Seaborn.




## Scikit-learn

Scikit-learn is a free software library for Machine Learning coding primarily in the Python programming language.Scikit-learn is built on top of other Python libraries like NumPy, SciPy,  Matplotlib, Pandas, etc. and so it provides full interoperability with these libraries.You can implement various Supervised and Unsupervised Machine learning models on Scikit-learn like Classification, Regression, Support Vector Machines, Random Forests, Nearest Neighbors, Naive Bayes, Decision Trees, Clustering, etc. with Scikit-learn. 

### Components of scikit-learn
Scikit-learn comes loaded with a lot of features. Here are a few of them to help you understand the spread:
* **Supervised learning algorithms**: Think of any supervised machine learning algorithm you might have heard about and there is a very high chance that it is part of scikit-learn. Starting from Generalized linear models (e.g Linear Regression), Support Vector Machines (SVM), Decision Trees to Bayesian methods – all of them are part of scikit-learn toolbox.
* **Cross-validation**: There are various methods to check the accuracy of supervised models on unseen data using sklearn.
* **Unsupervised learning algorithms**: Again there is a large spread of machine learning algorithms in the offering – starting from clustering, factor analysis, principal    component analysis to unsupervised neural networks.
* **Feature extraction**: Scikit-learn for extracting features from images and text

Check out [this documentation](https://scikit-learn.org/stable/) to get a deeper understanding of deploying it in machine learning, pre-processing, cross-validation and visualization algorithms.

## Data Collection
→ The quantity & quality of your data dictate how accurate our model is

→ The outcome of this step is generally a representation of data (Guo simplifies to specifying a table) which we will use for training

→ Using pre-collected data, by way of datasets from [Kaggle](https://www.kaggle.com/), [UCI](https://archive.ics.uci.edu/ml/datasets.php), etc., still fits into this step

→ Another way of collecting data is **[Web Scraping](https://www.geeksforgeeks.org/what-is-web-scraping-and-how-to-use-it/)** using packages like BeautifulSoup. Learn web scraping in python from [here](https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/). Also here's a good [Youtube Video](https://www.youtube.com/watch?v=uufDGjTuq34) .

## Data Preparation
→ Wrangle data and prepare it for training

→ Clean that which may require it (remove duplicates, correct errors, deal with missing values, normalization, data type conversions, etc.)

→ Randomize data, which erases the effects of the particular order in which we collected and/or otherwise prepared our data

→ Visualize data to help detect relevant relationships between variables or class imbalances (bias alert!), or perform other exploratory analysis

→ Split into training and evaluation sets

Learn more about [Data Preparation](https://www.alteryx.com/glossary/data-preparation) and **Exploratory Data Analysis** which is arguably the most important step. Here's a good [Youtube Playlist](https://youtube.com/playlist?list=PLZoTAELRMXVPQyArDHyQVjQxjj_YmEuO9) for EDA. [Here's](https://www.youtube.com/watch?v=v5dqavbyE-I) a short video recap for EDA.

## Assignment 2
Refer to the three files namely [data_october.csv](https://github.com/Agam9427/WiDS-2022-23/blob/main/Week%201/data_october.csv),[data_november.csv](https://github.com/Agam9427/WiDS-2022-23/blob/main/Week%201/data_november.csv) and [data_december.csv](https://github.com/Agam9427/WiDS-2022-23/blob/main/Week%201/data_december.csv)
Combine the three files programmatically, Carry out EDA and draw some inferences by working with the data. These inferences can be related to anything that can help the firm make decisions or create new strategies. Keep a .ipynb python notebook for the code and a word/doc file for inferences. Submission link will be provided :). I'll share my solution for this at the end.

## Optional Assignment (Hard)
This will be a big challenge and completing this will surely make you stand out.

**DATA EXTRACTION AND NLP**

## Objective
The objective of this assignment is to extract textual data articles from the given URL and perform text analysis to compute variables that are explained below. 

## Data Extraction

For each of the articles, given in the input.xlsx file, extract the article text and save the extracted article in a text file with URL_ID as its file name.

While extracting text, please make sure your program extracts only the article title and the article text. It should not extract the website header, footer, or anything other than the article text. 

** NOTE: YOU MUST USE PYTHON PROGRAMMING TO EXTRACT DATA FROM THE URLs. YOU CAN USE BEATIFULSOUP, SELENIUM OR SCRAPY, OR ANY OTHER PYTHON LIBRARIES THAT YOU PREFER FOR DATA CRAWLING. **

## Data Analysis
For each of the extracted texts from the article, perform textual analysis and compute variables, given in the output structure excel file. You need to save the output in the exact order as given in the output structure file, “Output Data Structure.xlsx”



## Variables
Definition of each of the variables is given in the “Text Analysis.docx” file.
Look for these variables in the analysis document (Text Analysis.docx):
* POSITIVE SCORE
* NEGATIVE SCORE
* POLARITY SCORE
* SUBJECTIVITY SCORE
* AVG SENTENCE LENGTH
* PERCENTAGE OF COMPLEX WORDS
* FOG INDEX
* AVG NUMBER OF WORDS PER SENTENCE
* COMPLEX WORD COUNT
* WORD COUNT
* SYLLABLE PER WORD
* PERSONAL PRONOUNS
* AVG WORD LENGTH

## Output Data Structure
Output Variables: 
* All input variables in “Input.xlsx”
* POSITIVE SCORE
* NEGATIVE SCORE
* POLARITY SCORE
* SUBJECTIVITY SCORE
* AVG SENTENCE LENGTH
* PERCENTAGE OF COMPLEX WORDS


