(function (root) {
  "use strict";
  function plural(n, word, form) { return n + " " + (n === 1 ? word : (form || word + "s")); }
  function money(c) { return "$" + Math.floor(c / 100) + "." + ("0" + (c % 100)).slice(-2); }

  function pilePlan(items, minutesPerItem) {
    if (!(items > 0) || !(minutesPerItem > 0)) return { error: "items and minutes must be positive" };
    var minutes = items * minutesPerItem;
    var hours = Math.round(minutes / 60 * 10) / 10;
    return { minutes: minutes, hours: hours };
  }

  function energyPlan(watts, minutes, pricePerKwh, sessionsPerWeek) {
    if (!(watts > 0) || !(minutes > 0) || !(pricePerKwh > 0) || !(sessionsPerWeek > 0)) return { error: "watts, minutes, price and sessions must be positive" };
    var kwh = watts * minutes / 60 / 1000;
    var sessionCents = Math.round(kwh * pricePerKwh * 100);
    var yearCents = Math.round(kwh * sessionsPerWeek * 52 * pricePerKwh * 100);
    var priceCents = Math.round(pricePerKwh * 100);
    return { kwh: kwh, sessionCents: sessionCents, yearCents: yearCents, priceCents: priceCents };
  }

  function schedulePlan(totalMinutes, sessionMinutes, sessionsPerWeek) {
    if (!(totalMinutes > 0) || !(sessionMinutes > 0) || !(sessionsPerWeek > 0)) return { error: "minutes and sessions must be positive" };
    var sessions = Math.ceil(totalMinutes / sessionMinutes);
    var weeks = Math.ceil(sessions / sessionsPerWeek);
    return { sessions: sessions, weeks: weeks };
  }

  function renderPile(r, items, minutesPerItem) {
    return plural(items, "item") + " at a labeled " + minutesPerItem + " minutes each: " + r.minutes + " minutes at the board - " + plural(r.hours, "hour") + " of ironing.";
  }

  function renderEnergy(r, watts, minutes, pricePerKwh, sessionsPerWeek) {
    return "A " + watts + " W iron for " + minutes + " minutes uses " + r.kwh + " kWh: " + money(r.sessionCents) + " a session at " + money(r.priceCents) + " a kWh, " + money(r.yearCents) + " a year at " + plural(sessionsPerWeek, "session") + " a week.";
  }

  function renderSchedule(r, totalMinutes, sessionMinutes, sessionsPerWeek) {
    return plural(totalMinutes, "minute") + " of pile in " + sessionMinutes + "-minute sessions: " + plural(r.sessions, "session") + ", cleared in " + plural(r.weeks, "week") + " at " + plural(sessionsPerWeek, "session") + " a week.";
  }

  var api = { pilePlan: pilePlan, energyPlan: energyPlan, schedulePlan: schedulePlan, renderPile: renderPile, renderEnergy: renderEnergy, renderSchedule: renderSchedule };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.IroningMath = api;
})(this);
