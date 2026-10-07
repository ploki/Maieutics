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
10. [Other tools](#10-other-tools)
11. [Running a project by proxy: metamaieutics](#11-running-a-project-by-proxy-metamaieutics)
12. [Going out and coming back: agora](#12-going-out-and-coming-back-agora)
13. [Languages](#13-languages)
14. [Things you can say](#14-things-you-can-say)

---

## 1. What to expect from the agent

- **You steer.** The agent imposes no plan, no thesis and no deliverable you didn't ask for. It doesn't fix the goal at the outset either: finding the real goal is part of the work.
- **No principle of charity.** If something you say is ambiguous (a vague word, a negation that could go either way, a name that could mean two things), the agent rephrases it in one line and asks you to confirm. It does not pick the likeliest meaning and move on. It also keeps a glossary as soon as the project has terms of its own.
- **Questions in prose.** The agent asks in sentences, never through multiple-choice menus or question boxes.
- **Numbered points.** Each observation, question and proposal in a reply is numbered, so you can answer by reference: "1 yes, 3 no".
- **Plain words, not internal labels.** Each point says what it is about — the decision, the scene, the question — never just its number in the corpus or an audit code. A word coined in the corpus comes with a short explanation the first time. If something slips through, ask "what's that?".
- **It talks before it writes.** Notes change only when something substantial appears. Replies are short.
- **Memento.** Say *memento* — Latin for "remember!" — and the agent writes down everything from the session that isn't written yet: its own observations, your remarks, ideas left hanging. If the session is lost, nothing is. What it saves of its own stays marked as its own.
- **It doesn't bother you with the notes.** It doesn't report which notes it wrote or changed.
- **It's frank.** Ask for its opinion and it gives one, with reservations. When it makes a mistake, it says so and corrects the corpus.

**New versions.** The skill evolves. When you start a new project, or when you ask, the agent compares your installed copy with the published one. If they differ, it tells you, offers to say what's new in plain words, and offers to upgrade all three skills.

If Claude Code's persistent memory is available, the agent also records there, on its own, what should outlive a session: how you like to work, your preferences, where the project stands. It doesn't copy what the corpus already holds.

If it drifts away from any of this, say so. That's a fair correction.

## 2. The corpus

`corpus/` is the project's written memory. The notes exist so that anyone can pick the work back up: you next month, or a new session that remembers nothing.

| File | What it is |
|---|---|
| `00-…-index.md` | The project's method and conventions, then one line per note with its status and a summary |
| `NN-type-subject.md` | A note. `NN` is creation order, not importance. The type is framing, concept, case, source, hypothesis, objection, decision… |
| a glossary note | The project's own terms, started as soon as any appear |
| `author-intent.md` | The agent's notebook on your intent and mood (§4) |
| `decision-log.md` | Every decision and every reversal (§5) |
| `prompt-log.md` | What you said, newest first (§6) |
| `prompt-chores.md` | What you said about the project's upkeep, newest first (§6) |
| `glosses.md` | The agent's own glosses — its interpretations of what you decided, kept unvalidated — only if you want it |

Every note opens with **Current**: what holds today. Read this and you know where the note stands. It is followed by the **History** of the reasoning, reversals included. A note may also have an **Open questions** section, when something in it isn't settled.

Beside `corpus/`:

| Directory | Latin | What's in it |
|---|---|---|
| `partus/` | *a delivery, that which is brought forth* | The deliverables |
| `instrumenta/` | *the instruments*, the midwife's own | Scripts: calculations, simulations |
| `archive/` | | Abandoned pistes and superseded versions, without distinction |

If figures recur across notes, the agent can keep a **register of key figures** (value, source, status), which the notes and scripts cite instead of copying. Ask for it when you need it.

**`glosses.md` is the one file the agent offers rather than keeps by default.** Its glosses are not facts about your subject but interpretations of what you have decided, and the agent is forbidden to build on them. Keeping them somewhere means you can come back to them, and that it shows when one stops fitting the corpus. Two things can happen to a gloss: you validate it, and it moves into the notes as a fact, with a struck line here saying where it went; or a change of mind makes it false, and it is struck here with the reason. The struck ones stay, so you can see what the corpus outgrew.

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

- **You** are identified by your git name (`git config user.name`), matched against a **roster** in the index: one line per contributor, with their marker and their handle if known. Your marker is your handle when the roster has one. If you're not on the roster, the agent asks once and adds you. Several people can work on the same corpus this way.
- **Validating.** A "yes" validates exactly the point you were asked about; a general "fine, go on" validates nothing. To validate several lines at once, name them: *"I validate all of note 07."* If you change the agent's wording before agreeing, the line takes your wording and your marker alone.
- **The agent** is identified by its short model name, not "Claude"; the index gives its exact model ID. The corpus will outlive the model, and a reader in two years will want to know which one thought this.

Both identities are recorded in the index, so any reader knows who the markers stand for.

A note full of the agent's name with no arrow is a note full of things you haven't agreed to. That's worth a look.

## 4. The author's intent

`corpus/author-intent.md` is the agent's notebook about you, kept for its own use: your mood, your intent, the big picture, and what you perceive only dimly. It also holds your convictions, what you refuse, your stance and your misgivings, in your own words where possible. Things the agent has observed about you are marked with its name, for you to confirm.

It holds only what bears on the project. It is updated whenever your intent sharpens or shifts, which is often where you find out what you are really after. The agent reads it first every time the project is picked back up, and the line it adds to `CLAUDE.md` tells any later session to do the same.

If it says something about you that isn't true, correct it. It's the compass for everything else, including `metamaieutics`.

## 5. Decisions and changes of mind

`corpus/decision-log.md` has one line per decision and per change of mind: number, date, the decision and why it was taken, what it replaces, and the files concerned.

When you **change your mind**, say so plainly. The agent:

1. hunts through the corpus and the deliverables for everything the change makes false, and corrects it;
2. adds a line to the log marked **↺**, naming what it reverses and why.

The reversed line stays where it is. **The log is never rewritten.** If a file is renamed later, old lines keep the old name. They aren't wrong, they're dated. That's what makes the log worth reading: it records what was actually decided, when, and why.

## 6. The prompt log

If you chose versioning option (c), `corpus/prompt-log.md` keeps a clean, concise rewrite of each of your messages, losing nothing, **newest first**. A message is logged only if it modifies something else: typing `/maieutics`, upgrading the skill installed on your machine, pushing, or a remark that changes nothing leave no entry. Like the decision log, it is never edited afterwards.

Messages about the upkeep of the project rather than its subject — upgrading the project to a newer format of the skill, adding skill customizations to its `CLAUDE.md`, and the like — go to `corpus/prompt-chores.md` instead, in the same form. The prompt log keeps to the subject.

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
- `partus/` is where you and the agent work together. You can write in a deliverable directly — a comment, a correction — and tell the agent; it sees what you mean, and where. What happens next depends on the occasion and on what you say.

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
- leaving the struck entries of `glosses.md` alone: a dead gloss is kept with its cause of death;
- repairing links and bringing the index up to date.

**The logs are never touched.** And nothing is lost: git keeps every version, and `archive/` keeps the reasoning.

## 10. Other tools

The agent won't run these without you. It may suggest them; you can ask at any time.

**The audits.** *"Run a consistency audit on the corpus."* A fresh agent, read-only, goes through the corpus, the deliverables and the logs, and reports what contradicts what, what is a plain bookkeeping error, and what needs a decision from you. It fixes nothing — it reports — and you work through the list one point at a time. A second and different pass, the **exhaustivity audit** — *"Compare the prompt logs with the corpus, both ways"* — checks that nothing you said got lost, that nothing in the corpus was never said, and that no number is missing from either log; it needs versioning (c). Once the corrections are made, ask for a **verification pass** by another fresh agent: that is the one that catches what the fixing broke. The agent may offer an audit after a long session or a big reversal; you can ask at any time.

**A devil's advocate.** *"Before I accept this, have someone attack it."* When the agent proposes something structural, an independent agent can argue against it before you validate. The agent may offer this, but only occasionally.

**Branches.** When to branch, and the rest of the git dance, is up to you. Ask in your own words; the agent knows how.

**Breaking changes.** Some changes are worth doing with git — a commit first, or a branch — because they touch everything at once. Upgrading a project to a newer version of the skill is the typical case: its markers, file names or rules may have changed since the project began. Just ask for it; Claude knows how to handle it with git. Before upgrading a project, the agent asks whether you want to upgrade the skill installed on your machine first.


## 11. Running a project by proxy: metamaieutics

`metamaieutics` is the companion skill. You hand over the work, and Claude carries it out on your behalf, on a separate git branch, while your main branch stays untouched.

**When to use it:** you have a brief or an existing project, a clear enough sense of what you want, and no time to hold the conversation yourself.

**How it goes:**

1. Type `/metamaieutics`, then give a brief or point to an existing maieutics project. The folder must be under git: if it isn't, Claude offers to set it up, and offers to commit any uncommitted changes first.
2. Claude drafts a **mandate** (`mandate.md`) from your brief, or from `author-intent.md` and the corpus. It covers your deeper intent, the branch's objectives and how to tell they've been met, the expected deliverables, a maximum number of iterations (30 by default), and a rule for questions outside the mandate.
3. **You approve it.** Nothing starts without an explicit yes. If the project has no `author-intent.md` yet, Claude writes one and you approve both together. If an approved `mandate.md` already exists, Claude reuses it instead of drafting a new one.
4. Claude creates a branch `metamaieutics/<subject>-<date>` and launches an agent that applies the maieutics method. Claude then plays **your** part. It isn't compliant: it pushes back, asks for precision, and refuses whatever strays from the mandate. Every exchange is logged in the project's own `prompt-log.md` (or `prompt-chores.md` for a chore), marked as said on your behalf, and committed, one commit per iteration — even one that changes nothing, since the log is the record of how Claude represented you.
5. Decisions taken on your behalf are marked **[opus-5 as alice]**, never as yours. Claude settles a question outside the mandate only if the answer is consistent with it and reversible. Otherwise it leaves the question open.
6. It stops when the objectives are met, when the iteration limit is reached, or when a question outside the mandate blocks the way.
7. You receive a **handback report** (`handback-report.md`): what was achieved, the decisions taken by proxy, where Claude was unsure it represented you well, what is still open, what to re-read first, and how to see, keep, take part of, or discard the work. You say which in plain words; Claude runs the git commands.

**Always forbidden by the mandate:** publishing anything; sending anything to an outside service (no mail, no message, no upload); touching your main branch; and removing anything from git history. Read-only web search stays allowed unless the mandate excludes it. You can add your own prohibitions.

Apart from approving the mandate, and answering those setup questions, you have nothing to do until the handback.

**You decide at the end.** Claude merges nothing of its own accord. You decide to keep it all, take part of it, or throw the branch away, and Claude carries it out. It then offers to go through the decisions taken on your behalf, one at a time: what you validate becomes **[opus-5 → alice]**, what you reject is reversed, what you leave aside stays **[opus-5 as alice]**. Merging alone validates nothing.

If another session is still working in the same folder, Claude can run the branch in a separate **worktree** (a second folder on the same repository), so the two don't collide.

## 12. Going out and coming back: agora

`agora` is the third skill. It makes one maieutics project your **agora**: the place your sessions start from and come back to — one per person, and it is called agora whatever its folder — as Socrates went out to the agora, followed whoever he met into their affairs, and came back.

- **Going out.** When you leave agora to work in another project, the agent writes a line in agora's `corpus/worklog.md`: the time, read from the clock, where you went, and why.
- **Away.** The other project follows its own rules. Agora leaves no trace there, so that project stays usable by someone who has no agora.
- **Coming back.** The agent writes the time you returned and the broad lines of what happened. Whatever you want agora to keep from the outing goes into its notes, like anything else in maieutics.
- **Getting in.** If a previous outing never came back, the agent asks you what happened, or reconstructs it from the other project's history and marks the reconstruction as its own.

**Talking to agora.** When you talk to agora — *"hey agora, what was I doing last night?"* — you talk to your own agora, from anywhere, in any context. If the skill isn't loaded, the agent first offers to load it.

What agora is about is up to you, and is discovered there, as in any maieutics project. With your agreement, the agent can add a pointer to your global instructions so that *"back to agora"* works from anywhere.

## 13. Languages

The agent talks to you in your language, and the body of your notes is written in it too. **The corpus's structure stays in English**: file and directory names, the headings *Current*, *History* and *Open questions*, and the markers. That way a corpus reads the same to any tool and any later session, whatever language it was conducted in.

The skill itself, the banner and these pages are in English only.

## 14. Things you can say

None of these are commands. Plain speech works, and these are just examples.

| You want to… | Say something like |
|---|---|
| start | `/maieutics` |
| pick up where you left off | `/maieutics`, then *"Let's take up the most pressing point."* |
| make sure nothing from the session is lost | *"Memento."* |
| change your mind | *"Actually, I no longer think X."* |
| get the agent's opinion | *"What do you honestly think?"* |
| see where things stand | *"Where are we?"* |
| get a deliverable | *"I think we have enough. Write a [genre] for [reader]."* |
| test a deliverable | *"Run a blind reading on it."* |
| find inconsistencies | *"Run a consistency audit on the corpus."* |
| check nothing you said got lost | *"Compare the prompt logs with the corpus, both ways."* |
| test a proposal before accepting it | *"Get a devil's advocate on this."* |
| slim the corpus down | *"Let's prune."* |
| go back and try another way | *"Can we branch from before we decided X?"* |
| keep a list of numbers straight | *"Start a register of key figures."* |
| keep the agent's glosses without endorsing them | *"Keep those somewhere, I'm not validating them."* |
| fix the banner on a light terminal | *"My terminal is light."* |
| hand the work over | `/metamaieutics` |
| start or return to agora | `/agora`, or *"Back to agora."* |
| ask agora something, from anywhere | *"Hey agora, what was I doing last night?"* |
