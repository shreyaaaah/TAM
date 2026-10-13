# Seating 2,000 People on a 3-Day Week: A Seat-Day Approach

*Case study: Technical Account Manager / Implementation Intern, WorkInSync*


# Short answer

Across the three offices, the fewest seats that can work is 1,200 and the most anyone could ever need is 2,000. The number I would actually plan for sits between them and depends on one thing a facility manager can influence: how evenly people spread over the five working days.

- **Minimum: 1,200 seats.** Proven, but only if attendance is perfectly even every day.
- **Maximum: 2,000 seats.** Proven, and it happens if everyone picks the same three days.
- **Planning number: 1,200 × k**, where k is the busiest day's attendance divided by the average day's attendance. I treat k as a policy I choose and then measure, not a number I guess.

Until real data exists, I would use k = 1.3 (1,560 seats) as a labelled placeholder, keep some flexible space in reserve, and let measured data replace it.

# How I framed the problem: count seat-days, not seats

A seat is capacity for five days a week, so I compare weekly demand with weekly supply. Demand is 2,000 people × 3 days = 6,000 attended seat-days. Supply is the number of seats × 5 days.

That gives a simple link between seats and average utilisation:

> average utilisation = 6,000 ÷ (5 × seats) = 1,200 ÷ seats

With 1,200 seats the average utilisation is 100%. With 1,600 seats it is 75%. With 2,000 seats it is 60%. So no seat count can hide how much space is empty on an average day.

The same seats can be judged from two sides. On the busiest day the question is whether everyone can sit. Across the whole week the question is how many desks sit empty. The gap between the two views is one number, k:

> average utilisation = peak utilisation ÷ k, where k = busiest-day attendance ÷ average-day attendance

I use k throughout because it turns a vague question ("how many seats?") into a decision about how concentrated attendance is allowed to be.

# Minimum: 1,200 seats is a floor, not a target

**Why it is a floor.** The five days of the week must together cover 6,000 attended seat-days, so the average day has 1,200 people. The busiest day is never below the average. With fewer than 1,200 seats, at least one day has someone standing. This argument needs no assumption about how people are spread. It only needs that everyone attends exactly three days.

**Why it can be reached.** Put people in groups of five and number the days 1 to 5. Person i in each group attends days i, i+1 and i+2 (wrapping around after day 5). Every day is then covered by exactly 3 of the 5 people, so each day is 60% of headcount.

**Three offices.** Seats cannot be shared across countries, so the floor holds for each office separately: seats in office o must be at least 3 × H<sub>o</sub> ÷ 5, rounded up. Rounding adds under one seat per office, so the total floor is 1,200 to 1,202.

**Why I would not build exactly 1,200.** Every seat is then full on every day. One person swapping a day, one team meeting moved, or one holiday week and somebody has no seat. The floor tells me the best case, not what to buy.

# Maximum: 2,000 seats is the ceiling, and nobody should build it

If all 2,000 people choose the same three days, for example Tuesday to Thursday, each of those days needs 2,000 seats and the other two days are empty. Here k = 2,000 ÷ 1,200 ≈ 1.67. Nobody can need more than the headcount, so 2,000 is the upper bound for this case.

I would not build it, because average utilisation would be 60%, meaning 40% of seat-days empty. And the ceiling is not a fixed fact. It is what happens when no one manages the day spread. A daily cap per office turns the ceiling into a chosen number.

The bound only holds while headcount is 2,000. Visitors, contractors, new joiners and growth are not in the case, so I would ask the client whether to add them.

# What sets the number in between: the peak factor k

Seats follow directly from k. H is headcount, d is in-office days (3) and w is working days (5):

> seats = H × (d ÷ w) × k

The table shows how the same 2,000 people need very different seat counts depending on k. The k values are scenarios I chose to show the range, not findings.

| k (illustrative) | Busiest day as % of headcount | Seats needed | Average utilisation |
|:---|:---|:---|:---|
| 1.00 | 60% | 1,200 | 100% |
| 1.20 | 72% | 1,440 | 83% |
| 1.33 | 80% | 1,600 | 75% |
| 1.50 | 90% | 1,800 | 67% |
| 1.67 | 100% | 2,000 | 60% |

