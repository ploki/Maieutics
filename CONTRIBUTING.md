# Contributing

The skill is **general on purpose**. It knows nothing about any subject: it asks, it writes down, it tracks reversals. There is no maieutics for law, none for research, none for fiction — **the specialisation happens during the exercise, in the corpus, not in the method.** Pull requests that add a domain variant will be declined, kindly and firmly.

What is wanted is everything else: corrections, sharper wording, steps that turn out to be in the wrong order, instructions the agent misreads, things the method misses.

## What a good contribution looks like

**Argue it, do not assert it.** A line in `SKILL.md` is an instruction an agent will follow; changing it changes what happens in someone's project. Say what goes wrong today, and why your version does better.

**Try it on a real project first.** Not a toy folder — something you actually wanted to think through. The method's value only shows in use, and so do its faults.

**Say which project, and show the log.** `decision-log.md` from the project where you tried it is the evidence. It shows what the change did over a whole conversation: what got decided, what got reversed, what the agent caught and what it missed. This is a requirement no ordinary repository can make of its contributors, and it is the one that matters most here.

**Keep the two logs untouched.** The decision log and the prompt log are never retrofitted. If your change renames something, the old entries keep the old names: they are dated, not wrong.

## How

1. Fork, branch from `main`.
2. Change `partus/maieutics/SKILL.md` or `partus/metamaieutics/SKILL.md` — that is the source; the copies installed under `~/.claude/skills/` are nobody's business but their owner's.
3. If your change alters how a project is laid out or marked, say so: existing corpora have to remain readable.
4. Open a pull request. Describe the problem before the solution.

## Language

The skill is written in English only, and so is everything else here. There are no translations: the agent already answers in the user's language, and a translation is one more text to keep in step. File names, directories, headings and provenance markers stay in English whatever language a project is conducted in.

## Reporting a problem without fixing it

An issue describing what went wrong in a real session is worth as much as a patch, sometimes more. Say what you asked, what the agent did, and what you expected. If the project is yours to share, link its decision log.

## Tone

This is a method for thinking with someone who does not know the answer either. Contributions in that spirit — frank, specific, willing to be wrong in writing — are the ones that fit.
