---
version: "alpha"
name: AgentSec Audit Design System
description: Dark security-engineer design system for the AgentSec Audit landing page. Red/Black/White/Gray brand.

colors:
  ink: "#0a0a0c"            # page ground
  panel: "#111114"          # raised surface
  panelDeep: "#16161a"      # deeper surface
  hairline: "#232329"       # 1px line ink
  hairlineStrong: "#2e2e36"
  red: "#ef3b3b"            # THE single accent
  redDeep: "#b32727"
  redGhost: "rgba(239,59,59,0.28)"
  white: "#f5f5f2"
  gray1: "#a3a3ad"          # secondary text
  gray2: "#6e6e78"          # muted text
  segOff: "#1d1d23"         # unlit LED ghost
  segRed: "#ff4545"
  segGreen: "#3ddc7a"

typography:
  display:
    fontFamily: Archivo Narrow
    fontWeight: 800
    transform: uppercase
    lineHeight: 1.02
    letterSpacing: "-0.02em"
    sizes: ["2.6rem", "4.2rem"]
  body:
    fontFamily: Archivo
    fontWeight: 400
    lineHeight: 1.55
    baseSize: 16px
  mono:
    fontFamily: IBM Plex Mono
    uses: [code, labels, findings, terminal, scores]

rounded:
  sm: 4px
  md: 8px

spacing:
  unit: 8px
  scale: [8, 16, 22, 32, 44, 56, 72, 84, 96]

components:
  button-primary:
    backgroundColor: "{colors.red}"
    textColor: "#FFFFFF"
    rounded: "{rounded.sm}"
    fontFamily: Archivo Narrow
    fontWeight: 700
    transform: uppercase
    boxShadow: "0 6px 22px rgba(239,59,59,0.25)"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.white}"
    border: "1px solid {colors.hairlineStrong}"
  ledger-row:
    gridColumns: "54px 110px 1fr 210px"
    borderBottom: "1px solid {colors.hairline}"
    hover: "{colors.panelDeep}"
  segment-readout:
    onRed: "{colors.segRed}"
    onGreen: "{colors.segGreen}"
    offGhost: "{colors.segOff}"

---

## Overview
The page is a live audit readout, not a marketing template. Every numeric
finding, score, and status renders as a segment-cell readout on matte black.

## Colors
One accent only (red). Red owns buttons, segment light, state marks, and
highlights. Gray text only on black; never gray-on-gray.

## Typography
Condensed uppercase display for headlines; Archivo for body; IBM Plex Mono
reserved strictly for code, data, labels, and terminal output (never as a
"technical" costume).

## Layout
6-column hairline grid over the whole page. Left-aligned split hero.
Findings ledger (not cards). Perforated rule rail.

## Elevation
Offset shadows with soft blur on panels only. No zero-offset halos.

## Shapes
One corner system: 4px on controls, 8px on panels. No pills except the
featured flag (documented exception).

## Do's and Don'ts
- DO show real scanner transcripts.
- DON'T fabricate testimonials, logos, or fake-precision benchmarks.
- DON'T use gradient text, neon glow costumes, or glassmorphism.

## Verified Anomalies (documented exceptions)
- scrollbar thumb radius: clamped to rounded.sm (was 5px, off-scale)
- .vuln text #ffa0a0: lighter tint of the single red accent for terminal output legibility on #0c0c10
- .pin-warn #e5b93c: amber severity token for WARN-class findings (semantic state, not decoration)
- offset shadows rgba(0,0,0,0.42): neutral depth shadows on dark panels (replaces AI-glow)
