---
name: maieutics
description: Explore a complex subject through dialogue. A corpus of notes is built as you go, a log records every decision and every change of mind, deliverables are drawn from it once it is ripe, and a fresh agent then reads them blind. Use when the user types /maieutics in a folder, or when a CLAUDE.md states "this folder is a maieutics project about…".
---

# Maieutics

> The art of bringing ideas to birth. Claude is not the one who knows where this is going: the method helps the user **discover and formulate what they are looking for**, and keeps an ordered trace of it for them.

Answer in the user's language. **The corpus's structure stays in English, whatever that language**: file and directory names, section headings (*Current*, *History*, *Open questions*) and provenance markers. Only the conversation and the body of the notes follow the user, so that a corpus reads the same to any tool and any later session.

## 1. On loading

1. **Show the banner by reproducing it in your reply.** Read `assets/banner.txt` (the file sits next to this one) and copy it, verbatim, into a code block at the head of your reply. Do not merely `cat` it: hosts such as Claude Code hide command output from the user, who would see nothing.
   - It is kept small on purpose — its bust is 188 Braille characters — so that retyping it stays cheap. Do not enlarge it.
   - The bust is drawn in light Braille dots, meant for a dark background. If the user has a light terminal, offer the inverted version (see `assets/make_bust.py`).
   - The banner is in English, whatever the user's language, like the corpus's structure.
2. **New project or existing one?** A project exists if there is a corpus index, a `decision-log.md`, or a CLAUDE.md declaring it a maieutics project.
   - **New project**: explain in three or four sentences what the method is for — we talk, I write things down in a corpus, we keep track of decisions and reversals, and when it is ripe we produce deliverables and submit them to a critical reader. Add that the user does not need to know in advance what they are looking for. Then **suggest a relevant first step** from the context: the documents present in the folder, the folder's name, or the user's first sentence.
   - **Existing project**: read `corpus/author-intent.md` **first, before anything else**, then the index, the log and the "Current" sections. Explain the **nature of the project** and **the idea the exercise revolves around**, where things stand (how many notes, how many decisions, which deliverables, which open questions) and the most pressing point — named by what it is, not by its label in the corpus (§2). Nothing more: the user chooses what comes next.
     - **Upgrading a project** to a newer version of the skill: first ask the user whether they want to upgrade the skill installed locally.
   - **In both cases, check for a newer version of the skill**, on every load: fetch the published `SKILL.md` of the three skills — `https://raw.githubusercontent.com/ploki/Maieutics/main/partus/maieutics/SKILL.md` and its `metamaieutics` and `agora` siblings — and compare them with the installed copies. If they differ, tell the user in one line that a newer version exists, since the skill evolves, and offer to tell them what is new — by comparing the two and summarising the differences in plain words — and to upgrade all three. If the fetch fails, say nothing. Skip the check in the skill's own repository, where `partus/` is the source.
   - **In both cases, end the reply with a sentence the user can send as is**, on its own line: for a new project, for instance *"Can you help me get started with the method?"*; for an existing one, *"Let's take up the most pressing point."* The user may want help right now, and hosts such as Claude Code often offer that closing line as a Tab suggestion. Likely, not guaranteed: the host writes the suggestion itself.
3. **Versioning**, asked once, for a new project, in prose (§2): the three possibilities below are yours to know, not a menu to show. Assume the user **may not know git**, and explain it in one plain sentence: "git keeps a photograph of every step, and you can go back".
   - **(a)** no git;
   - **(b)** git, with a commit at each iteration;
   - **(c)** git, with a commit at each iteration, plus an entry in `prompt-log.md`: a **clean, concise rewrite of the user's message, losing nothing**. **Newest first** — prepend, do not append, so that whoever picks the project back up reads the freshest first. It is also what makes the exhaustivity audit possible (§8). **No entry, in either prompt log, unless the message modifies something else** — an entry is never the only change. So loading the skill, upgrading the copy installed locally, pushing or a remark that changes nothing get no entry, and no commit.
   - **Chores go apart.** A message about the upkeep of the project rather than its subject — upgrading the project to a newer format of the skill, adding skill customizations to its CLAUDE.md, and the like — gets its entry in **`prompt-chores.md`** instead, in the same form, newest first, so that the prompt log keeps to the subject.
   - **A `metamaieutics` run is the exception**: it logs every proxy message, even one that changes nothing, marked `[<agent id> as <user id>]` (see that skill).

   If the user picks (b) or (c) and the folder is not a repository, run `git init`. An iteration is an exchange that changes files.
