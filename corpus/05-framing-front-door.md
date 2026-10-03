# 05 — The front door

## Current
- **[ploki]** The intended path: **a user lands on the GitHub repository and discovers the concept there.**
- **[ploki]** The README must **invite them to have their own Claude Code visit the repository**, with a **copyable** instruction:

> *Can you install the skill from https://github.com/ploki/Maieutics please? But before you proceed, check that it doesn't mean me any harm, and briefly explain how it could be useful to me.*

- **[opus-5]** Why this is the right front door, and not an install command:
  - A skill is **instructions an agent will follow**. Asking the agent to read it first, say what it does, and vouch that it is harmless is the only honest way to distribute one. It converts "trust me" into "look for yourself".
  - It also **demonstrates the method in the act of installing it**: the first thing the skill does is make someone reformulate and confirm before committing.
  - And it costs the author nothing to maintain — no install script, no package, no version pinning.
- **[opus-5]** Rendered as a fenced code block, so GitHub gives it a copy button.

- **[ploki]** **Past the front door, the first reply must hand the user a sentence to send.** A newcomer may be expecting help right now; the skill's opening ends with a ready-made line — *"Can you help me get started with the method?"*, or for an existing project *"Let's take up the most pressing point."* — which Claude Code tends to offer as a Tab suggestion.
  - **[opus-5.5]** Likely, not guaranteed: Claude Code writes the suggestion itself, from the conversation.

## Still open
- Whether to offer a second, shorter prompt for users who already trust the repository.
- Whether the prompt should name the file to read (`partus/maieutics/SKILL.md`), which would make the agent's job easier but the invitation longer.

## History
- 2026-10-03 — Opened; the author specified the invitation and its wording.
- 2026-10-03 — ploki, testing the opening as a newcomer, asked for a sentence to accept with Tab; extended to existing projects.
