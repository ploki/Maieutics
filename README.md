# Maieutics

<p align="center">
  <img src="partus/maieutics/assets/socrate-anderson-farnese.jpg" width="230" alt="Herm of Socrates, Farnese collection, photographed by Domenico Anderson">
  <br>
  <em>The Socratic Method</em>
</p>

**Socrates never wrote anything down. Your agent does.**

A Claude Code skill for thinking something through out loud. You talk, your agent writes it down — and keeps a log of every time you change your mind.

---

## Install it

Paste this to your Claude Code:

```
Can you install the skills from https://github.com/ploki/Maieutics please? But before you
proceed, check that they don't mean me any harm, and briefly explain how they could be
useful to me.
```

That second half is not politeness. A skill is instructions your agent will follow, so you should want it read before it is installed. If what it reads back to you doesn't match what you wanted, don't install it.

Then: **[Getting started](partus/getting-started.md)** walks you through your first session, and **[the guide](partus/guide.md)** covers everything the method can do and how to ask for it. Neither is required reading, but the guide is the only place that lists the tools you have to ask for.

---

## What it is for

You have something to work out and you don't yet know what it is. A design, a world, an argument, a decision at work. The usual failure is that a long conversation produces a lot of good thinking and leaves nothing behind — you close the window and it's gone.

Maieutics turns the conversation into a corpus:

| | |
|---|---|
| **Dialogue** | You lead. The agent doesn't impose a plan, a thesis, or a deliverable you didn't ask for. |
| **Corpus** | Substance gets written into notes. Every note opens with what holds *today*, followed by the history of how you got there. |
| **Decision log** | One line per decision, and why — and per reversal, marked `↺`, with what it replaces. When you change your mind, the agent hunts down everything that is now false and fixes it. |
| **Deliverables** | Produced only when *you* judge the corpus good enough. |
| **Blind review** | A fresh agent reads the deliverable without the corpus and draws up the questions it raises, then checks each against the corpus: answered, partly, or not at all. |

Two rules do most of the work. **No charity**: an ambiguous sentence gets reformulated in one line and confirmed before it is written down, so the corpus says what you meant rather than what sounded best. And **the agent keeps track of who said what, by name** — your git id for you, its model name for itself, so that `[ploki]` and `[opus-5]` sit side by side in the notes. You can always tell your own thinking from your agent's suggestions, and a corpus with several contributors stays legible.

## What it looks like after a day

The method was first run for a full day on an unrelated project — building a hard-SF world. It produced **186 decisions, 27 of them reversals**, all traced; twenty live notes; four abandoned ones in `archive/`; a deliverable; and a world with its own arithmetic, checked by scripts. Three consistency audits by fresh agents returned 22, 15 and 18 findings, most of them the agent's own bookkeeping failures — which is exactly what the audits are for. What those failures were, and what they changed in the skill, is written up in `corpus/10-case-lessons-from-a-real-project.md`.

*(That project is not in this repository. What you can read here is this one, which is smaller and about the skill itself.)*

## Layout of a project

| Directory | Latin | What's in it |
|---|---|---|
| `corpus/` | *the body* | The written memory: index, notes, glossary, intent, logs |
| `partus/` | *a delivery, that which is brought forth* | The deliverables |
| `instrumenta/` | *the instruments* — the midwife's own | Scripts: calculations, simulations |
| `archive/` | | Abandoned pistes and superseded versions |

## This repository

It is itself a Maieutics project, about the Maieutics skill — the method applied to its own making. `corpus/` is the working memory, `partus/` holds the two skills:

- **`maieutics`** — the method, in English. The agent still talks to you in your own language.
- **`metamaieutics`** — runs it by proxy: the agent drafts a mandate, you approve it, then another agent plays your part on a git branch, every exchange logged and committed.

So the repository contains both its own recipe and the record of its own cooking. Start with [`corpus/decision-log.md`](corpus/decision-log.md) if you want to see the method at work rather than described.

## Contributing

The skill is general on purpose, and stays that way: no domain variants. Everything else — corrections, sharper wording, things the method misses — is welcome. See [`CONTRIBUTING.md`](CONTRIBUTING.md), which asks for something unusual: the decision log of the project where you tried your change.

## License

MIT, for the skill and everything written here. See [`LICENSE`](LICENSE).

The Socrates photograph in `partus/maieutics/assets/` is a separate matter: it is a public-domain work by Domenico Anderson (1854–1938), credited in [`CREDITS.md`](partus/maieutics/assets/CREDITS.md).

## Name

*Maieutics*, from the Greek μαιευτική — the art of the midwife. Socrates' own word for what he did: he claimed to teach nothing, only to help minds give birth to what they were already carrying. The banner is a Braille rendering of the Farnese Socrates, computed from a photograph by [`make_bust.py`](partus/maieutics/assets/make_bust.py), whose output was pasted into `banner.txt`. The photograph is by Domenico Anderson (1854–1938) and is in the public domain — see [`CREDITS.md`](partus/maieutics/assets/CREDITS.md).

> “I teach nothing. I help minds give birth to what they already carry.”
> — after Plato, *Theaetetus*