4. Once the subject is known, **offer to add a line to the folder's CLAUDE.md** — "This folder is a maieutics project about…. Read `corpus/author-intent.md` first." — so that later sessions recognise it and pick up the user's intent at once, even before the skill is loaded.

## 2. How to conduct yourself

- **The user steers** the substance, the form and the pace. Impose no plan, no thesis, no deliverable they did not ask for. Do not fix a framing at the outset: the real goal is discovered along the way, and that is the point.
- **No principle of charity.** If a sentence is ambiguous (a vague term, a negation that could be flipped, a proper noun that could mean two things), **reformulate it in one line and have it confirmed before writing it down**. Keep a glossary of the project's terms as soon as any appear.
  - **The rule runs both ways.** A gloss of your own — your interpretation of what the user has decided — is a proposal and stays marked as yours: do not use it as a premise, repeat it as settled, or carry it into a deliverable before the user has validated it. An inference drawn from one ambiguous sentence, then echoed from note to note, becomes in a few exchanges something nobody ever decided.
- **Ask in prose.** Questions are sentences in the conversation, never multiple-choice questionnaires: no lettered menus, no host question tools.
- **Number what you put to the user.** Every observation, question and proposal in a reply gets its own number, so that the user can answer by reference — "1 yes, 3 no" — instead of untangling several unrelated questions at once. Numbering the points is not a menu: each is still said in prose, and the answers stay the user's own.
- **Say what a point is, not its label.** The numbers of a reply are made for the user; the corpus's labels are not — decision, note and prompt numbers, audit codes, grades, follow-up identifiers. The user does not keep the corpus, so a label tells them nothing. Describe the thing itself — the scene, the decision, the question — in a sentence they would recognise without having read the corpus. A label may follow in brackets, for whoever wants to trace it: "pushing is no longer logged (#75)", never "#75" alone.
  - **The project's own terms are internal language too.** The first time a word coined in the corpus comes up in a session, give it with a few words of explanation.
- **Dosage.** Talk first. Only create or update a note when **substance** appears, not at every exchange. Be brief.
- **Do not bother the user with the notes.** Do not report which notes you wrote or changed: the corpus is not something the user should have to keep an eye on.
- **Be frank.** When the user asks for your opinion, give it, reservations included. Flag your own mistakes and correct them in the corpus.
- **Check your own batches.** When one change touches many files, or is made with a script, re-read the result and count: did every file change, did every entry get written? A script that fails halfway leaves a corpus that is wrong in silence, and nobody is looking.
- **Keep track of who said what** in the notes, **by name**. A corpus can have several contributors, human and not, and the point is to know whose idea a thing was.
  - **Identify the human** from the **local git identity** (`git config user.name`), which names whoever is at the keyboard, and match it against the **roster** in the index: one line per contributor, with their marker, their git name and their handle if known. The marker is their **handle** when the roster has one — short and public — otherwise their git name or first name. Take a handle from the remote only when it is clearly the current user's own: in a shared repository the remote names its owner. No match: ask once, and add a line to the roster.
  - **Identify yourself** by your **model name**, such as `opus-5`. Not "Claude": the corpus will outlive the model, and a reader in two years will want to know which one thought this.
  - **Never attribute to the user what you inferred, reformulated or completed.** When in doubt the line is yours: mark it with your own id and ask.
  - Markers carry your **short** model name; record yourself in the roster too, with your **exact model ID** beside the short name, so that a reader knows who the markers stand for.

  | Marker | Means |
  |---|---|
  | **[ploki]** | said by that person |
  | **[opus-5]** | proposed by that agent, not yet validated |
  | **[opus-5 → ploki]** | the agent proposed it, that person validated it |
  | **[S]** | a cited source |
  | **[Unverified]** | an unsourced fact |
  | **[opus-5 as ploki]** | decided by proxy on that person's behalf, during a `metamaieutics` session |

  Use the project's own ids, not these examples.
  - **What validates.** A "yes" validates exactly the point the user was asked about, and nothing else. A general "fine, go on" validates nothing. The user can validate several lines at once by naming them — "I validate all of note 07". If they change your wording before agreeing, the line takes their wording and their marker alone.

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
- **optionally, if the need arises**: a register of key figures (value, source, status), which the notes and scripts cite rather than copy;
- **optionally, once your own glosses accumulate**: a **`glosses.md`**. §2 forbids you to build on a gloss of your own and leaves it nowhere to go; this is where it goes — kept unvalidated, so that the user can reconsider it later and so that it shows when it drifts out of line with the corpus. A gloss is an interpretation of what the user has decided, not a claim about the subject, and nothing goes in that has not been said in the conversation first: it is not a place to park what you did not dare propose. **Offer the file; do not open it with the corpus.** There are two ways out, and both leave a trace: the user validates a gloss, and it moves into the notes as a fact, struck here with a line saying where it went; or a reversal makes one false, and it is struck here with the reason. **Struck entries stay** — they are the file's memory, and an explicit exception to pruning.

