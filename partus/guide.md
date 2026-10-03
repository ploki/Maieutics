# The guide

Everything the method does, and how to ask for it. If you haven't run a session yet, start with **[getting started](getting-started.md)**.

This page describes what you see and what you can say. What the agent itself is told to do is in [`maieutics/SKILL.md`](maieutics/SKILL.md), and that file is the authority. If this guide and the skill ever disagree, the skill is right, and the guide needs a pull request.

**Contents**
1. [What to expect from the agent](#1-what-to-expect-from-the-agent)
2. [The corpus](#2-the-corpus)
3. [Who said what](#3-who-said-what)
4. [The author's intent](#4-the-authors-intent)
5. [Decisions and changes of mind](#5-decisions-and-changes-of-mind)
6. [The prompt log](#6-the-prompt-log)
7. [Deliverables](#7-deliverables)
8. [The blind reading](#8-the-blind-reading)
9. [Pruning](#9-pruning)
10. [Tools you have to ask for](#10-tools-you-have-to-ask-for)
11. [Running a project by proxy: metamaieutics](#11-running-a-project-by-proxy-metamaieutics)
12. [Languages](#12-languages)
13. [Things you can say](#13-things-you-can-say)

---

## 1. What to expect from the agent

- **You steer.** The agent imposes no plan, no thesis and no deliverable you didn't ask for. It doesn't fix the goal at the outset either: finding the real goal is part of the work.
- **No principle of charity.** If something you say is ambiguous (a vague word, a negation that could go either way, a name that could mean two things), the agent rephrases it in one line and asks you to confirm. It does not pick the likeliest meaning and move on. It also keeps a glossary as soon as the project has terms of its own.
- **It talks before it writes.** Notes change only when something substantial appears. Replies are short.
- **It's frank.** Ask for its opinion and it gives one, with reservations. When it makes a mistake, it says so and corrects the corpus.

If Claude Code's persistent memory is available, the agent also records there, on its own, what should outlive a session: how you like to work, your preferences, where the project stands. It doesn't copy what the corpus already holds.

If it drifts away from any of this, say so. That's a fair correction.

## 2. The corpus

`corpus/` is the project's written memory. The notes exist so that anyone can pick the work back up: you next month, or a new session that remembers nothing.

| File | What it is |
|---|---|
| `00-…-index.md` | The project's method and conventions, then one line per note with its status and a summary |
| `NN-type-subject.md` | A note. `NN` is creation order, not importance. The type is framing, concept, case, source, hypothesis, objection, decision… |
| a glossary note | The project's own terms, started as soon as any appear |
| `author-intent.md` | What you are really after (§4) |
| `decision-log.md` | Every decision and every reversal (§5) |
| `prompt-log.md` | What you said, newest first (§6) |

Every note opens with **Current**: what holds today. Read this and you know where the note stands. It is followed by the **History** of the reasoning, reversals included. A note may also have an **Open questions** section, when something in it isn't settled.

Beside `corpus/`:

| Directory | Latin | What's in it |
|---|---|---|
| `partus/` | *a delivery, that which is brought forth* | The deliverables |
| `instrumenta/` | *the instruments*, the midwife's own | Scripts: calculations, simulations |
| `archive/` | | Abandoned pistes and superseded versions, without distinction |

If figures recur across notes, the agent can keep a **register of key figures** (value, source, status), which the notes and scripts cite instead of copying. Ask for it when you need it.

The layout is a default, not a law. If you'd rather arrange things differently, say so. What matters is that it stays tidy and you understand it.

## 3. Who said what

Claims in the notes carry a marker saying who made them. A corpus can have several contributors, human and not, and the point is to know whose idea a thing was.

| Marker | Means |
|---|---|
| **[alice]** | said by Alice |
| **[opus-5]** | proposed by the agent, not yet validated |
| **[opus-5 → alice]** | the agent proposed it, Alice validated it |
| **[S]** | a cited source |
| **[Unverified]** | an unsourced fact |
| **[opus-5 as alice]** | decided by proxy on Alice's behalf, during a `metamaieutics` session (§11) |

- **You** are identified by your git id (`git config user.name`, or your handle on the remote). Failing that, by your first name, or the agent asks once.
- **The agent** is identified by its model name, not "Claude". The corpus will outlive the model, and a reader in two years will want to know which one thought this.

Both identities are recorded in the index, so any reader knows who the markers stand for.

A note full of the agent's name with no arrow is a note full of things you haven't agreed to. That's worth a look.

## 4. The author's intent

`corpus/author-intent.md` holds your deeper purpose: your convictions, what you refuse, your stance and your misgivings. It uses your own words where possible. Things the agent has observed about you are marked with its name, for you to confirm.

It holds only what bears on the project. It is updated whenever your intent sharpens or shifts, which is often where you find out what you are really after. The agent reads it first every time the project is picked back up.

If it says something about you that isn't true, correct it. It's the compass for everything else, including `metamaieutics`.

## 5. Decisions and changes of mind

`corpus/decision-log.md` has one line per structural decision: number, date, the decision and why it was taken, what it replaces, and the files concerned.

When you **change your mind**, say so plainly. The agent:

1. hunts through the corpus and the deliverables for everything the change makes false, and corrects it;
2. adds a line to the log marked **↺**, naming what it reverses and why.

The reversed line stays where it is. **The log is never rewritten.** If a file is renamed later, old lines keep the old name. They aren't wrong, they're dated. That's what makes the log worth reading: it records what was actually decided, when, and why.

## 6. The prompt log

If you chose versioning option (c), `corpus/prompt-log.md` keeps a clean, concise rewrite of each of your messages, losing nothing, **newest first**. Like the decision log, it is never edited afterwards.

It shows how your thinking moved. It also lets a new session see what you asked for, in the order that matters most: latest first.

## 7. Deliverables

A deliverable is produced only when **you** judge the corpus good enough and ask for one. It helps to name the genre, and the reader if there is one:

> *Write a one-page summary for the team.*
> *Draft the opening chapter.*
> *Turn this into a decision memo with the options and my recommendation.*

- It goes in `partus/`.
- It's a **starting point**: formal and grounded, not a final text. It may state things the notes mark *Unverified*, which is sometimes part of the exercise.
- Its tone follows its genre. If you want a more personal voice, ask for a separate deliverable.
- One corpus can yield several deliverables. The corpus can be broad. Each deliverable should be narrow.

## 8. The blind reading

This is a way to find out what a deliverable fails to say. The agent suggests it at good moments, typically right after a deliverable is written or heavily revised. You can also ask for it whenever you like.

1. A **fresh agent** reads only the deliverable, without the corpus, and writes down a substantial set of precise questions, grouped by theme.
2. Those questions are recorded in a note immediately, unaltered.
3. The same agent then reads the corpus and grades each question: **A** answered, **P** partially, **N** not addressed. It ends with a count, the most pressing gaps, and any **contradictions between the deliverable and the notes**.
4. The questions become a follow-up list tied to the decision log, and you work through them with the agent, one at a time.

The agent tells the blind reader which claims really need verifying, and you can say which those are. Otherwise, a claim the notes already mark *Unverified* doesn't count as a fault.

## 9. Pruning

A living corpus gets heavier over time: settled questions left hanging, dead pistes, notes emptied by a reversal, links to things that have moved. Eventually it buries what matters.

The agent **offers** a pruning now and then: after a major reversal, when a whole note falls, or when the corpus has become tiresome to re-read. It never does this unasked, and never in the middle of your momentum. You can also ask: *"Let's prune."*

Pruning means:

- moving whatever survives of an abandoned note into the note where it now belongs, then moving the note to `archive/`;
- clearing settled questions and dropped pistes out of **Current** and **Open questions**;
- repairing links and bringing the index up to date.

**The two logs are never touched.** And nothing is lost: git keeps every version, and `archive/` keeps the reasoning.

## 10. Tools you have to ask for

The agent won't start these on its own, so you need to know they exist.

**Hunt for contradictions.** *"Re-read the whole corpus and look for contradictions."* The agent lists them and resolves them with you one by one. It fixes nothing that needs a decision from you.

**A devil's advocate.** *"Before I accept this, have someone attack it."* When the agent proposes something structural, an independent agent can argue against it before you validate. The agent may offer this, but only occasionally.

**An exploration branch.** *"I think we took a wrong turn after we dropped the offline idea. Can we go back and try it the other way?"* If you're stuck and want to explore a different piste from an earlier point, the agent walks you through creating a git branch from that earlier commit, step by step. **It never suggests this itself.** You have to ask. It needs git, so versioning option (b) or (c).


## 11. Running a project by proxy: metamaieutics

`metamaieutics` is the companion skill. You hand over the work, and Claude carries it out on your behalf, on a separate git branch, while your main branch stays untouched.

**When to use it:** you have a brief or an existing project, a clear enough sense of what you want, and no time to hold the conversation yourself.

**How it goes:**

1. Type `/metamaieutics`, then give a brief or point to an existing maieutics project. The folder must be under git: if it isn't, Claude offers to set it up, and offers to commit any uncommitted changes first.
2. Claude drafts a **mandate** (`mandate.md`) from your brief, or from `author-intent.md` and the corpus. It covers your deeper intent, the branch's objectives and how to tell they've been met, the expected deliverables, a maximum number of iterations (30 by default), and a rule for questions outside the mandate.
3. **You approve it.** Nothing starts without an explicit yes. If the project has no `author-intent.md` yet, Claude writes one and you approve both together. If an approved `mandate.md` already exists, Claude reuses it instead of drafting a new one.
4. Claude creates a branch `metamaieutics/<subject>-<date>` and launches an agent that applies the maieutics method. Claude then plays **your** part. It isn't compliant: it pushes back, asks for precision, and refuses whatever strays from the mandate. Every exchange is logged in `prompt-log.md` and committed, one commit per iteration.
5. Decisions taken on your behalf are marked **[opus-5 as alice]**, never as yours. Claude settles a question outside the mandate only if the answer is consistent with it and reversible. Otherwise it leaves the question open.
6. It stops when the objectives are met, when the iteration limit is reached, or when a question outside the mandate blocks the way.
7. You receive a **handback report** (`handback-report.md`): what was achieved, the decisions taken by proxy, where Claude was unsure it represented you well, what is still open, what to re-read first, and the git commands to see, keep, take part of, or discard the work.

**Always forbidden by the mandate:** publishing anything; sending anything to an outside service (no mail, no message, no upload); touching your main branch; and removing anything from git history. Read-only web search stays allowed unless the mandate excludes it. You can add your own prohibitions.

Apart from approving the mandate, and answering those setup questions, you have nothing to do until the handback.

**You decide at the end.** Claude merges nothing. You merge it all, take part of it, or throw the branch away.

If another session is still working in the same folder, Claude can run the branch in a separate **worktree** (a second folder on the same repository), so the two don't collide.

## 12. Languages

The agent talks to you in your language, and the body of your notes is written in it too. **The corpus's structure stays in English**: file and directory names, the headings *Current*, *History* and *Open questions*, and the markers. That way a corpus reads the same to any tool and any later session, whatever language it was conducted in.

The skill itself, the banner and these pages are in English only.

## 13. Things you can say

None of these are commands. Plain speech works, and these are just examples.

| You want to… | Say something like |
|---|---|
| start | `/maieutics` |
| pick up where you left off | `/maieutics`, then *"Let's take up the most pressing point."* |
| change your mind | *"Actually, I no longer think X."* |
| get the agent's opinion | *"What do you honestly think?"* |
| see where things stand | *"Where are we?"* |
| get a deliverable | *"I think we have enough. Write a [genre] for [reader]."* |
| test a deliverable | *"Run a blind reading on it."* |
| find inconsistencies | *"Re-read the whole corpus and look for contradictions."* |
| test a proposal before accepting it | *"Get a devil's advocate on this."* |
| slim the corpus down | *"Let's prune."* |
| go back and try another way | *"Can we branch from before we decided X?"* |
| keep a list of numbers straight | *"Start a register of key figures."* |
| fix the banner on a light terminal | *"My terminal is light."* |
| hand the work over | `/metamaieutics` |
