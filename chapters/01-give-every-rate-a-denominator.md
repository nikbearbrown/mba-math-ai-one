# 1. Give every rate a denominator

*Two reports can both be correct and still disagree about what you should plan for.*

Imagine a van-based repair service making its first monthly capacity plan. It has one line of input: “5.5 requests daily.” Before drawing a revenue line, ask what a day means. The team is open 20 days in the modeled month. The rate is per **operating** day, not per calendar day. That makes the middle scenario 110 requests, not 165.

This compact course assumes basic arithmetic and the ability to read a table. By the end you can build a simple operating model, test a plausible but wrong result, and explain the assumptions that could change your recommendation. The company and all figures are invented.

## Let the units do part of the work

Write the operation before reaching for a calculator:

`5.5 requests / operating day × 20 operating days / month = 110 requests / month`.

The operating-day unit cancels. If the input instead says 5.5 per calendar day, it describes a different process. If it was measured only on busy days, neither monthly estimate is justified without another assumption.

Our three monthly scenarios have rates of 4.5, 5.5 and 8.5, giving 90, 110 and 170 requests. These rates summarize the whole operating month under each scenario. A value of 5.5 does not imply half a booking arrived on a particular day. For this first model, treat all requests as interchangeable, fulfill them in the same month if capacity permits, and assume no carryover. Note the omission: we do not model a Tuesday rush that might exceed daily capacity while monthly capacity is spare. If daily peaks matter, replace this monthly capacity assumption rather than promising it can handle any schedule.

## Changing the denominator changes the story

At a capacity of 120 with demand of 170, 50 requests are not served. That is about 29.4% of demand, using 170 as the denominator. Calling it a 41.7% shortfall uses 120 as the base. Both quotients measure something, but only the first is the share of requests unserved.

Percent and percentage points also answer different questions. A fulfillment rate moving from 60% to 75% rises 15 percentage points, or 25% relative to its old rate: (75−60)/60. State the base if readers might mistake a relative change for a difference between rates.

**Try it unaided.** If the shop is open 18 days and the rate is 6.5 requests per operating day, what is monthly demand? If 100 of those requests are served, give a fulfillment rate and name its denominator. Keep those units when you build the margin model.
