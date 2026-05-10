---
title: "I Spent a Night Reverse-Engineering Buy Borrow Die With Gemini, and Realized the F-1 Script Looks Nothing Like the Billionaire One"
date: 2026-02-08
permalink: /posts/2026/02/f1-buy-borrow-die/
tags:
  - f-1
  - personal-finance
  - international-students
  - ibkr
  - tax
  - investing
  - thinking
---

I spent a whole evening with Gemini taking apart the Buy Borrow Die playbook that American billionaires run, expecting that with a little scaling down I could just copy the moves, and what I found instead was that almost every single move has an F-1 trapdoor underneath it, and the list of things I can actually do fits on one page.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

Here is the setup, and let me put this up front so nobody gets the wrong idea. I am not a rich guy. I am just a student. There is no family money, no portfolio anybody would call meaningful, just enough in the bank to pay rent and buy groceries. But I have had this nagging itch for a while, which is to figure out exactly what the richest people in America are actually doing with their money, and then see if I can lift even one or two moves into my own life.

You probably know the headline version. Rich Americans never sell their stock, because selling triggers tax. They post their stock as collateral and borrow against it from the bank, and borrowed money is not income so there is no tax on it either. They live on the borrowed cash, reinvest it, let the asset compound. When they die, the cost basis of the asset gets reset to the market price on the day of death, this is called step-up in basis, the heirs sell some shares to pay back the loan, and the IRS basically gets nothing. That is Buy, Borrow, Die.

It sounds clean. I figured, I have IBKR, I have cash, I have credit, in theory I should be able to run a tiny version of this loop.

So I started asking Gemini, walk me through it from my balance sheet, step by step.

The first thing that stopped me cold was the mortgage piece. Billionaires never get a home loan based on their W2 income. They use Asset-based Lending, posting their portfolio as collateral, and a lot of those loans are interest-only so the cash flow drag is almost zero. Then the property itself depreciates on paper and shields rental income from tax. It feels like cheating.

The problem is, F-1 students cannot get those products. Most mainstream U.S. banks (the ones running on Fannie Mae and Freddie Mac rules) will not write a conventional mortgage for an F-1 holder. The reasoning is not complicated, your visa is considered unstable, full stop. The banks that will lend to you are places like East West Bank that specifically run Foreign National Loan programs, but the price of admission is 30% to 40% down, and the rate is no friendlier than market. I ran the math, current mortgage rates are sitting at 6%-7%, while a risk-free money market fund is paying 4%-5%. There is no arbitrage here, only a negative spread, you would be bleeding money every month.

So move number one from the billionaire playbook, dead on arrival.

The second thing that gave me a chill was the Section 179 thing. The classic billionaire bit, you set up an LLC, buy a 6000-pound vehicle like a G-Wagon or a Model X, and write off the full purchase price against your active income in the same year. Every finance influencer on the planet has talked about this one.

For a hot second I thought, fine, I can open an LLC too, F-1 students can hold assets through an LLC. Then Gemini iced the whole thing. The premise of Section 179 is that the vehicle is used for business operations. To take the deduction you have to tell the IRS, on the record, that this car is the operating vehicle of your LLC.

But your F-1 visa says, in plain language, you cannot engage in unauthorized active employment. F-1 students can hold an LLC, but they cannot operate one. The moment you take that Section 179 deduction to save a few thousand bucks in tax, you have basically signed a confession to the IRS that you violated USCIS rules. That is a trade where you bet your immigration status to win pocket change.

Yeah no. That is digging your own grave.

By this point I was pretty deflated. The two flashiest moves in the billionaire toolkit, mortgage arbitrage and LLC tax shielding, are off the table for F-1, one because the math does not work and the other because the law does not allow it.

But I was not ready to give up. I kept pushing, asking what the actually-doable moves were. Gemini reframed it for me. Forget the heavy-asset billionaire approach, lean into credit arbitrage and tax arbitrage instead. These two sound boring, but they are the one slice of the pie F-1 students can eat clean.

Credit arbitrage is just the float window on 0% APR cards. Discover, Chase Freedom Flex, those products often give new accounts 12 to 15 months at zero interest. You pay only the minimum, and every dollar you would have spent paying down the card goes into a money market fund like Fidelity SPAXX or Schwab SWVXX, paying around 5% annualized. The risk is approximately zero, and it is fully legal. I was already doing this, but Gemini's nudge was that I should push the scale a notch higher.

Tax arbitrage is even sweeter. There is a US-China Tax Treaty, and Article 20(c) of that treaty plainly states that as a Chinese student, the first 5,000 USD of your income each year is exempt from federal tax. This is not a gray-area trick, it is written into the treaty. I had used it before, but a lot of new students have no idea it exists. Stack that on top of the already low bracket a student's income lands in, and the effective federal rate ends up around 6%-8%, which is lower than what most American working-class folks pay.

OK so the picture sharpens. Billionaire moves do not transfer cleanly, but F-1 has its own little gold seam.

The story could have ended there, but I wanted to push one more step. Could a student-sized account at IBKR even run a miniature Buy Borrow Die loop, buy assets, borrow against them via margin or something fancier like a Box Spread, reinvest the proceeds, and let it compound?

Gemini's first answer was textbook. Buy VOO, lever it 1.3x with margin, then run a Box Spread on XSP (mini SPX) to drop the financing cost. The moment I read that I felt something was off, so I pushed for one more layer down.

There were two pits underneath.

