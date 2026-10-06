---
name: agora
description: Runs agora — the user's maieutics project that every session starts from and returns to. Logs each departure to another project and each return, with the time and the broad lines of what happened there. Builds on the maieutics skill. Use when the user types /agora, says "let's go to agora" or "back to agora", addresses agora by name ("hey agora…"), or when a CLAUDE.md states "this folder is agora".
---

# Agora

> Socrates did not stay in one house: he went to the agora, followed whoever he met into their affairs, and came back. Agora is that square.

Agora is the user's maieutics project that sessions start from and return to — one per user, and it is called agora, whatever its folder. Follow `maieutics` in full; this skill adds only the going out and the coming back. What agora is about is discovered there, as in any maieutics project.

## Getting in
- Open or resume as in `maieutics`.
- Close what was left open: a departure with no return means the last session never came back. Ask the user, or reconstruct from the other place's own history, mark the reconstruction as yours, and close the line.
- With the user's agreement, wire agora once: a line in its `CLAUDE.md` ("This folder is agora, a maieutics project (skill `agora`). Read `corpus/author-intent.md` first."), and a pointer in the user's global instructions so that their own words for "back to agora" work from anywhere. The pointer also says that talking to agora is talking to this folder, and that if this skill is not loaded, the agent first offers to load it.

## Talking to agora
When the user talks to agora, they talk to their own agora — from anywhere, in any context.

## Going out
Add a line to `corpus/worklog.md`, newest first: the start time **read from the system clock**, never estimated; where; why, in a few words. Commit agora if it is versioned.

## Away
The other place's own rules apply: its `CLAUDE.md`, its skill, its logs. **Leave no trace of agora there** — it must stay usable by someone who has none of this.

## Coming back
Write the end time, from the clock, and the broad lines of what happened, drawn from the session and from the other place's own history. Whatever the user wants agora to keep from the outing goes into its notes, as anything does in `maieutics`. Commit agora if it is versioned.

## The worklog
One line per outing. Parallel outings get a line each. An outing that started outside agora gets its line late, marked as such. The worklog is never pruned.
