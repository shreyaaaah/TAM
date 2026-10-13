# TAM / Implementation Intern case study: seating 2,000 people on a 3-day week

Case for WorkInSync (MoveInSync): a facility manager runs 3 offices in 3 countries, 2,000 people need seats, and employees come in 3 days a week. How many seats at minimum and maximum, and which KPIs show whether the facilities team is doing a good job?

## Start here

| File | What it is |
| --- | --- |
| [Seating_Case_Study_WorkInSync.pdf](Seating_Case_Study_WorkInSync.pdf) | The full solution (submission copy) |
| [Seating_Case_Study_WorkInSync.docx](Seating_Case_Study_WorkInSync.docx) | Same document in Word |
| [case_study.md](case_study.md) | Same document as readable text on GitHub |
| [calculations/seat_model.py](calculations/seat_model.py) | Script that re-checks every number in the solution |
| [calculations/seat_model_output.txt](calculations/seat_model_output.txt) | Output of that script |
| [data_request_checklist.md](data_request_checklist.md) | What I would ask the client, and what data replaces each assumption |

## The answer in brief

- **Minimum: 1,200 seats.** The week needs 2,000 x 3 = 6,000 attended seat-days over 5 days, so the average day has 1,200 people, and the busiest day is never below the average. Reachable with a rotation where each day is exactly 60% of headcount.
- **Maximum: 2,000 seats.** Everyone picks the same three days.
- **Planning number: 1,200 x k**, where k = busiest-day attendance / average-day attendance. Each 0.1 of k is 120 seats company-wide. k is a policy I set with day menus and daily caps, then measure. 1.3 (1,560 seats) is only a placeholder until data arrives.
- **Three offices** are planned separately with the same formula, because seats cannot be shared across countries. Holiday weeks are handled by a rule or flexible space, not by buying seats.
- **Six KPIs, read in pairs:** seat-denied rate, peak occupancy, average utilisation, no-show rate, team co-location rate, cost per attended person-day. Each has a formula, a purpose and a note on how it can be misread.
- **Operational insight:** check-in data only records people who got a seat, so unmet demand must be logged separately or capacity decisions will shrink supply further.

## What is proven and what is assumed

Proven from the case alone: the 1,200 floor and the 2,000 ceiling. Assumed or made up for illustration: k = 1.3, the 1,000 / 600 / 400 office split, and the 3% and 7% buffers (calculated under independent attendance). The solution lists what data would replace each one.

## Run the numbers

```
python3 calculations/seat_model.py
```

Standard library only.
