# partus — what this project brings forth

**[opus-5 → ploki]** The deliverable is **the pair of skills**. They were first received as installed on the author's machine on 2026-10-03, and have been worked on here since — translated, renamed, re-marked.

```
partus/maieutics/
  SKILL.md                            the skill, in English
  SKILL.fr.md                         the French original, kept
  assets/banner.txt                   the Socrates buste, Braille, 41 lines
  assets/make_bust.py                 generates the buste from the portrait
  assets/socrate-anderson-farnese.jpg the source portrait

partus/metamaieutics/
  SKILL.md                            the companion: running a project by proxy
  SKILL.fr.md                         the French original, kept
```

`maieutics` is the method; `metamaieutics` runs it **by proxy** — Claude writes a mandate, the author approves it, and an agent then plays the author's part on a git branch, every exchange logged and committed. That is where the proxy marker — `[<agent id> as <user id>]` — comes from.

**This repository is the source.** The copies under `partus/` are what gets worked on; the versions installed in `~/.claude/skills/` are never modified from here. They will drift, and that is expected — the author refreshes his installation when he chooses. See `corpus/04-decision-working-rule.md`.

The banner is worth a note of its own: it is **not drawn by hand but computed** from a photograph of the Farnese Socrates, by `make_bust.py`.
