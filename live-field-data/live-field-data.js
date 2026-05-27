// Live Field Data — vanilla JS animator. Works with any framework or no
// framework: include this script once, and any element with [data-lfd]
// will get its clock, monitoring count, risk index, and sparkline animated.
//
// Markup contract (see preview.html for the full template):
//   [data-lfd]              wrapper element
//   [data-lfd-time]         clock text node       (HH:MM, 24h)
//   [data-lfd-monitoring]   location name text node (cycles through MONITORING_LOCATIONS)
//   [data-lfd-risk]         risk index text node  ("STABLE" / "LOW")
//   [data-lfd-spark]        <polyline> in the SVG sparkline
//
// All of these are optional — omit anything you don't want to animate.

(function () {
  const SPARK_POINTS = 28;

  function buildSparkPoints(tick) {
    const pts = [];
    for (let i = 0; i < SPARK_POINTS; i++) {
      const x = (i / (SPARK_POINTS - 1)) * 100;
      const seed = Math.sin((i + tick) * 0.6) * 0.5 + 0.5;
      const y = 30 - (seed * 18 + (1 - i / SPARK_POINTS) * 6);
      pts.push(`${x},${y.toFixed(2)}`);
    }
    return pts.join(" ");
  }

  function pad2(n) { return String(n).padStart(2, "0"); }

  function updateTime(el) {
    const d = new Date();
    el.textContent = `${pad2(d.getHours())}:${pad2(d.getMinutes())}`;
  }

  const MONITORING_LOCATIONS = [
    "ELLINIKON", "PAIANIA", "GLYFADA", "ALIMOS",
    "KYPSELI", "PAGKRATI", "LARISSA"
  ];

  function init(root) {
    if (root.__lfdInit) return;
    root.__lfdInit = true;

    const timeEl  = root.querySelector("[data-lfd-time]");
    const monEl   = root.querySelector("[data-lfd-monitoring]");
    const riskEl  = root.querySelector("[data-lfd-risk]");
    const sparkEl = root.querySelector("[data-lfd-spark]");

    if (timeEl) updateTime(timeEl);
    setInterval(() => { if (timeEl) updateTime(timeEl); }, 30 * 1000);

    let tick = 0;
    function step() {
      if (monEl)   monEl.textContent  = MONITORING_LOCATIONS[tick % MONITORING_LOCATIONS.length];
      if (riskEl)  riskEl.textContent = tick % 4 === 0 ? "LOW" : "STABLE";
      if (sparkEl) sparkEl.setAttribute("points", buildSparkPoints(tick));
      tick++;
    }
    step();
    setInterval(step, 1400);
  }

  function boot() {
    document.querySelectorAll("[data-lfd]").forEach(init);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }

  // expose for SPAs that mount the card after initial load
  window.LiveFieldData = { init, refresh: boot };
})();
