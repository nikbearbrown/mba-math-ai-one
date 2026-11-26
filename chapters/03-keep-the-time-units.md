# 3. Keep the time units

*The balance charged interest this month may not be the balance borrowed last month.*

Suppose, as a **separate financing comparison**, the service team tests what would be due on an initial $990 balance over three months at 1% per month, with no interim payments or fees. This is not a line in the operating-profit forecast. It is a small way to see what changes when the interest itself begins earning interest.

## Two rules, two bases

At simple interest the monthly charge is always $9.90, because 1% of the original $990 is $9.90. Three such increments leave $1,019.70 due. With principal P, rate r per period and n periods, the formula is P(1 + nr).

At monthly compounding the new balance becomes the next month's base: multiply by 1.01 once, then again, then again. In general the result is P(1 + r)^n.

| Month | Simple balance | Compounded balance, displayed to cents |
| --- | ---: | ---: |
| 0 | $990.00 | $990.00 |
| 1 | $999.90 | $999.90 |
| 2 | $1,009.80 | $1,009.90 |
| 3 | $1,019.70 | $1,020.00 |

The compound computation before rounding is $1,019.99799. The table displays to cents; it does not round and reinvest each intermediate display. A real contract could round at each billing period. Read its terms instead of assuming the displayed method.

## Test an easy limit

At n = 0 both rules give P. At n = 1 both rules give P(1+r). They diverge only when a later period can act on earlier interest. When r = 0, neither rule changes the balance. These checks catch a missing initial balance or an exponent off by one.

A monthly rate requires a monthly period count. Even when 12 × 1% = 12%, the annualized effective growth from monthly compounding is (1.01)^12−1, about 12.68%, under the same constant-rate assumption. That is not a claim about any loan's disclosed APR, fees, or availability. If payments arrive before the end or the rate floats, update the balance and rate period by period.

**Try it unaided.** On a synthetic $500 balance at 2% per month and no cash flows, calculate the amount due after two months under both rules. Explain why the difference appears only in the second month.