Every 0.1 of k is worth 120 seats across the company (1,200 × 0.1). That is the trade-off I would show a client: the less we control the day spread, the more seats we pay for.

**Randomness is the smaller risk.** Suppose each person independently comes in with probability 0.6 on a given day. For 2,000 people the standard deviation of daily headcount is √(2,000 × 0.6 × 0.4) ≈ 22. Planning for the 95th-percentile day adds about 1.645 × 22 ≈ 36 seats, roughly 3%. In reality teams move together, so attendance is not independent and the true buffer is larger. This is why clustering (k) matters more than random variation, and why I would take the buffer from observed data.

**How I would set k.** Give each team a short menu of day combinations, and set a daily cap per office. The cap is both the policy and the seat count: a cap of 80% of headcount means 1,600 seats. After a few weeks of check-in and "no seat found" data, I would revise the cap.

# Planning the three offices independently

The case does not say how the 2,000 people are split, how big each office is, or what the local holidays are. So I plan each office on its own with the same formula, and fill in the unknowns as data arrives:

> seats<sub>o</sub> = H<sub>o</sub> × (3 ÷ w<sub>o</sub>) × k<sub>o</sub>

The total floor stays 1,200 whatever the split, because 0.6 × H<sub>o</sub> adds up to 0.6 × 2,000. What changes by office:

- **Own k.** A sales-heavy office and an engineering office will not spread across the week the same way.
- **Own working week.** Weekends and public holidays differ by country, so w<sub>o</sub> differs, and seats cannot move between countries to cover the gaps.
- **Holiday weeks.** If the 3-day expectation stays but the week has 4 working days, average attendance goes from 60% to 75% of headcount that week. I would not buy seats for that week. I would handle it with a rule (a lower in-office expectation or a cap) or short-term flexible space, and I would confirm with the client which they prefer.
- **Smaller offices need a proportionally bigger buffer.** Under the same independence assumption as before, the 95th-percentile buffer is about 3% for 2,000 people but about 7% for a 400-person office (1.645 × √(400 × 0.6 × 0.4) ≈ 16 seats on 240).
- **Unknown split.** The headcount by site is the first thing I would ask for, because HR knows it immediately. Until it arrives I would give the formula per office and commit only to the floor 0.6 × H<sub>o</sub>.

**Example with made-up numbers, to show the method:** headcount 1,000 / 600 / 400 and k = 1.2 / 1.3 / 1.4 gives 720 + 468 + 336 = 1,524 seats. None of these inputs come from the case.

# Operating model: match each fix to its speed, and agree the triggers early

My feedback loop has four levers, and they work on very different timescales. Mixing them up is how teams end up moving walls to fix a problem that a booking rule would have solved.

| Lever | How fast it acts | What it changes | Cost of using it |
|:---|:---|:---|:---|
| Release seats not checked in | Same day | Usable supply | Almost none |
| Team day menus and daily caps | 1 to 2 weeks | k (how concentrated the days are) | Less freedom for teams |
| Team zones and seat types | Quarterly | Whether people sit near their team | Moving people and equipment |
| Seat count and flexible space contracts | Months, tied to lease terms | Total supply | High |

I would use the fastest lever that fixes the problem and move to a slower one only when the problem repeats.

**Release timing matters.** A seat released at 10:30 does little for someone who decided at 8:30 to work from home. The release time should come from data on when people actually book, not from a round number.

**Agree triggers before the data arrives.** For example: if the seat-denied rate stays above an agreed threshold for several weeks, raise the cap or add flexible space; if average utilisation stays below an agreed threshold while seat-denied is near zero, give back seats at the next lease decision. The thresholds and the number of weeks are the client's decision. I would propose starting values with reasoning, mark them as placeholders, and agree them in the first meeting. Doing this early stops later debates about what the numbers mean.

**Overbooking** (accepting more bookings than seats) is only safe once the no-show rate has been measured for each office. I would not start with it.

