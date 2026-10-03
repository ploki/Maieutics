# 04 — Working rule: the repository is the source

## Current
- **[ploki]** **When working in this repository, the installed skill is not touched.** Whatever is installed under `~/.claude/skills/` is left alone — today that is still `maieutique/` and `metamaieutique/`, under their French names, while the repository has moved to `maieutics` and `metamaieutics`. The divergence is expected.
- **[ploki]** **What we work on here is the creation of the skill**: the files under `partus/`.
- **[ploki]** **Only the behaviour of the running session adapts**, in the moment, to whatever the repository's skill now says. The agent follows the repository version while the exercise lasts; nothing is written back to the installation.

## What this settles [opus-5]
- **The source question is closed.** `partus/` is the original; the installation is a copy that will be refreshed by the author when he chooses, by his own means. The drift noted on 2026-10-03 is no longer a problem to manage but an expected state.
- **Two versions coexist during a session**, and that is deliberate: the installed one triggered the skill, the repository one governs how we go on. When they disagree, **the repository wins** — but only for the current session's conduct.
- **A trap worth naming:** the running session loaded the *installed* `SKILL.md` into context at startup. The agent does not automatically see edits made to `partus/maieutics/SKILL.md` afterwards. Someone has to say so, or the agent has to re-read the file. **Re-read it before relying on it.**

## Still open
- How the author refreshes his installation from the repository — by hand, by a symlink, by a script in `instrumenta/`? *(His business, but it affects whether `partus/` should hold an installable layout.)*
- Whether `partus/` should mirror the installable shape exactly, so that a user can copy it straight into `~/.claude/skills/`.

## Upgrades on request
- **[ploki]** 2026-10-03: "upgrade my installation" — `~/.claude/skills/maieutics/` brought level with `partus/maieutics/` (decision #37). The rule is unchanged: the agent upgrades the installation only when the author asks.

## History
- 2026-10-03 — Rule stated by the author.
