"""Seat-planning model for the WorkInSync case study.

Re-checks every number used in the write-up. Run: python3 seat_model.py
Only the standard library is needed.
"""
import math

HEADCOUNT = 2000
DAYS_IN_OFFICE = 3
WORKING_DAYS = 5


def floor_seats(headcount, d=DAYS_IN_OFFICE, w=WORKING_DAYS):
    """Fewest seats that can work: average daily attendance, rounded up."""
    return math.ceil(headcount * d / w)


def seats_for_k(headcount, k, d=DAYS_IN_OFFICE, w=WORKING_DAYS):
    """Seats = H x (d / w) x k, where k = busiest day / average day."""
    return headcount * d / w * k


def rotation_check(group_size=5, d=3):
    """Person i attends days i, i+1, i+2 (mod 5). Count people per day."""
    per_day = [0] * group_size
    for person in range(group_size):
        for step in range(d):
            per_day[(person + step) % group_size] += 1
    return per_day


def random_buffer(headcount, p=0.6, z=1.645):
    """95th-percentile extra seats if attendance is independent (binomial)."""
    sd = math.sqrt(headcount * p * (1 - p))
    return sd, z * sd


print("1. Minimum and maximum")
print("   floor =", floor_seats(HEADCOUNT), "seats")
k_max = HEADCOUNT / floor_seats(HEADCOUNT)
print(f"   max = {HEADCOUNT} seats, k = {k_max:.2f}")

print("\n2. Rotation proof (people per day in a group of 5):", rotation_check())

print("\n3. Scenario table (k values are illustrative)")
print("   k      peak%   seats   avg utilisation")
for k in (1.0, 1.2, 4 / 3, 1.5, 5 / 3):
    seats = seats_for_k(HEADCOUNT, k)
    print(f"   {k:.2f}   {0.6 * k:5.0%}   {seats:5.0f}   {1 / k:5.0%}")
print("   seats per 0.1 of k:", round(seats_for_k(HEADCOUNT, 0.1)))

print("\n4. Random buffer, independent attendance (p = 0.6)")
for h in (2000, 400):
    sd, extra = random_buffer(h)
    print(f"   H={h}: sd={sd:.1f}, extra={extra:.1f} seats = {extra / (0.6 * h):.1%} of average")

print("\n5. Holiday week: 3 days in a 4-day week =", f"{3 / 4:.0%}", "of headcount (vs 60%)")

print("\n6. Made-up three-office example")
offices = {"A": (1000, 1.2), "B": (600, 1.3), "C": (400, 1.4)}
total = 0
for name, (h, k) in offices.items():
    s = seats_for_k(h, k)
    total += s
    print(f"   {name}: H={h}, k={k} -> {s:.0f} seats")
print("   total =", round(total))

print("\n7. Censored demand illustration (made-up)")
seats, wanted = 1200, 1350
print(f"   check-ins={seats} (100% utilisation), turned away={wanted - seats} ({(wanted - seats) / wanted:.0%} of those who wanted a seat)")
