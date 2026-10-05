# partus — what this project brings forth

**[opus-5 → ploki]** The deliverable is **the pair of skills**. They were first received as installed on the author's machine on 2026-10-03, and have been worked on here since — translated into English, renamed, re-marked.

```
partus/getting-started.md             the first session, step by step
partus/guide.md                       everything the method does, and how to ask for it

partus/maieutics/
  SKILL.md                            the skill, in English
  assets/banner.txt                   the Socrates buste, Braille, 26 lines
  assets/CREDITS.md                   the portrait's source and licence
  assets/make_bust.py                 generates the buste from the portrait
  assets/socrate-anderson-farnese.jpg the source portrait

partus/metamaieutics/
  SKILL.md                            the companion: running a project by proxy
```

`maieutics` is the method; `metamaieutics` runs it **by proxy** — one agent writes a mandate, the author approves it, then that agent plays the author's part on a git branch while a second agent applies the method, every exchange logged and committed. That is where the proxy marker — `[<agent id> as <user id>]` — comes from.

**This repository is the source.** The copies under `partus/` are what gets worked on; the versions installed in `~/.claude/skills/` are never modified from here. They will drift, and that is expected — the author refreshes the installation when they choose, by their own means or by asking the agent. See `corpus/04-decision-working-rule.md`.

The banner is worth a note of its own: it is **not drawn by hand but computed** from a photograph of the Farnese Socrates, by `make_bust.py`.