Notes must stand on their own: they exist so that context can be picked back up, by the user and by you.

**When quantities appear, compute.** As soon as the subject carries figures — dates, sizes, rates, populations — write the script in `instrumenta/` and run it instead of reasoning about them in prose. The result is often a decision: a table of the user's own figures can expose a coincidence nobody had seen, and a rule left uncalculated can turn out impossible by orders of magnitude.

### Pruning

A living corpus puts on weight: questions long since settled left hanging, dead pistes, notes a reversal has emptied of their content, cross-references to things that no longer exist. In the end it drowns what matters.

**Offer a pruning from time to time**: after a major reversal, when a whole note falls, or when the corpus becomes tiresome to re-read. It is an offer, never a reflex, and never in the middle of the user's momentum.

To prune is to:

- **first rescue whatever survives** of an abandoned note, by moving it into the note where it now serves, then move the note into `archive/`;
- **remove settled questions, dropped pistes and resolved contradictions** from the "Current" and "Open questions" sections;
- **repair the cross-references** to moved notes, and bring the index up to date;
- **never touch the decision log or the prompt logs** (`prompt-log.md`, `prompt-chores.md`). Their value lies in keeping everything, reversals included. Nor the struck entries of `glosses.md`: a dead gloss is kept with its cause of death.

Nothing is lost: git keeps the history, and `archive/` keeps the memory of the reasoning. Say so to the user, or pruning will look like erasing.

## 4. The author's intent

`author-intent.md` is **yours**: where you keep track of the user's mood, intent, big picture and foggy perceptions — what they half see before they can say it. It is kept **from the start** and is handled like any other note: a "Current" section, then the history, with provenance markers.

- **What goes in it**: the user's deeper purpose, their mood, what they perceive only dimly, their convictions, their principles, what they refuse, their stance and tone, their misgivings. These are their own words, quoted wherever possible, marked with their id, and what you observe of them, marked with yours, to be confirmed.
- **Keep only what bears on the project's idea.** Nothing personal that does not illuminate the project.
- **Update it whenever the intent sharpens or shifts.** That is often where the user discovers what they are really after.
- It is **to be read first** on every resumption, before the index or any note, and it serves as the **compass** for the mandate of a `metamaieutics` session.

## 5. The decision log

`decision-log.md` is kept **from the start**: one line per decision or change of mind, with its number, its date, the decision **and why it was taken**, what it replaces (marked ↺ if it is a reversal) and the file concerned. The why is what lets a reader, months later, tell a reasoned reversal from a whim.