The first pit is the Portfolio Margin threshold. The reason billionaires can lever so aggressively at IBKR is that they sit on Portfolio Margin, an advanced collateral mode that IBKR opens up to accounts above 110k USD. For low-volatility assets like VOO, the margin requirement under PM can drop to roughly 15%, which is a different universe. A student account is nowhere near that gate, not even close. What you are stuck with is regular Reg-T margin, where overnight leverage caps at 2x, and a 10% drop in VOO eats a big chunk of your buffer immediately. A small-base account running 1.5x leverage gets shaken out the moment the market hiccups.

The second pit is sneakier, it is the liquidity of the XSP Box Spread. The whole point of a Box Spread is that the implied financing cost sits very close to the risk-free rate, but only if you can actually transact at fair value. SPX itself has plenty of liquidity, but one contract is notional 500k, way out of my league. XSP is the mini version, notional one tenth of that, which sounds friendlier, but the bid-ask spread is much wider. You think you locked in 4.5% borrowing cost, in reality slippage drags it up to 6%, which is essentially what IBKR's official margin rate would have been anyway. At that point the whole exercise is just cosplay.

So what now. Gemini handed me a tool I had genuinely never heard of, called NTSX, full name WisdomTree US Efficient Core. The internal structure is clever. It puts roughly 90% of the assets into the U.S. equity market, then uses Treasury futures to layer on a 60% bond exposure, so the total exposure works out to about 1.5x, but because the futures position itself does not pay interest (only roll cost, around 50 bps annualized), it is essentially handing you a 1.5x leverage for free.

This was the biggest find of the whole night.

Think about it. If I borrow on IBKR margin and buy VOO, I am paying 5%-6% to do it. If I run a Box Spread, I am wrestling with liquidity, slippage, and rolling at expiry. But if I just buy NTSX, I do nothing, and I get 1.5x equity-plus-bond exposure with no margin call risk and no interest cost.

That one stunned me into silence for a moment. Turns out at my capital level, you do not need fancy financial engineering, the market has already packaged the tool for you, most people just have not heard of it.

Back to the loop itself. I asked Gemini one more time, can F-1 actually close the Buy Borrow Die loop. The answer was one I had not seen coming. In theory the first two steps (Buy and Borrow) are doable, but the Die step has a fatal bug for F-1.

For U.S. citizens and green card holders, the federal estate tax exemption sits around 13 million USD, so the last mile of Buy Borrow Die is essentially tax-free for almost everyone in this strategy. For Non-Resident Aliens like an F-1 student, the exemption on U.S.-situs assets (which includes U.S. stocks) is only 60,000 USD. Anything above that gets taxed at 40%.

So if I am still on F-1 and I have, say, 1 million USD in VOO, and something happens to me, the government takes 40% of the 940k that exceeds the 60k exemption.

That moment was a little cold. A loop that looks airtight for billionaires snaps clean off at the last step for F-1.

Gemini also offered the patches. Either you eventually move to H1B, green card, or citizenship, joining the Resident Alien tax universe. Or you set up an offshore vehicle in BVI or Cayman to hold U.S. equities, which makes the assets non-U.S.-situs and out of reach of U.S. estate tax. The second one is the standard playbook for top-tier NRA billionaires, but the maintenance cost is heavy and clearly overkill for someone in a PhD.

That is when it clicked for me. Buy Borrow Die is not really a financial maneuver at the bone, it is a status dividend. You have to be a citizen or long-term resident to fully eat the last and biggest chunk of the loop. What an F-1 student can actually do is run the first two steps, accumulate position, and prepare for the day the green card or status conversion lands.

So the takeaway from this back-and-forth with Gemini is not a cut-and-paste billionaire script, it is a much sharper read of where I actually stand.

Here is the F-1 list I came out with.

One, max out the float window on every 0% APR card I have. This is legal, stable, near-zero-risk debt. Whatever modest cash flow a student does have can sit in IBKR money market funds at 5%, daily expenses run on the credit cards, and I deal with payoff before the promo expires.

Two, on the asset side, NTSX as the base layer. Built-in 1.5x exposure, no financing cost, no margin call risk, the cleanest math at my capital level. Once net liquidity crosses 110k USD, then I can revisit Portfolio Margin and SPX Box Spread.

Three, every tax season, fully use the 5,000 USD federal exemption from Article 20(c) of the US-China Tax Treaty. Run the checklist before filing.

Four, never open an LLC just to run a Section 179 deduction on a vehicle. That is trading future status for pocket change.

Five, hackathons and bank account bonuses are the only legal fast cash channels for F-1. Climate-plus-AI hackathons especially are basically a free hit at my background, a weekend can land a few thousand. Chase, Wells Fargo, that kind of deposit bonus stacks up to 1k-2k a year, almost free money.

Six, the long game is status conversion. If I am not heading back to China, I need a clear H1B and green card plan. The last mile of Buy Borrow Die is gated to local residents, and that gate is the actual ticket to the ride.

I keep coming back to one framing. The world the rich live in is not built on income, it is built on assets and debt. The financial model of a regular person looks like Income → Tax → Savings. The financial model of the rich looks like Asset → Debt → Spending. The river of taxes runs in the middle, and the rich cross it on a bridge made of assets, while everyone else wades through.

F-1 students are standing in the middle of the river, the bridge half-built, the far bank still some distance off. But you can at least see what the bridge looks like, how it gets built, and how long it takes.

I did not get richer this evening. But I got a real, three-dimensional read on where I actually sit in the world as a student and a regular person. And honestly, that feels more solid than making the money would have.
