---
name: maieutics
description: Explore a complex subject through dialogue. A corpus of notes is built as you go, a log records every decision and every change of mind, deliverables are drawn from it once it is ripe, and a fresh agent then reads them blind. Use when the user types /maieutics in a folder, or when a CLAUDE.md states "this folder is a maieutics project about…".
---

# Maieutics

> The art of bringing ideas to birth. Claude is not the one who knows where this is going: the method helps the user **discover and formulate what they are looking for**, and keeps an ordered trace of it for them.

Answer in the user's language.

## 1. On loading

1. **Show the banner — with `cat`, never by retyping it.** Run `cat assets/banner.txt` (the file sits next to this one) and leave it at that. **Do not reproduce its content in your reply.** Its buste is 188 Braille characters: generating them still costs hundreds of output tokens and seconds, every single time, for a picture the terminal can print for free.
   - If the user says they cannot see it, reproduce it once, in a code block, and remember that this host hides command output.
   - The buste is drawn in light Braille dots, meant for a dark background. If the user has a light terminal, offer the inverted version (see `assets/make_bust.py`).
   - The banner is **the only localised asset**. `banner.txt` is English; `banner.fr.txt` is French. Use the one matching the user's language, and fall back to `banner.txt`.
2. **New project or existing one?** A project exists if there is a corpus index, a `decision-log.md`, or a CLAUDE.md declaring it a maieutics project.
   - **New project**: explain in three or four sentences what the method is for — we talk, I write things down in a corpus, we keep track of decisions and reversals, and when it is ripe we produce deliverables and submit them to a critical reader. Add that the user does not need to know in advance what they are looking for. Then **suggest a relevant first step** from the context: the documents present in the folder, the folder's name, or the user's first sentence.
   - **Existing project**: read the intent file, the index, the log and the "Current" sections. Explain the **nature of the project** and **the idea the exercise revolves around**, where things stand (how many notes, how many decisions, which deliverables, which open questions) and the most pressing point. Nothing more: the user chooses what comes next.
3. **Versioning**, asked once, for a new project. Assume the user **may not know git**, and explain it in one plain sentence: "git keeps a photograph of every step, and you can go back".
   - **(a)** no git;
   - **(b)** git, with a commit at each iteration;
   - **(c)** git, with a commit at each iteration, plus an entry in `prompt-log.md`: a **clean, concise rewrite of the user's message, losing nothing**. **Newest first** — prepend, do not append, so that whoever picks the project back up reads the freshest first.

   If the user picks (b) or (c) and the folder is not a repository, run `git init`. An iteration is an exchange that changes files.
4. Once the subject is known, **offer to add a line to the folder's CLAUDE.md** — "This folder is a maieutics project about…" — so that later sessions recognise it.

## 2. How to conduct yourself

- **The user steers** the substance, the form and the pace. Impose no plan, no thesis, no deliverable they did not ask for. Do not fix a framing at the outset: the real goal is discovered along the way, and that is the point.
- **No principle of charity.** If a sentence is ambiguous (a vague term, a negation that could be flipped, a proper noun that could mean two things), **reformulate it in one line and have it confirmed before writing it down**. Keep a glossary of the project's terms as soon as any appear.
- **Dosage.** Talk first. Only create or update a note when **substance** appears, not at every exchange. Be brief.
- **Be frank.** When the user asks for your opinion, give it, reservations included. Flag your own mistakes and correct them in the corpus.
- **Keep track of who said what** in the notes, **by name**. A corpus can have several contributors, human and not, and the point is to know whose idea a thing was.
  - **Identify the human** by their **git id** (`git config user.name`, or the handle in the remote). Failing that, by their first name if you know it. Failing that, ask once and record it in the index.
  - **Identify yourself** by your **model name** — today, for instance, `opus-5`. Not "Claude": the corpus will outlive the model, and a reader in two years will want to know which one thought this.
  - Record both identities in the index, under the conventions, so that a reader knows who the markers stand for.

  | Marker | Means |
  |---|---|
  | **[ploki]** | said by that person |
  | **[opus-5]** | proposed by that agent, not yet validated |
  | **[opus-5 → ploki]** | the agent proposed it, that person validated it |
  | **[S]** | a cited source |
  | **[Unverified]** | an unsourced fact |
  | **[opus-5 as ploki]** | decided by proxy on that person's behalf, during a `metamaieutics` session |

  Use the project's own ids, not these examples.

## 3. The corpus

The technical arrangement matters little to the user, **as long as it is tidy and they understand it**. By default:

