# One-month service plan

All inputs are fictional. Read [the case data](../examples/case.json) or use the tables here. No software account is needed.

| Input | Value |
| --- | ---: |
| Operating days per month | 20 |
| Revenue per fulfilled booking | $28 |
| Variable expense per fulfilled booking | $16 |
| Plan A | 120 bookings/month, $900 fixed/month |
| Plan B | 160 bookings/month, $990 fixed/month |
| Minimum low-scenario operating profit | $150 |

| Scenario | Requests per operating day | Probability |
| --- | ---: | ---: |
| Low | 4.5 | 0.25 |
| Middle | 5.5 | 0.50 |
| High | 8.5 | 0.25 |

## First attempt: no tool feedback

1. Convert the rates to monthly demand with units and give weighted demand. In the high scenario, what fraction of requests can Plan B not serve?
2. Write revenue, operating cost, operating profit, and fulfilled-booking formulas. For each plan, check the break-even result by substituting whole bookings.
3. Build the six operating-profit results. Report each plan's expected profit. Compare with the result of substituting mean demand into each plan's formula. Explain why, without claiming one calculation is inherently invalid.
4. Screen with the $150 floor and choose. Then lift the floor and find the high-demand probability that ties expected profits with the low probability fixed at 0.25. Name an assumption that would move that threshold.
5. In a separate block, compare simple and monthly compound interest on $990 over three months at 1% per month. Record unrounded balances and then round to cents. Do not combine this with the operating-profit comparison.
6. Write a four-sentence decision memo with a constraint, a recommendation, an independent numeric check, and one input that could change the recommendation.

## Revise and disclose

Use the key or ask a model to inspect only the synthetic case and your draft. Give it one bounded task: “Look for a denominator or capacity error. Pick one row and show a counterexample by substitution. Leave the recommendation to me.” Rerun the arithmetic from the inputs, regardless of whether the suggestion agrees with you. For a paper-only route, substitute demand zero and then demand above capacity and compare against your rule.

Record the first claim, your check, the change you accepted or rejected, and whether you used the answer key or an AI tool. If you used a tool, name it and state its role. Follow instructor rules and do not use a tool on the first attempt or transfer.

## Unaided transfer: studio rentals

A fictional studio earns $8 contribution per completed rental. Policy C has capacity 10 and fixed cost $80. Policy D has capacity 16 and fixed cost $112. Demand is 10 with probability 0.25 and 18 with probability 0.75. Assume the same monthly accounting and no carryover. Without a tool or the key, give each expected operating profit and select under a nonnegative low-month floor. State what you would choose if the floor were removed. Validate one result by substitution.
