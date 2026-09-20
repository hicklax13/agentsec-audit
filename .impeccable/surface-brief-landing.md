# Surface Brief: Landing Page (agentsec-audit index)

## Scope & Visitor Mode
- Surface: single landing page (`index.html`), Persuade mode. Visitor: AI engineer or security lead deciding whether to adopt the audit tool.

## Audience, Job, Action
- Job: determine in under 30 seconds whether AgentSec can gate their agent deploys against OWASP ASI-10, and take one action (install CLI / subscribe Team / subscribe Pro).
- Proof: real terminal scan transcript (real output from actual runs), GitHub Action snippet, comparison vs Snyk/LlamaGuard.

## Direction Contract (code-led, seed key 8971cc1c)

THESIS: The audit scoreboard. The page IS a live security readout: every score, status, and finding renders as a seven-segment LED cell on matte black, unlit ghost segments deliberately drawn. Refuses the category-default centered hero with gradient blob.

OWN-WORLD: Pitch black (#08080a) ground; matte carbon panels (#101014/#15151b); a single crimson red (#ef4444) owning ALL segment-light, buttons, and state marks; white display type; gray supporting text. Line ink is black hairlines. Seven-segment digit masks (clip-path or grid cells) for scores; terminal window with measured chrome; pinned state-marks (grease-cross style) instead of status dots.

STORY: Visitor sees a real audit run immediately - red CRITICAL segments lighting, score 10/100 in dead red digits, then `agentsec fix` flipping the same readout to green PASSED 100/100. Believes: this tool executes, it does not advertise. Acts: installs CLI or subscribes.

FIRST VIEWPORT: Left-aligned split hero (not centered). Left column: wordmark nav row already above; headline 2 lines max ("Ship autonomous AI agents without security violations", "security violations" in red), 20-word subtext, primary red CTA + secondary GitHub ghost button. Right column: terminal window (real transcript) with seven-segment score readout strip beneath it. Grid hairlines faint. CTA visible without scroll.

FORM: Assigned direction (audit-readout world), raised by: seven-segment numeric discipline (donor: seven-segment display), pinned state-mark findings (donor: film cutting bench), single-line-ink hierarchy (donor: glazier partition).

SIGNATURE INTERACTION: The hero terminal replays a real scan → fail → fix → pass cycle as an authored, once-per-load choreographed sequence (blinking cursor, segments igniting left-to-right), honoring prefers-reduced-motion (final state shown instantly).

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance.

## Unresolved Decisions
- None blocking; principal pinned colors and name.
