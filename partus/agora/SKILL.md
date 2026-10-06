---
name: agora
description: Runs a maieutics hub — the project every session starts from and returns to. Logs each departure to another project and each return, with the time and the broad lines of what happened there. Builds on the maieutics skill. Use when the user types /agora, says "let's go to the hub" or "back to the hub", or when a CLAUDE.md states "this folder is a maieutics hub".
---

# Agora

> Socrates did not stay in one house: he went to the agora, followed whoever he met into their affairs, and came back. The hub is that square.

A hub is a maieutics project that sessions start from and return to. Follow `maieutics` in full; this skill adds only the going out and the coming back. What the hub is about is discovered there, as in any maieutics project.

## Getting in
- Open or resume as in `maieutics`.
- Close what was left open: a departure with no return means the last session never came back. Ask the user, or reconstruct from the other place's own history, mark the reconstruction as yours, and close the line.
- With the user's agreement, wire the hub once: a line in its `CLAUDE.md` ("This folder is a maieutics hub (skill `agora`). Read `corpus/author-intent.md` first."), and a pointer in the user's global instructions so that their own words for "back to the hub" work from anywhere.

## Going out
Add a line to `corpus/worklog.md`, newest first: the start time **read from the system clock**, never estimated; where; why, in a few words. Commit the hub if it is versioned.

## Away
The other place's own rules apply: its `CLAUDE.md`, its skill, its logs. **Leave no trace of the hub there** — it must stay usable by someone who has none of this.

## Coming back
Write the end time, from the clock, and the broad lines of what happened, drawn from the session and from the other place's own history. Whatever the user wants the hub to keep from the outing goes into its notes, as anything does in `maieutics`. Commit the hub if it is versioned.

## The worklog
One line per outing. Parallel outings get a line each. An outing that started outside the hub gets its line late, marked as such. The worklog is never pruned.
