# 09 — Blind reading of the getting started and the guide

## Current
- **[ploki]** Blind reading requested on `partus/getting-started.md` (GS) and `partus/guide.md` (G), 2026-10-03.
- Stage 1: 81 questions, recorded below unaltered. Stage 2: graded against the skills and the corpus — **A 12 · P 39 · N 30**.
- **[opus-5.5]** The main finding is not the gaps but **13 places where the pages misdescribe the skills** (C1–C13 below), mostly by overstating them. Several are inherited from the skill itself (C5, C8, C13).
- The blind reader also caught a bookkeeping error of the agent's: decision #45 written twice in the log, a stray copy after #39. Removed (decision #47).

## Follow-up list
Status: **open** · answered · decided. Tied to the decision log by number once settled.

**Contradictions between the pages and the skills** (GS = getting-started, G = guide, MS / MMS = the two `SKILL.md`)
| # | Point | Status |
|---|---|---|
| C1 | GS §2: plain speech mentioning the method starts the skill. MS triggers on `/maieutics` or the CLAUDE.md line only | answered — page fixed (#48) |
| C2 | GS §3: "the agent sets one up" reads as unconditional; MS: `git init` only under (b) or (c) | answered — page fixed (#48) |
| C3 | Note shape: GS says Current + History, G says Current + Open questions + History; MS requires only Current then history | decided — no: Open questions stays optional; G fixed (#48) |
| C4 | GS §4, G §3: "every claim" is marked. MS: keep track of who said what; the corpus has unmarked lines | answered — page fixed (#48) |
| C5 | GS §5: the log shows "why you stopped thinking it". MS §5: the log line has no reason field | decided — yes: the log records why (#48) |
| C6 | GS §8: the blind reader "lists everything it couldn't understand"; MS §7: a pool of questions, then A/P/N grading | answered — page fixed (#48) |
| C7 | G §8: *you* tell the agent which claims need verifying; MS §7.4: the orchestrating agent tells the blind reader | answered — page fixed (#48) |
| C8 | G §10 "tools you have to ask for" includes memory (automatic, MS §9, now §10) and the devil's advocate (offered, MS §8, now §9) — MS has the same tension | decided — §9 and the guide's §10 no longer claim "on request"; the offers in §7, §8 and §9 stay as they were; the exploration-branch rule is dropped, git being the user's discretion (#64, corrected by #65) |
| C9 | G §11: nothing sent to an outside service; MMS §2: read-only web search stays allowed | answered — page fixed (#48) |
| C10 | G §11: approving the mandate is "your only step"; MMS also offers `git init`/a first commit, has the intent file approved with the mandate, and reuses an already-approved mandate | answered — page fixed (#48) |
| C11 | GS and G present `01-reference-glossary.md` as the default; MS names no glossary file | answered — page fixed (#48) |
| C12 | GS: "the agent explains the method as it goes"; MS gives a 3–4 sentence opening; note 05 says the on-request tools are otherwise never learnt | decided — no: pages no longer promise it (#48) |
| C13 | GS: the agent offers an inverted banner; none ships, `make_bust.py --invert` needs Pillow and outputs the buste without the title; note 03 still has it as an open question | decided — no inverted banner shipped (#48) |
| minor | G §10 "needs (b) or (c)", G §13 "Where are we?", G §7 "name the genre and the reader" — unsupported by MS but harmless | answered — reworded (#48) |

**Most pressing unaddressed questions for a newcomer** (the reader's ranking)
| # | Question | Status |
|---|---|---|
| Q29 | How a proposal gets validated, `[opus-5]` → `[opus-5 → me]` | decided — a "yes" validates exactly the point asked; a general assent validates nothing; a batch only when named; a reworded line takes the user's marker alone (#80) |
| Q2 | Plain speech or `/maieutics`? (= C1) | answered with C1 (#48) |
| Q38, Q45 | Will the agent rewrite a deliverable edited by hand; which wins, corpus or deliverable | decided — no fixed rule: `partus/` is a shared workspace; the user writes in it and says so, and the agent's reaction depends on the occasion (#81) |
| Q80 | How the user knows a note was written | decided — the agent doesn't report on the notes; the user is not to be bothered with them (#82) |
| Q37, Q42 | What counts as "structural"; is the reason for a reversal recorded (= C5) | partly — the reason is recorded (C5, #48); what counts as structural is still open |
| Q11 | Who authors commits, what they say, is anything pushed | open |
| Q10 | Changing the versioning option later | open |
| Q65, Q73 | Interrupting a metamaieutics run; must the session stay open | open |
| Q67 | Accepting or rejecting `[x as me]` decisions after handback | open |
| Q60 | Exploration branch: finding the commit, rejoining | decided — no longer specified: branching is the user's discretion, and the agent knows git (#64) |
| Q40 | How a log corrects its own errors — made concrete by the duplicate #45 | open |

## Grades [opus-5.5, the same fresh agent, after reading the skills and the corpus]
A — answered · P — partially · N — not addressed. "absent from GS/G" means the skill answers it but the pages don't say.

| Q | | Where | Note |
|---|---|---|---|
| 1 | P | README, 04 | Per-user install implied, never stated; metamaieutics install not mentioned |
| 2 | P | MS | Triggers: `/maieutics` or the CLAUDE.md line (C1) |
| 3 | P | MS | CLAUDE.md line meant to trigger; GS §7 doesn't say typing is optional |
| 4 | P | MS §1.2 | Documents only seed the first step |
| 5 | N | | |
| 6 | A | MS §1.2 | "Likely, not guaranteed"; GS only says "often" |
| 7 | P | README, 03 | What it depicts, not what it's for; no off switch |
| 8 | N | | |
| 9 | N | | |
| 10 | P | MS §1.3, MMS §3.3 | Asked once; metamaieutics skips it; absent from GS. Changing later not covered |
| 11 | P | MS §1.3 | Iteration defined; authorship, messages, pushing not |
| 12 | P | MS §1.3 | `git init` only under (b)/(c) (C2) |
| 13 | N | | "costs you nothing" unbacked |
| 14 | N | MS §1.3 | Same tension in MS |
| 15 | A | MMS §1.3 | Folder must be versioned; absent from G |
| 16 | N | | |
| 17 | P | MS §3 | C3 |
| 18 | P | 00 | Index and glossary names unspecified in MS (C11) |
| 19 | N | | |
| 20 | P | MS §3 | List open; who picks, not said |
| 21 | P | 00 | Statuses in use, undefined |
| 22 | A | MS §4, §5, §2 | Intent and log from the start, glossary when terms appear; absent from GS/G |
| 23 | N | | |
| 24 | P | MS §1.2, §3 | Resumption needs an index, a log or the CLAUDE.md line |
| 25 | A | 06 item 6 | Deliberate; undefined in the pages and the glossary |
| 26 | P | 01, #6 | Why answered; telling apart not |
| 27 | P | MS §2, 07, 00 | Open in note 07 |
| 28 | P | 07 | Open in note 07 |
| 29 | N | | |
| 30 | N | | |
| 31 | N | | Combined in practice (note 03) |
| 32 | P | 07 | Motivation, not mechanics |
| 33 | P | 00 | Practice, no rule |
| 34 | P | MS §2, §4, MMS §3 | Deliverables not addressed |
| 35 | P | MS §4, MMS §2 | From the start; absent from the pages |
| 36 | P | MS §4 | Timing and privacy not addressed |
| 37 | N | | |
| 38 | N | | |
| 39 | A | MS §5, log | |
| 40 | N | | The log's duplicate #45 shows the gap |
| 41 | P | MS §1.3 | Decision log order unspecified |
| 42 | N | MS §5 | C5 |
| 43 | N | | |
| 44 | P | MS §6 | Flagging not addressed |
| 45 | N | | |
| 46 | N | | |
| 47 | P | MS §6 | |
| 48 | N | | |
| 49 | A | MS §7 | G accurate, GS oversimplifies (C6) |
| 50 | P | MS §7.3 | Same agent confirmed, no reason given |
| 51 | P | MS §7.2, 09 | |
| 52 | P | MS §7.5 | Mechanics unspecified |
| 53 | N | | |
| 54 | N | | |
| 55 | P | MS §3, 03, 06 | History gets a "Pruned" entry in practice |
| 56 | P | #43 | Logged in practice |
| 57 | P | MS §3 | |
| 58 | N | | |
| 59 | P | MS §9 (was §8) | C8 |
| 60 | N | | |
| 61 | A | MS §10 (was §9) | Memory automatic (C8) |
| 62 | N | | |
| 63 | A | MMS Roles, §3–4 | Mostly absent from G |
| 64 | P | MMS §3.2, §6 | On the branch; path implied |
| 65 | N | | |
| 66 | P | MMS §4 | One loop turn, one commit |
| 67 | N | | |
| 68 | A | MMS §4.3–4.4 | Prompt log + one commit per iteration; absent from G |
| 69 | P | MMS §3.1 | |
| 70 | P | MMS §2 | C9 |
| 71 | P | MMS §1–3 | Corpus creation implied |
| 72 | P | MMS §3.1 | `../<folder>-meta`; memory caveat absent from G |
| 73 | N | | |
| 74 | A | MMS | `/metamaieutics` only |
| 75 | P | MS | Logs, glossary, deliverables unspecified |
| 76 | N | | |
| 77 | A | README, CONTRIBUTING | Relative link works only in the repository |
| 78 | A | MS §1.2, 05 | C12 |
| 79 | P | MS §2 | Logging of corrections not addressed |
| 80 | N | | |
| 81 | N | | |

## Questions from the blind reader, unaltered [opus-5.5, fresh agent, deliverables only]

**A. Installation, invocation and triggering**
Q1. GS intro and §1: the page says "if you haven't installed the skill yet, see the README". Is the skill installed per user or per project, and does `metamaieutics` need a separate install?
Q2. GS §2: is "just say what's on your mind and mention the method" enough to trigger the skill without typing `/maieutics`? What exact wording is needed, and what happens if the method isn't mentioned?
Q3. GS §6 and §7: once the `CLAUDE.md` line exists, "later sessions will recognise the project without being told". So why does §7 still tell you to type `/maieutics` again when you come back? Is it needed or not?
Q4. GS §1: what does the agent do with existing material in the folder (notes, PDFs)? Does it read it, move it into `corpus/`, convert it, or leave it alone? Is there a size or format limit?
Q5. GS §1: what happens if `/maieutics` is run in a folder that already has unrelated content, such as a code repository or an existing `CLAUDE.md`?
Q6. GS §2: who generates the "sentence you can send as is", and why does it matter that Claude Code "often" offers it as a Tab suggestion? When doesn't it?

**B. The opening and the banner**
Q7. GS §2: what is the banner for? Can it be turned off for good, not just inverted?
Q8. GS §2 and G §13: once you've said "my terminal is light", is that remembered across sessions, and where (memory, `CLAUDE.md`, the corpus)?
Q9. GS §2: the "first step to suggest" is "based on whatever is in the folder, its name, or your first sentence". What does a typical first step look like for an empty folder?

**C. Versioning and git**
Q10. GS §3: is the versioning question asked again on later sessions or in metamaieutics? Can the choice be changed later (say from (a) to (c)), and what happens to the history before the change?
Q11. GS §3: in option (b), what exactly counts as "an exchange that changes files"? Who writes the commit messages, under whose author name, and is anything ever pushed?
Q12. GS §3: "If the folder isn't a repository yet, the agent sets one up". Does it do this even under option (a)? Does it ask first? What about a `.gitignore`, or an existing repository with uncommitted work?
Q13. GS §3: "it costs you nothing" for option (c). Is there no cost in tokens, time or privacy (your messages are rewritten into a versioned file)?
Q14. GS §3 and G §6: the prompt log is described as "faithful" (GS) and "losing nothing" (G), yet it is a "short", "concise" rewrite. How can a short rewrite lose nothing? What gets dropped?
Q15. G §10 (exploration branch) needs option (b) or (c). G §11 (metamaieutics) works on a git branch. Does metamaieutics also need versioning (b) or (c)? What happens if the project chose (a)?
Q16. G §4 and G §9: the claim that "nothing is lost: git keeps every version" relies on git. What is the safety net under option (a)?

**D. The corpus structure**
Q17. GS "What you end up with" versus G §2: GS says each note has **Current** then **History**, while G lists three sections (Current, Open questions, History). Which is right?
Q18. G §2: `00-…-index.md` has an ellipsis in its name. What is the actual filename? Likewise, why is the glossary numbered `01-` while `author-intent.md` and `decision-log.md` are not?
Q19. G §2: `NN` is "creation order". Does the glossary, at `01`, take up the first note number? Do archived notes free up their numbers?
Q20. G §2: the note types are listed with "…". Is the list open, and who picks a note's type?
Q21. G §2: the index shows each note's "status". What are the possible statuses, and how does that differ from a note's **Current** section?
Q22. GS tree and G §2: when are the glossary, `author-intent.md` and `decision-log.md` created? From the very first exchange, or only when needed ("as soon as the project has terms of its own")?
Q23. G §2: where does the register of key figures live (filename, location)? Is it in the corpus, in `instrumenta/`, or somewhere else?
Q24. G §2: "the layout is a default, not a law". If you rearrange it, does the skill still recognise and resume the project correctly? Do metamaieutics and blind readings still work?
Q25. G §2: "pistes" (also in §9 and §10) is never defined. Is it a deliberate term of art, and should it be in a glossary?
Q26. G §2: `archive/` keeps "abandoned pistes and superseded versions, without distinction". Why "without distinction", and how do you tell them apart later?

**E. Markers and attribution**
Q27. GS §4 and G §3: the examples use `[opus-5]`. Is the marker the exact model ID, a shortened form, or something else? What happens to markers when the model changes mid-project?
Q28. G §3: your identity is your git id, "or your handle on the remote". Which takes precedence, and what if `user.name` contains spaces or a full name ("alice" versus "Alice Martin")?
Q29. G §3: how do you validate a proposal? Is an explicit "yes" needed per claim, or does a general agreement promote all `[opus-5]` markers to `[opus-5 → alice]`?
Q30. G §3: how are `[S]` sources cited? Where does the reference go, and does `[S]` replace the author marker or sit beside it?
Q31. G §3: can a claim be `[alice]` and `[Unverified]` at the same time? How do the source markers combine with the author markers?
Q32. G §3: how are multiple human contributors handled in practice? Can a second person join the same corpus, and how are disagreements between humans recorded?
Q33. G §3: "both identities are recorded in the index". What if the index and the markers disagree, for example after a model change?
Q34. GS §4: do the markers apply only to the notes, or also to `author-intent.md`, the logs and the deliverables?

**F. Author intent**
Q35. G §4: `author-intent.md` holds "convictions, what you refuse, your stance and your misgivings". Who writes it first, and when? Is it asked for at the start or inferred over time?
Q36. G §4: are you asked to confirm the agent's observations about you right away, or do they sit unconfirmed? Is there a privacy concern if the folder is shared or pushed?

**G. Decisions, reversals and the logs**
Q37. G §5: what makes a decision "structural" and therefore worth a log line? Who decides, and are minor decisions recorded anywhere?
Q38. G §5 versus G §9: GS §5 says the agent corrects "everything that is now false" in the corpus and deliverables. Does it ask before rewriting a deliverable you may have edited by hand?
Q39. G §5: what does a ↺ line look like in practice (format, numbering)? GS §5 and G §5 describe it slightly differently ("with what it replaces" versus "naming what it reverses").
Q40. G §5 and §6: "the log is never rewritten" and the prompt log "is never edited afterwards". What if the log itself contains a mistake, such as a wrong date or a mis-transcribed prompt?
Q41. G §6: the prompt log is newest-first, while the decision log presumably runs in number order (oldest first). Why the difference, and does it confuse a reader?
Q42. GS §5: "Months later you can still see what you thought, when, and why you stopped thinking it". Does the log record the *why* of a reversal, given that G §5 lists only number, date, decision, what it replaces and files?

**H. Deliverables**
Q43. GS §8 and G §7: what does "formal and grounded" mean in practice? Does a deliverable cite the corpus notes, carry markers, or neither?
Q44. G §7: a deliverable "may state things the notes mark Unverified, which is sometimes part of the exercise". Are those claims flagged in the deliverable, and when is it "part of the exercise"?
Q45. G §7: if you edit a deliverable by hand, does the agent sync those edits back into the corpus? Which one is authoritative afterwards?
Q46. G §7: "the corpus can be broad, each deliverable should be narrow". What does the agent do if you ask for a broad deliverable?
Q47. GS §8: the agent "never produces a deliverable on its own initiative". Does it ever suggest that the corpus looks ripe, or must the user judge that alone?
Q48. G §7 and GS tree: are deliverables versioned (v1, v2) in `partus/`, or overwritten? Do they appear in the index?

**I. Blind reading**
Q49. GS §8 versus G §8: GS says the blind reader "lists everything it couldn't understand", while G describes a two-stage process (questions, then grading against the corpus). Is the newcomer's picture in GS accurate?
Q50. G §8: in step 3, does "the same agent" mean the same fresh agent that did the blind read? Doesn't reading the corpus after its questions are already recorded make it biased? Why the same one?
Q51. G §8: in which note are the questions recorded, and with what filename or type?
Q52. G §8: "a follow-up list tied to the decision log". What does "tied to" mean concretely? Is there one log line per question?
Q53. G §8: can a blind reading be run on a corpus note or on something outside `partus/`?
Q54. G §8: what is the cost of a blind reading (time, tokens, a subagent)? Does it need any particular Claude Code feature?

**J. Pruning and the other tools you ask for**
Q55. G §9: pruning removes "settled questions" from **Open questions**. Where do they go, into **History**? Does pruning ever touch **History**?
Q56. G §9: is a prune itself recorded in the decision log? Is it committed as one step?
Q57. G §9 versus G §1: the agent "never does this unasked" yet "offers a pruning now and then". Does an offer count as asking? How is "never in the middle of your momentum" judged?
Q58. G §10: the devil's advocate is "an independent agent". Does it see the whole corpus or only the proposal? Where is its argument recorded?
Q59. G §10: "the agent may offer this, but only occasionally". Isn't that at odds with the section title "Tools you have to ask for" and "the agent won't start these on its own"?
Q60. G §10: the exploration branch is created from "that earlier commit". How does the user find the right commit, and how does the work on the branch later rejoin, or not rejoin, the main corpus and logs?
Q61. G §10: the memory entry sits under "Tools you have to ask for", but it reads as automatic. Is memory something you have to ask for? What exactly gets written there, and can you see or turn it off?
Q62. G §13: "Where are we?" isn't described anywhere else. Is it the same summary as the resume in GS §7?

**K. Metamaieutics**
Q63. G §11: in step 2 Claude drafts the mandate and in step 4 "Claude" plays your part. Is that the same session that drafted the mandate, or a subagent? Who is "the agent" that applies the method?
Q64. G §11: where are `mandate.md` and `handback-report.md` saved (root, `corpus/`, `partus/`, on the branch or on main)?
Q65. G §11: "this is your only step before the end". Can you interrupt or redirect a run in progress, and how?
Q66. G §11: what counts as one "iteration" toward the default limit of 30? How long does a typical run take, and what does it cost?
Q67. G §11: decisions by proxy are marked `[opus-5 as alice]`. When you review them afterwards, how do you accept them? Do they become `[opus-5 → alice]` or `[alice]`?
Q68. G §11: "Every exchange is logged and committed". Logged where? In the prompt log, a separate transcript, or the decision log?
Q69. G §11: the branch name uses `<subject>-<date>`. What happens if two runs happen on the same day?
Q70. G §11: the mandate forbids "sending anything to an outside service". Does that rule out web search or fetching sources, and how is it enforced, beyond being written down?
Q71. G §11: does metamaieutics work from just a brief in an empty folder (no corpus yet)? Does it then create the corpus on the branch and run the versioning question by itself?
Q72. G §11: the worktree option applies "if another session is still working in the same folder". Does Claude detect that, or must you say so? Where is the worktree created, and who cleans it up?
Q73. G §11: does the run need the Claude Code session to stay open? Does it run in the background, and does closing the terminal stop it?
Q74. G §11 and GS "Next": metamaieutics is "the companion skill". Is it started with `/metamaieutics` only, or can plain speech start it too, as with maieutics?

**L. Language, authority and consistency**
Q75. G §12: the corpus body is in the user's language but its headings and markers are in English. What about the glossary, the logs, `author-intent.md` and the deliverables? Which language are they written in?
Q76. G §12: is the prompt log a rewrite in the original language or a translation into English?
Q77. G intro: "the skill is right, and the guide needs a pull request". Where is the repository to send the pull request to? The relative link `maieutics/SKILL.md` assumes the guide sits next to the skill folder, so does the link work from an installed copy?
Q78. GS §1 and G §1: "the agent explains the method as it goes" and "you don't need to read this first". How much of what is in the guide (such as the tools you have to ask for) will the agent actually tell you about without being asked?
Q79. G §1: "When it makes a mistake, it says so and corrects the corpus". Is such a correction logged as a decision or a reversal (↺), or silently edited?
Q80. GS §4 and G §1: "Replies are short" and "it won't write after every exchange". How does the user know when a note was written? Does the agent announce it?
Q81. Both pages: neither says which Claude models or Claude Code versions the skill needs, or whether it works outside Claude Code (for example in Claude.ai or the desktop app).

## History
- 2026-10-03 — Opened; stage 1 questions recorded unaltered.
- 2026-10-03 — Stage 2 grading recorded; follow-up list drawn up.
- 2026-10-04 — ploki settled C3, C5, C12 and C13 and asked for the page errors to be fixed (#48); C8 widened to the audits after #50. Q2 and Q37/Q42 brought in line with C1 and C5, and *piste* added to the glossary (Q25), after the audit of 2026-10-04.
- 2026-10-04 — C8 and Q60 settled (#64). ↺ #64 had the agent run the blind reading, the audits and the devil's advocate unasked: the agent's own reading of ploki, which he rejected; reverted by #65. What stands: branching left to the user, and no "on request" heading.
