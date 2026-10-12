import json, math

def jsnum(x):
    return int(x) if isinstance(x, float) and x == int(x) else x
def plural(n, word, form=None): return str(jsnum(n)) + " " + (word if n == 1 else (form or word + "s"))
def money(c): return "$" + str(c // 100) + "." + str(c % 100).zfill(2)
def fmt(x): return str(jsnum(x))
def rnd(x): return math.floor(x + 0.5)

def pile_plan(items, minutesPerItem):
    if not (items > 0) or not (minutesPerItem > 0):
        return {"error": "items and minutes must be positive"}
    minutes = items * minutesPerItem
    return {"minutes": minutes, "hours": jsnum(rnd(minutes / 60 * 10) / 10)}

def energy_plan(watts, minutes, pricePerKwh, sessionsPerWeek):
    if not (watts > 0) or not (minutes > 0) or not (pricePerKwh > 0) or not (sessionsPerWeek > 0):
        return {"error": "watts, minutes, price and sessions must be positive"}
    kwh = jsnum(watts * minutes / 60 / 1000)
    return {"kwh": kwh, "sessionCents": rnd(kwh * pricePerKwh * 100),
            "yearCents": rnd(kwh * sessionsPerWeek * 52 * pricePerKwh * 100),
            "priceCents": rnd(pricePerKwh * 100)}

def schedule_plan(totalMinutes, sessionMinutes, sessionsPerWeek):
    if not (totalMinutes > 0) or not (sessionMinutes > 0) or not (sessionsPerWeek > 0):
        return {"error": "minutes and sessions must be positive"}
    sessions = math.ceil(totalMinutes / sessionMinutes)
    return {"sessions": sessions, "weeks": math.ceil(sessions / sessionsPerWeek)}

def render_pile(r, items, minutesPerItem):
    return (plural(items, "item") + " at a labeled " + fmt(minutesPerItem) + " minutes each: " + fmt(r["minutes"])
            + " minutes at the board - " + plural(r["hours"], "hour") + " of ironing.")

def render_energy(r, watts, minutes, pricePerKwh, sessionsPerWeek):
    return ("A " + fmt(watts) + " W iron for " + fmt(minutes) + " minutes uses " + fmt(r["kwh"]) + " kWh: "
            + money(r["sessionCents"]) + " a session at " + money(r["priceCents"]) + " a kWh, " + money(r["yearCents"])
            + " a year at " + plural(sessionsPerWeek, "session") + " a week.")

def render_schedule(r, totalMinutes, sessionMinutes, sessionsPerWeek):
    return (plural(totalMinutes, "minute") + " of pile in " + fmt(sessionMinutes) + "-minute sessions: "
            + plural(r["sessions"], "session") + ", cleared in " + plural(r["weeks"], "week") + " at "
            + plural(sessionsPerWeek, "session") + " a week.")

cases = []
for a in [(15, 5), (22, 4), (10, 6), (0, 5)]:
    r = pile_plan(*a)
    cases.append({"fn": "pilePlan", "args": list(a), "result": r,
                  "render": None if "error" in r else render_pile(r, *a)})
for a in [(2000, 45, 0.15, 1), (2400, 30, 0.22, 2), (1800, 60, 0.18, 1), (0, 45, 0.15, 1)]:
    r = energy_plan(*a)
    cases.append({"fn": "energyPlan", "args": list(a), "result": r,
                  "render": None if "error" in r else render_energy(r, *a)})
for a in [(75, 30, 1), (88, 45, 2), (60, 20, 3), (0, 30, 1)]:
    r = schedule_plan(*a)
    cases.append({"fn": "schedulePlan", "args": list(a), "result": r,
                  "render": None if "error" in r else render_schedule(r, *a)})

with open("expected.json", "w") as f:
    f.write(json.dumps(cases, separators=(",", ":")) + "\n")
print("wrote", len(cases), "cases")
