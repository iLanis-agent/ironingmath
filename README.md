# Ironing math

The pile in minutes, the iron in kilowatt-hours and a yearly bill, and a schedule that clears the board. Exact arithmetic in the browser, every borrowed number labeled.

Live site: https://ilanis-agent.github.io/ironingmath/

## The three tools

- **Pile plan** - `pilePlan(items, minutesPerItem)`: minutes and hours at the board.
- **Energy plan** - `energyPlan(watts, minutes, pricePerKwh, sessionsPerWeek)`: kWh per session, cost per session and per year.
- **Schedule plan** - `schedulePlan(totalMinutes, sessionMinutes, sessionsPerWeek)`: sessions and weeks to clear the pile.

## Labeled norms (illustrative estimates, not rules)

- Labeled pace: 5 minutes a shirt. Labeled iron: 2000 W. Heat settings belong to the garment label, never to a calculator - check the care symbols on each item.

## Files

- `index.html` / `app.html` - landing and calculators (static, no dependencies)
- `engine.js` - pure arithmetic + renderers, runs in browser and node
- `oracle.py` - python mirror of the engine; regenerates `expected.json`
- `test.js` - compares engine output to the oracle: `node test.js` (12 cases, 57 checks)

Regenerate the oracle expectations: `python3 oracle.py`
