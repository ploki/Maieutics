# Maieutics

**Socrates never wrote anything down. Your agent does.**

A Claude Code skill for thinking something through out loud. You talk, your agent writes it down — and keeps a log of every time you change your mind.

---

## Install it

Paste this to your Claude Code:

```
Can you install the skill from https://github.com/ploki/Maieutics please? But before you
proceed, check that it doesn't mean me any harm, and briefly explain how it could be
useful to me.
```

That second half is not politeness. A skill is instructions your agent will follow, so you should want it read before it is installed. If what it reads back to you doesn't match what you wanted, don't install it.

---

## What it is for

You have something to work out and you don't yet know what it is. A design, a world, an argument, a decision at work. The usual failure is that a long conversation produces a lot of good thinking and leaves nothing behind — you close the window and it's gone.

Maieutics turns the conversation into a corpus:

| | |
|---|---|
| **Dialogue** | You lead. The agent doesn't impose a plan, a thesis, or a deliverable you didn't ask for. |
| **Corpus** | Substance gets written into notes. Every note opens with what holds *today*, followed by the history of how you got there. |
| **Decision log** | One line per structural decision — and per reversal, marked `↺`, with what it replaces. When you change your mind, the agent hunts down everything that is now false and fixes it. |
| **Deliverables** | Produced only when *you* judge the corpus good enough. |
| **Blind review** | A fresh agent reads the deliverable without the corpus and lists what it couldn't understand. |

Two rules do most of the work. **No charity**: an ambiguous sentence gets reformulated in one line and confirmed before it is written down, so the corpus says what you meant rather than what sounded best. And **the agent keeps track of who said what** — `[A]` you, `[C]` the agent unvalidated, `[S]` a cited source — so you can always tell your own thinking from your agent's suggestions.

## What it looks like after a day

A real project, one day of conversation: **184 decisions, about twenty of them reversals**, all traced; twelve live notes; three abandoned ones in `archive/`; two deliverables; a world with its own arithmetic, checked by scripts. Three consistency audits by fresh agents found eighteen internal contradictions, sixteen of which were the agent's own bookkeeping failures — which is exactly what the audits are for.

## Layout of a project

| Directory | Latin | What's in it |
|---|---|---|
| `corpus/` | *the body* | The written memory: index, notes, glossary, intent, logs |
| `partus/` | *a delivery, that which is brought forth* | The deliverables |
| `instrumenta/` | *the instruments* — the midwife's own | Scripts: calculations, simulations |
| `archive/` | | Abandoned pistes and superseded versions |

## This repository

It is itself a Maieutics project, about the Maieutics skill — the method applied to its own making. `corpus/` is the working memory, `partus/` holds the two skills:

- **`maieutique`** — the method. Currently in French; an English version is being worked out here.
- **`metamaieutique`** — runs it by proxy: the agent drafts a mandate, you approve it, then another agent plays your part on a git branch, every exchange logged and committed.

So the repository contains both its own recipe and the record of its own cooking. Start with [`corpus/decision-log.md`](corpus/decision-log.md) if you want to see the method at work rather than described.

## Name

*Maieutics*, from the Greek μαιευτική — the art of the midwife. Socrates' own word for what he did: he claimed to teach nothing, only to help minds give birth to what they were already carrying. The banner is a Braille rendering of the Farnese Socrates, computed from a photograph by [`partus/maieutique/assets/make_bust.py`](partus/maieutique/assets/make_bust.py).

> « Je n'enseigne rien ; j'aide les esprits à mettre au monde ce qu'ils portent. »
> — after Plato, *Theaetetus*
