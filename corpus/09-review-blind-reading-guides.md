# 09 — Blind reading of the getting started and the guide

## Current
- **[ploki]** Blind reading requested on `partus/getting-started.md` (GS) and `partus/guide.md` (G), 2026-10-03.
- Stage 1 done: 81 questions, recorded below unaltered. Stage 2 (grading against the corpus and the skills) pending.

## Open questions
- Grading A / P / N, and the follow-up list, to come.

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
