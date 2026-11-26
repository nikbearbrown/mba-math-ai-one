# 5. Screen plans before ranking them

*“Best” has no numerical meaning until the plan fits and the score is named.*

The repair service must choose A or B before it sees next month's demand. The shop's constraint is at least $150 operating profit in the low scenario. Its objective is expected operating profit among plans that pass. A passes at $180. B fails at $90. Select A among these two candidates under that rule. This is enumerating a finite feasible set, not solving a continuous optimization problem.

## Find the point at which the advice would change

In the low and middle scenarios, both plans serve the same number, so B earns $90 less than A. In the high scenario it handles 40 extra bookings. At $12 contribution each and $90 extra fixed cost, B earns $390 more. Let h be the probability of high demand. With the low probability fixed at 0.25 and the remaining 0.75−h assigned to middle demand, the expected difference is:

`E[B−A] = −90(1−h) + 390h = −90 + 480h`.

The expected values tie at h = 90/480 = 0.1875, within the allowable range 0 ≤ h ≤ 0.75. At h = 0.25 the difference is $30. This does not make B feasible under the low-scenario floor, which does not depend on h here. If the manager instead changes the floor to $90, both plans pass under an inclusive rule, and B wins at the baseline weights.

## Write the recommendation another person can test

Lead with the constraint and action, then give the number that supports it. “Select A under a $150 low-month floor. As modeled A earns $180 in that scenario; B earns $90. B leads by $30 in expected operating profit before screening. I would revisit if the floor or B's fixed cost changes.” Say where the assumptions live. The financing calculation is a separate illustration; combining it would require a clearly dated cash-flow model rather than subtracting a three-month loan balance from one month's operating profit.

Before presenting, test one alternate input where you know the direction of the result. If A's capacity rises to 130 at the same fixed cost, only the high row changes and expected A profit rises by 0.25×10×$12 = $30. If every row moves, inspect the model rather than accepting the dashboard.

Complete the [planning worksheet](../practice/planning-worksheet.md) before looking at the [key](../practice/answer-key.md). Then carry the logic to the separate transfer item without feedback.