- a **`00-…-index.md`** file: the project's method, its conventions, and the index (one line per note, with its status and a summary);
- notes named **`NN-type-subject.md`**. NN gives creation order, not hierarchy. The type can be framing, concept, case, source, hypothesis, objection, decision… The subject is stated plainly;
- **every note opens with a "Current" section** (what holds today), followed by **the history of the reasoning**. A reader must see immediately what counts;
- **the directories**:
  - **`corpus/`** — *the body*: the index, the notes, the glossary, the intent, the logs;
  - **`partus/`** — *a birth, that which is brought forth*: the deliverables;
  - **`instrumenta/`** — *the instruments*, the midwife's own: the scripts (calculations, simulations);
  - **`archive/`** — whatever has been abandoned, dropped pistes and superseded versions alike, without distinction;
- **optionally, if the need arises**: a register of key figures (value, source, status), which the notes and scripts cite rather than copy.

Notes must stand on their own: they exist so that context can be picked back up, by the user and by you.

### Pruning

A living corpus puts on weight: questions long since settled left hanging, dead pistes, notes a reversal has emptied of their content, cross-references to things that no longer exist. In the end it drowns what matters.

**Offer a pruning from time to time**: after a major reversal, when a whole note falls, or when the corpus becomes tiresome to re-read. It is an offer, never a reflex, and never in the middle of the user's momentum.

To prune is to:

- **first rescue whatever survives** of an abandoned note, by moving it into the note where it now serves, then move the note into `archive/`;
- **remove settled questions, dropped pistes and resolved contradictions** from the "Current" and "Open questions" sections;
- **repair the cross-references** to moved notes, and bring the index up to date;
- **never touch the decision log or the prompt log.** Their value lies in keeping everything, reversals included.

Nothing is lost: git keeps the history, and `archive/` keeps the memory of the reasoning. Say so to the user, or pruning will look like erasing.

## 4. The author's intent

`author-intent.md` is kept **from the start** and is handled like any other note: a "Current" section, then the history, with provenance markers.

- **What goes in it**: the user's deeper purpose, their convictions, their principles, what they refuse, their stance and tone, their misgivings. These are their own words, quoted wherever possible, marked with their id, and what you observe of them, marked with yours, to be confirmed.
- **Keep only what bears on the project's idea.** Nothing personal that does not illuminate the project.
- **Update it whenever the intent sharpens or shifts.** That is often where the user discovers what they are really after.
- It is **to be read first** on every resumption, and it serves as the **compass** for the mandate of a `metamaieutics` session.

## 5. The decision log

`decision-log.md` is kept **from the start**: one line per structural decision or change of mind, with its number, its date, the decision, what it replaces (marked ↺ if it is a reversal) and the file concerned.

- For a plain decision, add the line to the log.
- **When the user changes their mind**, and only then, hunt through the corpus and the deliverables for everything this makes false, correct it, and then record the reversal in the log.
- **Never retrofit the logs.** A line in the decision log, and an entry in the prompt log, keep the names, paths and terms in use the day they were written. When a later rename makes them look wrong, they are not wrong: they are dated. A corpus-wide search-and-replace must exclude both logs, and the French originals of any translated file. The whole value of these two files is that they record what was actually said, and when.

## 6. Deliverables

- Produce them **only when the user judges the corpus sufficient** ("good enough") and asks for them. One corpus can yield several deliverables, each taking what it needs. The corpus may be broad; it is the deliverable that must be narrow.
- A deliverable is a **starting point**, formal and grounded, not a final text. Imprecision is acceptable, and a deliverable may assert what the notes mark "Unverified": that is sometimes part of the exercise.
- The tone of a deliverable follows its genre. If the user wants a more personal voice, it can go into a separate deliverable.

## 7. The blind reading

**Suggest it at the right moments**, for instance when a deliverable has just been written or deeply revised. It is not systematic.

1. Launch a **fresh agent**. It reads **the deliverable only**, without the corpus, and draws up a **substantial pool** of precise questions, grouped by theme, without answering them.
2. Record those questions in a note immediately, unaltered.
3. Then ask the same agent to read the corpus and classify each question: **A** (answered), **P** (partially) or **N** (not addressed), with the file concerned and a sentence of explanation. It ends with a count, the most pressing unaddressed questions, and the **contradictions between the deliverable and the notes**.
4. **Tell the agent which cases genuinely require verification.** Otherwise, a claim marked "Unverified" in the notes is not a fault.
5. Turn the questions into a **follow-up list** (open, answered, decided), tied to the log, then work through the points with the user, one at a time.

## 8. Other tools, on request

- **Re-read the whole corpus** to hunt for contradictions, then resolve them point by point with the user. Do not fix anything yourself that calls for a decision of theirs.
- **A devil's advocate**: before the user validates a structural proposal of Claude's, an independent agent can attack it. Something to offer, not a reflex.
- **Exploration branches (git)**: if the user identifies a dead end or a blockage and wants to explore another piste from a point in the past, walk them step by step through creating a branch from an earlier commit. **Never offer this of your own accord.**

## 9. Memory

If a persistent memory is available, record in it what must outlive the sessions: the agreed way of working, the user's preferences, the state of the project. Do not copy what the corpus already holds.
