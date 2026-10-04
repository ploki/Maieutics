# 04 — Working rule: the repository is the source

## Current
- **[ploki]** **When working in this repository, the installed skill is not touched.** Whatever is installed under `~/.claude/skills/` is left alone **unless the author asks for an upgrade**. The installation is now `maieutics/` and `metamaieutics/`, under the repository's names; between upgrades, the divergence is expected.
  - ↺ *Until 2026-10-03 the installation was still `maieutique/` and `metamaieutique/`, under their French names.*
- **[ploki]** **What we work on here is the creation of the skill**: the files under `partus/`.
- **[ploki]** **Only the behaviour of the running session adapts**, in the moment, to whatever the repository's skill now says. The agent follows the repository version while the exercise lasts; nothing is written back to the installation, except when the author asks (below).
- **[ploki]** **The installation is refreshed by the agent, on request**, by copying `partus/maieutics/` and `partus/metamaieutics/` into `~/.claude/skills/`. `partus/` therefore holds the installable shape exactly (decisions #37, #39, #41).

## What this settles [opus-5]
- **The source question is closed.** `partus/` is the original; the installation is a copy that will be refreshed by the author when he chooses, by his own means. The drift noted on 2026-10-03 is no longer a problem to manage but an expected state.
- **Two versions coexist during a session**, and that is deliberate: the installed one triggered the skill, the repository one governs how we go on. When they disagree, **the repository wins** — but only for the current session's conduct.
- **A trap worth naming:** the running session loaded the *installed* `SKILL.md` into context at startup. The agent does not automatically see edits made to `partus/maieutics/SKILL.md` afterwards. Someone has to say so, or the agent has to re-read the file. **Re-read it before relying on it.**

## Open questions
- None at present.

## Upgrades on request
- **[ploki]** 2026-10-03: "upgrade my installation" — `~/.claude/skills/maieutics/` brought level with `partus/maieutics/` (decision #37). Again after the push, both skills, `SKILL.fr.md` included (#39); and with decision #40 (#41); and with decision #42 (#44). The rule is unchanged: the agent upgrades the installation only when the author asks.

## History
- 2026-10-03 — Rule stated by the author.
- 2026-10-03 — Pruned: the two questions on how the installation is refreshed, answered by practice, moved into Current.
