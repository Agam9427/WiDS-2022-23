# Intro to ML
For this week we will be reading articles related to ML and we'll start with the [applications in finance](#Applications-in-Finance!).

1. [What is Machine Learning?](https://www.edureka.co/blog/what-is-machine-learning/)
2. [Mathematics for Machine Learning](https://www.edureka.co/blog/mathematics-for-machine-learning/)
3. [Basic Intro and Terminologies](https://www.edureka.co/blog/introduction-to-machine-learning/)

## Supervised Learning
1. [What is supervised learning?](https://www.edureka.co/blog/supervised-learning/)
2. [Linear Regression](https://www.edureka.co/blog/linear-regression-in-python/) and it's [implementation](https://www.edureka.co/blog/linear-regression-for-machine-learning/)
3. [Classification](https://www.edureka.co/blog/classification-algorithms/) and it's [implementation](https://www.edureka.co/blog/classification-in-machine-learning/)
4. [Overfitting problem in ML](https://www.edureka.co/blog/overfitting-in-machine-learning/) and it's [solution](https://www.edureka.co/blog/regularization-in-machine-learning/)

## Unsupervised Learning
1. [What is unsupervised learning?](https://www.edureka.co/blog/unsupervised-learning/)
2. [K-means clustering](https://www.edureka.co/blog/k-means-clustering-algorithm/)
3. [K-Nearest Neighbours](https://www.edureka.co/blog/k-nearest-neighbors-algorithm/)



# Applications in Finance!

Now, you can begin looking at some of the applications of Python. Starting with its application in Finance and Specifically in
Automated-Trading in Stock Markets.

* You may get a minimal Introduction of the Stock Market and Trading (in genral) from [here](https://www.youtube.com/watch?v=bl797s8u0QQ&t=463s). You just need to know about how prices fluctuate in such Markets and how that can be used to generate profits.

* This Process of buying at low prices and selling them at higher ones could be automated to yield astronomical profits. This is what's known as Algorithmic Trading!
* Some people who effiectively automated Cryptocurrency-Trading made upto 3000% Profits, and even though that was partly fueled by the
Cryptocurrency frenzy that took over the world, In general even not-so-complex Stock Market Strategies give upto 10% cumulative Annual Profits in
certain markets.

One of the easiest Strategies in Algorithmic Trading is that of **Mean Reversion**.

* Mean reversion in stock price is the assumption that the price will tend to move back to the average price over time. Mean reversion trading often refers to counter-trend or reversal trading.
* If any stock price is currently below its average, then we should buy it, as there is every chance that it is having some down-time and will rise in coming times.
* Similarly if some Stock Price is above its Average, then that indicates, its time to sell.

You may look at a naive implementation of Mean Reversion in [Country Equity Indices](https://en.wikipedia.org/wiki/Stock_market_index) [here](https://www.quantconnect.com/tutorials/strategy-library/mean-reversion-effect-in-country-equity-indexes).

## Assignment

This week's assignments would be a great leap more difficult than last week's. If you aren't able to complete them just as easily as last week's, do not lose hope. You can always ask for help in the whatsapp. We are making two separate versions of the assignment for that purpose!

* The first version would have a basic coding architecture ready for you, and you'll only have to implement various functions (we'll also tell you what these functions are supposed to do!)

* For the second version, We will just give you the data and control flow of the Program and expect you to do the rest on your own!

Choose according to your comfort level!

If you plan to go for the second version then don't look at the first at all, as that would defeat the purpose of pushing yourself!

If you look at the Compulsory Exercises and find even the second versions to be fairly easy for you, then you may solve only the Optional Assignments and we'll still be considering you passed.

Please, Attempt the first Compulsory Exercise before proceeding to the second!
### Compulsory Assignments
#### Momentum-Effect in Stock Trading

* There's something which goes by the name of Momentum Anamoly in Trading, which says that what was strongly going up in the near past will probably continue to go up shortly. Stocks which outperform peers on 3-12 month period tend to perform well also in the future.
* You may read more about Momentum from [here](https://quantpedia.com/strategies/momentum-factor-effect-in-stocks/).

You can make use of instructions which we've provided for you in this [easier version](https://github.com/wncc/TSS-2021/blob/main/Python%20%26%20its%20Applications/Week-2/Momentum.ipynb) of the assignment or implement everything from scratch in this [notebook](https://github.com/wncc/TSS-2021/blob/main/Python%20%26%20its%20Applications/Week-2/MomentumH.ipynb) containing only the bare minimum instructions required to implement a strategy which exploits the Momentum Effect in Stock Trading.

#### Paired Switching

* You should get familiar with [Correlation](https://www.investopedia.com/ask/answers/032515/what-does-it-mean-if-correlation-coefficient-positive-negative-or-zero.asp) and its significance in Trading.
* Next, Read up about [Paired Switching](https://quantpedia.com/strategies/paired-switching/).
* The basic idea behind Paired Switching is to select two stocks which are negatively co-related, so that if one falls then the other should be rising shortly afterwards and vice versa.

You can start implementing this strategy by taking help of instructions given in this [easier version](https://github.com/wncc/TSS-2021/blob/main/Python%20%26%20its%20Applications/Week-2/Pairs.ipynb) of the assignment, or implement everything from Scratch in this [notebook](https://github.com/wncc/TSS-2021/blob/main/Python%20%26%20its%20Applications/Week-2/PairsH.ipynb) containing only the bare minimum instructions required to implement the strategy.

### Optional Assignments

#### Predicitng Outlooks using a Naive Bayes' Model

* Get to know about the Naive Bayes' Model from this [article](https://towardsdatascience.com/all-about-naive-bayes-8e13cef044cf) on Naive Bayes' Models and the part on Bernoulli's Naive Bayes' Classifier from this Wikipedia [article](https://en.wikipedia.org/wiki/Naive_Bayes_classifier).
* Get to know about various indicators used to judge where the market/prices are going. [RSI](https://blog.quantinsti.com/rsi-indicator/) (Relative Strength Index) and [Stoch](https://blog.quantinsti.com/stochastic-oscillator/) (Stochastic Oscillator) are great indicators, you may or may not stop just at them.
* Next you can use RSI, Stoch (and other Indicators of your choice) and implement a Bernoulli Naive Bayes' Classifier to predict next day's returns and then use that to trade.

You should also use Matplotlib/Seaborn to plot these results.

Pre-defined functions from the sklearn library may help you with this task!

#### Mean Reversion and Momentum

Implementing a Strategy combining [Mean Reversion](https://www.investopedia.com/terms/m/meanreversion.asp) and Momentum into one.
