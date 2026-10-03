# Getting started

Your first session with the maieutics skill, from an empty folder to a corpus you can come back to tomorrow. You don't need to read this first: the agent explains the essentials when you start. This page is for people who like to know what's coming.

If you haven't installed the skill yet, see the [README](../README.md#install-it).

## 1. Give it a folder

Each project lives in its own folder. Make one and name it after your subject, even roughly. If you already have material, such as notes, drafts or a PDF you keep coming back to, put it in the folder. The agent will look at it.

```
mkdir ~/thinking/my-subject
cd ~/thinking/my-subject
claude
```

## 2. Start

Type:

```
/maieutics
```

The agent replies with:

- **a banner**, Socrates in Braille dots. It is drawn for a dark terminal. If yours is light, say so: the agent can generate an inverted buste with `make_bust.py`, which needs Python and Pillow;
- **three or four sentences** explaining what the method is for;
- **a first step to suggest**, based on whatever is in the folder, its name, or your first sentence;
- **a sentence you can send as is**, on its own line, such as *"Can you help me get started with the method?"* Claude Code often offers it as a Tab suggestion.

You don't have to know what you're looking for. Not knowing is the starting point.

## 3. Answer one question about versioning

The agent asks once how you want your work kept. git keeps a photograph of every step, so you can go back.

- **(a)** no git;
- **(b)** git, with a commit at each exchange that changes files;
- **(c)** the same, plus a **prompt log**: a short, faithful rewrite of each of your messages, newest first.

If you're unsure, pick (c). It costs you nothing, and it's the best record of how your thinking moved. If you pick (b) or (c) and the folder isn't a git repository yet, the agent runs `git init`.

## 4. Talk

Now talk. You lead: the subject, the form and the pace are yours. Expect three things that may surprise you.

- **The agent will check what you meant.** If a sentence of yours could be read two ways, it rephrases it in one line and asks you to confirm before writing it down. That is deliberate: the notes should say what *you* meant, not what sounded best.
- **It won't write after every exchange.** It writes a note only when something substantial appears. Several exchanges with no files changing is normal.
- **It tells you when it disagrees.** Ask for its opinion and you get one, reservations included.

When it does write, the notes go in `corpus/`. Each note opens with **Current**, what holds today, followed by **History**, how you got there. Claims are marked with who made them: your git id for you, the model's name for the agent.

```
- **[alice]** The tool must work offline.
- **[opus-5]** Then sync is the hard part, not storage.
- **[opus-5 → alice]** Sync is designed first.
```

A marker with only the agent's name is a proposal you haven't accepted. Once you agree, it gets your name after the arrow.

## 5. Change your mind

Just say so: *"Actually, I don't want it to work offline."* This is the part the method is built for. The agent:

1. looks through the corpus, and any deliverables, for everything that is now false, and corrects it;
2. records the reversal in `corpus/decision-log.md`, marked **↺**, with what it replaces and why.

The old line stays in the log. Months later you can still see what you thought, when, and why you stopped thinking it.

## 6. Let later sessions find it

Once the subject is clear, the agent offers to add one line to the folder's `CLAUDE.md`: *"This folder is a maieutics project about…"*. Say yes. Later sessions will then recognise the project without being told.

## 7. Stop, and come back

Close the session whenever you like. Nothing is lost, because it's all in the files.

When you come back, open Claude Code in the same folder and type `/maieutics` again. Once the `CLAUDE.md` line is there, just starting to talk is usually enough too. This time the agent reads the corpus and tells you:

- what the project is and the idea it revolves around;
- where things stand: how many notes, how many decisions, which deliverables, which open questions;
- the most pressing point.

Then it stops and lets you choose what comes next. The suggested sentence is now *"Let's take up the most pressing point."*

## 8. When it's ripe

The agent never produces a deliverable on its own initiative. When **you** judge the corpus good enough, ask for one by naming the genre:

> *I think we have enough. Write a two-page proposal for my manager.*

It goes in `partus/`. A deliverable is a **starting point**, solid enough to build on, not a finished text. One corpus can yield several.

After a deliverable, the agent may suggest a **blind reading**: a fresh agent reads the deliverable without the corpus and writes down the questions it leaves open. Then it reads the corpus and checks which of those the corpus answers. What neither answers shows you what's missing.

## What you end up with

```
my-subject/
  CLAUDE.md                  one line, so later sessions recognise the project
  corpus/
    00-…-index.md            how the project works, and one line per note
    …-glossary.md            the project's terms, once there are any
    author-intent.md         what you are really after, in your words
    decision-log.md          every decision and reversal
    prompt-log.md            what you said, newest first, if you chose (c)
    NN-type-subject.md       the notes
  partus/                    the deliverables
  instrumenta/               scripts, if the subject needs calculations
  archive/                   abandoned notes and superseded versions
```

## Next

Some of the method's tools only run when you ask for them: the audits, a devil's advocate, pruning, exploring an old idea on a branch, and running a project by proxy with `metamaieutics`. They're all in the **[guide](guide.md)**.
