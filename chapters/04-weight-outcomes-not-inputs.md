# 4. Weight the outcomes, not the inputs

*An average month can be absent from your forecast and still sneak into your spreadsheet.*

The repair service has three scenarios. Give low, middle and high weights of 0.25, 0.50 and 0.25. They are subjective planning assumptions for mutually exclusive, exhaustive scenarios in this exercise, not forecasts validated on historical data. Expected value across them is the sum of probability times outcome.

| Monthly demand D | Probability | A fulfilled | A profit | B fulfilled | B profit |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 90 | 0.25 | 90 | $180 | 90 | $90 |
| 110 | 0.50 | 110 | $420 | 110 | $330 |
| 170 | 0.25 | 120 | $540 | 160 | $930 |

A's expected profit is 0.25×180 + 0.50×420 + 0.25×540 = $390. B's is $420. Neither mean has to match a realized month's profit. A decision maker who ranks solely by expected monthly operating profit picks B, given these inputs.

## Catch the tempting shortcut

The weighted demand is 120. Put that demand into the formula for both plans and you get A $540, B $450. This answer picks A. The arithmetic is internally consistent, but it answers a different question: how does each plan perform if demand is exactly 120?

Capacity changes the slope of the profit curve. Below it, an extra request can add $12. Above it, the extra request adds zero in this model. A's expected fulfilled count is 107.5, computed as 0.25×90 + 0.50×110 + 0.25×120; it is not 120. You may weight fulfilled counts and then use the linear profit rule, because the rule is linear in that already-capped count. You may not usually average demand before capping it. The same issue appears in overtime thresholds, rate tiers and inventory shortages.

## Price the downside separately

Under B the low scenario yields $90. Under A it yields $180. With a $150 minimum in any modeled scenario, A falls below the floor in none of them; B falls below in the low one, with modeled probability 0.25. A floor is a constraint, not a second estimate of expected profit. If the scenario list omits a disruption, the calculated probability is not protection from it.

**Try it unaided.** Replace the high probability with 0.20 and the middle with 0.55. Leave the low fixed. Recompute the expected difference by weighting B minus A in each row. Compare that result to the previous $30 advantage without touching the capacity cells.
