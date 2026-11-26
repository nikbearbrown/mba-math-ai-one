# 2. Find the break-even booking

*A rate of twelve dollars per booking can pay a fixed bill. It cannot pay it before the bookings happen.*

The fictional repair service charges $28 per fulfilled booking and uses $16 of variable expense for each. Before the first booking, however, it owes the plan's monthly fixed cost. You can read this as two lines: revenue starts at zero and rises by $28 per booking. Operating cost starts at the fixed amount and rises by $16. The intersection is where the lines meet.

## Derive the contribution instead of memorizing it

Let q be the whole number of bookings fulfilled in a month. Let F be monthly fixed cost in dollars. Then revenue is 28q, operating cost is F + 16q, and operating profit is:

`π(q) = 28q − (F + 16q) = 12q − F`.

The slope is $12 per fulfilled booking, not a monthly dollar amount. Each additional booking contributes that amount toward fixed cost until the fixed cost is covered. Afterward it adds $12 to operating profit, given constant price and per-booking cost.

Plan A has F = $900 and up to 120 bookings. With q = 75 its revenue and cost both equal $2,100. Plan B has F = $990 and capacity 160. Its lines cross at q = 82.5, which is not an operational outcome. At 82 bookings B earns −$6; at 83 it earns $6. Thus 83 is the first whole booking count with nonnegative profit, not an integer point of exact equality. Rounding 82.5 down would accept a loss.

## Put capacity where it acts

For demand D and capacity C, q = min(D,C). In the high scenario the service expects 170 requests. A serves 120 and earns $540; B serves 160 and earns $930. Do not plug all demand into the revenue line while limiting only costs. The same fulfilled count controls both.

At zero bookings the model gives −F. If someone changes the assumptions so contribution is zero, no positive booking count can cover positive fixed cost; a formula that divides by the contribution is not valid there. Likewise, a computed break-even above capacity is unreachable for that plan, even if the formula returns a number.

**Try it unaided.** Check whether a plan with a $1,000 fixed cost and the same $12 contribution can break even at capacity 80. Give the fractional crossing, the first whole booking count with nonnegative profit, and the result at capacity.