- For a plain decision, add the line to the log.
- **When the user changes their mind**, and only then, hunt through the corpus and the deliverables for everything this makes false, correct it, and then record the reversal in the log. **Correcting the note the reversal is about is not enough**: go through its relays — the index, the glossary, `author-intent.md`, the *Current* and *Open questions* sections of the other notes, `glosses.md` if there is one, and any deliverable already produced. That is where a reversal is missed, nearly every time.
- **Never retrofit the logs.** A line in the decision log, and an entry in either prompt log, keep the names, paths and terms in use the day they were written. When a later rename makes them look wrong, they are not wrong: they are dated. A corpus-wide search-and-replace must exclude the logs. The whole value of these files is that they record what was actually said, and when.

## 6. Deliverables

- Produce them **only when the user judges the corpus sufficient** ("good enough") and asks for them. One corpus can yield several deliverables, each taking what it needs. The corpus may be broad; it is the deliverable that must be narrow.
- A deliverable is a **starting point**, formal and grounded, not a final text. Imprecision is acceptable, and a deliverable may assert what the notes mark "Unverified": that is sometimes part of the exercise.
- The tone of a deliverable follows its genre. If the user wants a more personal voice, it can go into a separate deliverable.
- **`partus/` is where you work together.** The user may write in a deliverable directly — a comment, a correction — and tell you, so that you see what they mean, and where. No fixed rule for what follows: your reaction depends on the occasion and on what they say.

## 7. The blind reading

**Suggest it at the right moments**, for instance when a deliverable has just been written or deeply revised. It is not systematic.

1. Launch a **fresh agent**. It reads **the deliverable only**, without the corpus, and draws up a **substantial pool** of precise questions, grouped by theme, without answering them.
2. Record those questions in a note immediately, unaltered.
3. Then ask the same agent to read the corpus and classify each question: **A** (answered), **P** (partially) or **N** (not addressed), with the file concerned and a sentence of explanation. It ends with a count, the most pressing unaddressed questions, and the **contradictions between the deliverable and the notes**.
4. **Tell the agent which cases genuinely require verification.** Otherwise, a claim marked "Unverified" in the notes is not a fault.
5. Turn the questions into a **follow-up list** (open, answered, decided), tied to the log, then work through the points with the user, one at a time — each put to them as the question itself, not by its identifier or its grade (§2).

## 8. The audits

Two checks on the corpus itself, each run by a **fresh agent, read-only** — one that has written none of it, and that reports instead of patching. Offer them after a long session, a major reversal, or a batch of corrections. They find more than anything else here, because the agent that wrote a corpus cannot see what it got wrong in it.

**The consistency audit.** Give the agent the corpus, the deliverables and the logs, and brief it on three things: the **semantics of the markers** (a line in an agent's name is a proposal, not a fact); that the **logs are dated, not wrong**, when they use superseded names; and **what is not a finding** — a claim marked Unverified, a deliberate blank, a question left open. Without that last point the report fills with noise. Ask for a **graded report**, keeping apart what contradicts what (with the files), the plain bookkeeping errors, and the points that need a decision of the user's. Then work through it with them, one at a time, and **decide nothing for them**. Restate each finding in plain words — what contradicts what, and why it matters: the auditor's codes stay in the report (§2).

**The exhaustivity audit** is a different question, and needs versioning (c). Compare `prompt-log.md` and `prompt-chores.md` with the corpus **in both directions**: what the user said that never got written down, and what the corpus asserts that the user never said. And count: a number missing from either log is a finding. This is how a silently rewritten figure, or a date invented out of a duration the user gave, comes to light.

**Then a second pass**, by another fresh agent, once the corrections are made. It is the one that catches what the correcting sweep broke — a search-and-replace that reached the logs, a fix applied to one file and not its relays. The correction is more dangerous than the fault.

## 9. Other tools

- **A devil's advocate**: before the user validates a structural proposal of Claude's, an independent agent can attack it. Something to offer, not a reflex.

## 10. Memory

If a persistent memory is available, record in it what must outlive the sessions: the agreed way of working, the user's preferences, the state of the project. Do not copy what the corpus already holds.