**My role as a technical account manager** would be to get the data request out in the first week, agree KPI definitions in writing, check what the booking tool can and cannot log, and run a short review every month. I have not verified what any specific product logs, so that is a question for the client's tool and not an assumption.

# KPIs: six measures, always read in pairs

No single KPI is trustworthy alone, because each one can be improved at another's expense. I set targets only after a baseline period, and I treat occupancy as a healthy band, not a number to maximise.

| KPI | Formula | Purpose | How it can be misread |
|:-----|:--------------|:-----------|:---------------|
| 1. Seat-denied rate | People who wanted a suitable seat on a day and could not get one ÷ people who wanted a seat that day | The only measure that sees overcrowding and unmet demand (employee experience) | People give up trying, so it undercounts. Count unique people per day, and log failed searches and "no seat" reports. |
| 2. Peak occupancy | People present in the busiest hour ÷ usable seats, taken on a typical busy day (for example the 90th-percentile day) | Shows whether people could sit comfortably (employee experience) | Near 100% looks efficient but leaves no slack. Judge it against KPI 1. |
| 3. Average utilisation | Attended seat-days ÷ available seat-days | Shows how much of the space paid for is used (cost) | Low does not always mean waste, since some spare capacity is what makes booking flexible. It equals peak utilisation ÷ k, so read it with KPI 2. |
| 4. No-show rate | Bookings not checked in by the release time ÷ all bookings | Shows wasted capacity and whether overbooking would be safe (cost) | A high rate can mean people book "just in case" because they fear not finding a seat, which is really a KPI 1 problem. |
| 5. Team co-location rate | Team in-office days on which present team members sit in the same zone ÷ team in-office days (zone definition agreed with the client) | Shows whether the office is serving the reason people come in (employee experience) | Needs clean team data, and not every team benefits from sitting together. |
| 6. Cost per attended person-day | Total seat-related cost in a period (rent, services, flexible space) ÷ attended person-days | Shows cost efficiency over time (cost) | It falls when seats are cut, even if KPI 1 gets worse. Compare an office with its own past, not across countries with different rents. |

KPIs 1, 2 and 5 describe the employee's experience. KPIs 3 and 6 describe cost. KPI 4 sits between them. I would add a short pulse question to employees ("Could I work effectively on my office days?") because numbers miss things like noise or a seat far from the team.

# An operational insight: check-in data only shows people who got a seat

Attendance data records who sat down. It cannot record who wanted to come and could not. If seats are tight, some people quietly work from home or move to another day, and the numbers still look healthy.

**Illustration with made-up numbers.** Suppose an office has 1,200 seats and 1,350 people want one on the busiest day. Check-ins show 1,200, which is 100% utilisation and looks perfectly efficient. In truth 150 people (about 11%) were turned away. Some of them then stay home the next week, recorded demand falls, and a loop that sets capacity from check-ins concludes there are too many seats. Capacity shrinks and more demand is hidden.

**What I would do.** Record wanted-but-failed seat searches, waitlist requests and "no seat" reports as data in their own right, and base capacity decisions on wanted seats, not attended seats. If the booking tool cannot log failed searches, a one-question prompt when someone cancels or gives up would be enough to start.

I chose this because it affects every number in this document, and because it can be fixed cheaply.

# What is proven, what is assumed, and what data would replace it

| Statement | Status | What would replace it |
|:--------------|:-------------------|:------------------------|
| Minimum is 1,200 seats | Proven, if everyone attends exactly 3 days of a 5-day week | Actual attendance rules and leave patterns |
| Maximum is 2,000 seats | Proven, while headcount is 2,000 | Visitors, contractors and growth plans |
| Seats = 1,200 × k | Proven algebra, but k is unknown | Measured k per office |
| k = 1.3 as a starting point | Assumption, a placeholder only | 8 to 12 weeks of check-in and booking data by office |
| About 3% and 7% random buffer | Calculated under independent attendance | Observed day-to-day variation, which will be larger because teams move together |
| 1,000 / 600 / 400 split | Made up for the example | Headcount by site from HR |
| Holiday-week effect | Arithmetic on a 4-day week | Each country's holiday calendar and the client's holiday policy |
