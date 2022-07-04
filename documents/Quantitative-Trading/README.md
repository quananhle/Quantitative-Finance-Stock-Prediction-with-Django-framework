# Quantitative Trading

## Menu

* [Stock Prices](#stock-prices)
 	* [Stocks](#Stocks)
	* [Options: calls, puts, American, European](#Options: calls, puts, American, European)
		* [Frontend](#frontend)
		* [Datalayer](#datalayer)
		* [Backend](#backend)
	* [Low Level Design](#low-level-design)
* [Requirement](#requirement)
	* [Change Request (Document)](#change-request-document)
	* [Req Analysis (IT Assessment)](#req-analysis-IT-assessment)
		* [Frontend](#frontend)
		* [Datalayer](#datalayer)
		* [Backend](#backend)
	* [Low Level Design](#low-level-design)
* [Changes](#changes)
	* [Change Summary](#change-summary)
		* [Back-end](#back-end)
		* [Front-end](#front-end)
		* [Database](#database)
	* [Change Details](#change-details)
* [Testing](#testing)
	* [Summary](#summary)
	* [Cases](#cases)

## Stock Prices

### Stocks

#### Options: calls, puts, American, European
Options give the owner the right to buy or sell at the strike price (a fixed price that is determined when the option is created), on or before an expiration date. The most common are call options and put options. Call options give the right to buy at the strike price; put options give the owner the right to sell at a fixed price. Some options allow the holder to “exercise” (buy or sell) at the strike price any time up to the expiration date. These are called “American options” by convention, even though this doesn’t mean that the options are traded in the Americas. Another class of options only allows the holder to exercise the option at the expiration date, but not earlier. These are called “European options” by convention, but again, European options don’t necessarily have to be traded in Europe.

#### Forwards and Futures
Futures and forwards contracts are similar, in that a buyer and seller both agree to make a future transaction at a predetermined price. Futures are standardized contracts that can be traded on a futures exchange, so this may be what people think of when discussing “forwards and futures”. Forward contracts are usually privately determined contracts between two parties. So an investor can trade futures contracts, but forward contracts are not designed to be traded like futures.

#### Public versus private equity
Public equity refers to stocks that can be traded on a stock exchange. Private equity refers to ownership in private companies, so the owners of private equity do not trade their shares on a stock exchange. Our course is primarily focused on public equity, which we’ll refer to as stocks, since the ability to buy and sell freely enables us to adjust our investments based on new or time-sensitive information.

#### Market Bubbles
A recent example of a bubble is bitcoin, which rose from from under $1,000 per coin in January of 2017, to over $17,000 per coin by December of the same year, before dropping to about $6,000 by June of 2018.

#### How many trading days are there in a typical year for NYSE? 
252 days

### Fundamental Information

#### Fundamental Analysis
Fundamental analysis of a company involves looking at a company’s balance sheet and cash flow statements, which are usually updated every quarter, which is every three months when the company reports earnings. It’s important to keep in mind that looking at a single quarter’s metrics is only a snapshot of the company, and there are several metrics that each try to capture the health of the company, but in slightly different ways.

In a way, analyzing a company’s fundamentals is like going on a safari taking photographs of an antelope. A single still photo from one angle may tell you some things about the antelope, but taking multiple photos from different angles will give you a better view. Also, taking multiple photos over time will give you a sense of where the antelope is going. So before we introduce some commonly used metrics, please keep in mind that to get a better picture of a company that you’re trying to analyze, you’ll want to look at a collection of different measures over time.

#### Sales Per Share
A company’s revenue is based on its sales over that quarter, so we can think of sales and revenue as referring to the same thing. It’s a quick way to get a sense for how a company is doing, because we don’t have to subtract out cost of sales, which depends a bit on some accounting decisions. For example, if a company sells a million smartphones for a hundred dollars each over the past 3 months, then its revenue is $100 times 1 million, or $100 million. If the company issued ten million shares, then its sales per share is $100 million divided by ten million, or $10 per share.

You may be wondering why we bother dividing sales by the number of shares. This helps shareholders get a sense of how much the sales figures might impact a change in a single share price. You can imagine that if the company only issued 10 shares, a report of higher sales than forecasted would impact each share more than if the company issued ten million shares.

Also, note that sales of $10 per share probably does not mean that the shareholders will get $10 for each share that they own, or that their stock price will increase by $10. It costs money for the company to make each smartphone. Let’s take a look at a metric that accounts for cost of sales next.

#### Earnings Per Share
Earnings is the company’s revenue minus its cost of sales. Cost of sales refers to the cost of manufacturing the phone, employee wages, rent payments for office space, and the cost of equipment, like machines that make the phones. Earnings gives investors a sense of how much the equity of the company has changed over the past 3 months. Recall that stock represents a fractional ownership of a company’s equity.

Continuing with the smartphone company example, let’s say we can estimate the cost of sales per phone to be $80 per phone. If the sales per phone is $100, then the earnings per phone is $100 - $80 equals $20 per phone. With sales of one million phones, earnings would be $20 times one million, or $20 million.

With ten million shares, this is earnings of $20 million divided by ten million shares, which is $2 earnings per share.

Note again, that this $2 per share doesn’t mean that investors automatically receive an additional $2 per share in their pocket. Let’s look at one way that investors do receive some of those earnings by looking at dividends.

#### Dividends Per Share
After a company has positive earnings, they may decide to either reinvest the cash in growing the company’s business. A company’s executives are usually expected to make spending decisions based on maximizing shareholder value. Whether this always happens in practice is debatable, but ideally, if the executives decide that re-investing in the business yields lower returns than an investor could gain from investing in a similar business at the same level of risk, they will give some of the earnings to shareholders as cash. This cash is referred to as dividends.

Let’s say, for example, that the smartphone company decides to return $10 million of its earnings to its shareholders. The dividend per share is then $10 million divided by 10 million, or $1 per share.

### Price Earnings Ratio
#### Price to Earnings Ratio
A term you’ll see often is price to earnings ratio, or PE ratio for short. This is the stock’s current market price divided by its most recently reported earnings per share (EPS). You can sort of interpret the PE ratio as how much the company is valued compared to how much money it made. It’s important to be careful about how we interpret a high or low PE ratio, because we can’t say whether a PE ratio is good or bad by looking at it in isolation. Let’s first look at where the price comes from. This market price of a share is based on the collective estimates by investors of the company’s current equity plus its future earnings. The future earnings are based on estimates of future cash flow, which are then adjusted to their present-day value, or Present Value (PV). This is getting a bit outside the scope of what you’ll need to know for this course, but the point we want you to remember is that the market price of a stock is based on both its current assets minus liabilities, but also estimates of the company’s future performance.

Now coming back to the PE ratio. What does it mean to have a high PE ratio? A company may have low or negative earnings, but a high stock price. Why do you think that is? You may have heard of certain startups that are valued at billions of dollars, and yet have low earnings. This is because investors expect potential for high earnings growth, based on the trajectory of past earnings growth. This also means that investors are estimating that the high stock price relative to earnings will be justified by high future earnings. On the other hand, it’s also possible that investor optimism towards the company’s future never materializes, in which case the stock may be overpriced.

Note also that a low PE ratio can also be due to different underlying reasons. An example of a company with a low PE ratio may be one that has high and stable earnings, but less expectations for future growth. Since the company may decide that its investors are better off receiving earnings as dividends instead of reinvesting earnings into the business, the earnings will be distributed as cash to shareholders. This also means that the stock price itself represents the value of the company excluding the cash that was already distributed to these shareholders. Again, keep in mind that a low PE ratio can also be a sign of something else. If a company is expected to face pressure from competitors or government regulation that reduce their expectations for future earnings, then investors may pay a lower price for each share, and that could also result in a lower PE ratio.

In practice, you’ll want to see how a company’s PE ratio compares to other similar companies in the same industry and same geographic region.

You’ll see PE ratios again in later lessons, so for now, just remember that it’s one of many ways to take a snapshot of a company’s financial health.

### Compoundings

#### Rates of Compounding

A statement by a bank that the interest rate on one-year deposits is 4% per year sounds straightforward and unambiguous. In fact, its precise meaning depends on the way the interest rate is measured. For an interest rate statement to be clear, the magnitude and time dependence of the rate of interest, as well as the frequency of compounding, must be clearly stated.

If the interest rate is measured with annual compounding, the bank’s statement that the interest rate is 4% means that $100 grows to 
100 $\times$ (1 $\+$ .04) $\=$ \$104 at the end of 1 year.

When the interest rate is measured with semi-annual compounding, it means that 2% is earned every 6 months, with the interest being reinvested. In this case, $100 grows to 
100 $\times$ (1 $\+$ .04 $\div$ 2) $\times$ (1 + .04 $\div$ 2) $\=$ 100 $\times$ (1 + .04 $\div$ 2)<sup>2</sup> = \$104.04 at the end of 1 year.

When the interest rate is measured with quarterly compounding, the bank’s statement means that 1% is earned every 3 months, with the interest being reinvested. The $100 then grows to 
100 $\times$ (1 $\+$ .04 $\div$ 4)<sup>4</sup> = \$104.06 at the end of 1 year.

#### Continuous Compounding
Let's compare the amount of money accumulated after 1 year with the same annual rate of interest of 4%, but different rates of compounding:

| __Compounding frequency__     | __Value of $100 after 1 year__ |
| -----------                   | -----------                    |
| Annually ($n=1$)              | $104.00                        |
| Semi-annually ($n=2$)         | $104.04                        |
| Quarterly ($n=4$)             | $104.06                        |
| Monthly ($n=12$)              | $104.07                        |
| Weekly ($n=52$)               | $104.08                        |
| Daily ($n=252$)               | $104.08                        |
     
Looking at the table, you can see that with more frequent compounding, the value at 1 year increases but then seems to level off. If you assumed that the benefit of compounding more and more frequently had a limit, you would be right! How do we calculate this limit? Well, first we write down the formula for compounding,

$p_{t} = p_{t-1}(1 + \frac{r}{n})^np$

and then we notice that what we'd like to do is make n bigger and bigger. We want the limit as n goes to infinity. Well, it turns out that this limit is:

$\lim_{n\to\infty}\left( 1 + \frac{r}{n}\right)^n = \mathrm{e}^rlim$

Compounding infinitely often is called continuous compounding. So what does this mean? Well, it means that if you wanted to calculate how much money you’d have at the end of the year if you started with $100 and compounded continuously, but at a simple annual rate of 4%, you’d calculate:

$100 \times \mathrm{e}^{.04} = 104.08$

You'll notice that the value after 1 year with continuous compounding is pretty close (it's the same if we round to two decimal places) to the value after 1 year with daily compounding.

#### Continuously Compounded Return

Now, say you were trying to reverse the previous calculation. Say you knew you had $104.08 at the end of the year, and $100 at the beginning of the year, and you wanted to calculate the rate of interest as _if it had been compounded continuously_. You would simply invert the formula. So you’d calculate:
$ 104.08 \div 100 = \mathrm{e}^r $

Then you'd take the natural log of both sides, and then you'd have,
$\ln(104.08 \div 100) $=r

So,
$.04 = r$

r is the _continuously compounded annual return_. So the continuously compounded annual return equals 
$\ln(p_t/p_{t-1})$.
But what is this quantity? It’s just the log return! This is why you might hear log returns called _continuously compounded returns_.

#### Additivity
Now, say we invested \$100, and the monthly continuously compounded interest rate was 2%. At the end of the month, we’d have
$100 \times \mathrm{e}^{.02} = 102.02$

But if the investment continued to accrue at a monthly continuously compounded rate of 0.02 for a whole year, we’d have

$ 100 \times \mathrm{e}^{.02}\times \mathrm{e}^{.02}\times \mathrm{e}^{.02}\times \mathrm{e}^{.02}\times \mathrm{e}^{.02}\times \mathrm{e}^{.02}\times \mathrm{e}^{.02}\times \mathrm{e}^{.02}\times \mathrm{e}^{.02}\times \mathrm{e}^{.02}\times \mathrm{e}^{.02}\times \mathrm{e}^{.02}$ ... in total, 12 factors of $\mathrm{e}^{.02}$. 

So we'd have

$ 100 \times (\mathrm{e}^{.02*12}) = 127.12$

Equivalently,

$100 \times \mathrm{e}^{.24} = 127.12$

Since the annual rate of continuous compounding, 0.24, is simply the sum of the monthly rates of continuous compounding, we say that the continuously compounded rate of return is additive over time.

#### Annualized Rate of Return
We saw above how to calculate the annual rate of continuous compounding from the monthly rate of continuous compounding. If we just had a single monthly rate, but we assumed that the rates for all the months of the year were the same, we could extrapolate the monthly rate to an annual rate by multiplying by 12. This is called annualizing the rate of continuous compounding. Rates of return and other metrics are often converted to a common annual basis in order to make comparisons across contexts and instruments.

#### Time Additivity of Log Returns
So, as you can see, the rate of continuous compounding is additive over time. Since, mathematically, the rate of continuous compounding is just the log return, this means that log returns are additive over time, and this can be very convenient. As another example,

$\log$ return for January $+$ $\log$ return for February

$ = \ln \left( \frac{p_{\mathrm{Feb\;1}}}{p_{\mathrm{Jan\;1}}} \right) + \ln \left( \frac{p_{\mathrm{Mar\;1}}}{p_{\mathrm{Feb\;1}}} \right) $

$ = \ln(p_{\mathrm{Feb\;1}}) - \ln(p_{\mathrm{Jan\;1}}) + \ln(p_{\mathrm{Mar\;1}}) - \ln(p_{\mathrm{Feb\;1}}) $

$ = \ln(p_{\mathrm{Mar\;1}}) - \ln(p_{\mathrm{Jan\;1}}) $

$ = \ln \left( \frac{p_{\mathrm{Mar\;1}}}{p_{\mathrm{Jan\;1}}} \right) $

$\=$ $\log$ return for January and $\log$ return for February

Since the annual rate of continuous compounding, 0.24, is simply the sum of the monthly rates of continuous compounding, we say that the continuously compounded rate of return is _additive over time_.

__Numerical Stability__
Multiplication of many small numbers can result in the problem that the product is smaller than the smallest number representable in computer memory. Sometimes the computation will incorrectly yield the value 0. This is called arithmetic underflow. The use of logarithms can help with this, since it enables the representation of much smaller (and much larger) numbers. For example:

![image](https://user-images.githubusercontent.com/35042430/172473901-891fd5f9-8fee-40f3-a5c2-f5f5b6a15788.png)

### Distributions of Returns and Prices

#### Distributions of Returns and Prices
Investors are always interested in the potential appreciation or depreciation of financial assets. They'd like to be able to predict what will happen to assets in the future, hence, they'd like to be able to build models of stock prices and returns. An important first step is to think of these prices and returns as random variables, i.e. outcomes of random phenomena, that take on values as described by distributions. Distributions allow us to summarize the behavior of random variables. So, what are the distributions of returns and prices?

One strategy for getting a sense of potential future behavior is to look to the past. Let's look at some data from the stock of a familiar company with a storied past, Apple Inc.


### Returns
The raw return may be referred to simply as the _return_, or alternatively, as the _percentage return_, _linear return_, or _simple return_. It is defined as

$ r = \frac{p_t - p_{t-1}}{p_{t-1}} $

![image](https://user-images.githubusercontent.com/35042430/177209254-f7f8874d-32e1-462b-90c1-6d6d1ecdaa90.png)

![image](https://user-images.githubusercontent.com/35042430/177209295-d0acf722-3bd1-4bb0-aace-7a1f38c67dc0.png)



