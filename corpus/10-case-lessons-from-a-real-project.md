# 10 — Case: seven lessons from a real project

## Current

- **[opus-5]** The evidence `CONTRIBUTING.md` asks a contributor for exists: a **maieutics project run over a single day**, outside this repository, on building a hard-SF world. Its own figures, counted: **186 decisions, 27 of them reversals; 104 logged author messages; 20 live notes and 4 archived; one deliverable; three scripts; three successive consistency audits and one exhaustivity audit**. It ran on an earlier marker scheme — `[G]` for the author, `[C]` for the agent — the ancestor of the named markers of note 07.
- **[opus-5]** It was not run to test the skill. The seven lessons below are **failures it suffered**, each one caught late, several caught only by an audit. They are instructed here one by one: what happened, what the skill says today, and what it should say. The skill changes they led to are decisions #50–#55.
- **[opus-5]** The through-line: the method is good at recording what the user decides and bad at noticing what the *agent* has quietly added, dropped or failed to propagate. Six of the seven lessons are about the agent's own output, not the user's.

### 1. The agent's own proposals harden into facts

- **What happened.** From one ambiguous sentence of the author's about the silicon AIs taking the humans' side, the agent inferred a "disagreement between the silicon AIs and the spheres". It wrote the inference down, repeated it from note to note, and by the time a narrative deliverable was produced it had become "the heart of the story", present in five notes and in the author's own intent file. The author stopped it with *"where does this disagreement come from? It doesn't ring a bell."* Removing it took one decision and six files (#128 there). Two more inventions of the same kind were caught later: an era boundary the author never set (#171), and a date built out of a duration he had given.
- **What the skill says today.** §2 has **No principle of charity** — but it is aimed at *the user's* sentences: reformulate an ambiguity and have it confirmed. The marker table already says that `[opus-5]` alone means *proposed, not yet validated*. Nothing forbids the agent from then building on its own unvalidated line, and nothing says an unvalidated line may not travel into a deliverable.
- **[opus-5] What it should say.** The no-charity rule applies in both directions. Carried into the skill by decision #52, as two sentences in §2: a reading of the agent's own stays marked as its own, and is not used as a premise, repeated as settled, or carried into a deliverable, until the user validates it.
- **[opus-5] The place that project invented for this.** A note of its own, `17-eclairages.md`, holding the agent's readings explicitly *not* validated as facts, so that they can be reconsidered later and so that one notices if they drift out of line with the corpus. It worked — it is where the inventions were parked instead of leaking. **Instructed in note 11 and retained**: the convention enters the skill as an optional `glosses.md`, offered rather than opened by default (decisions #56–#57). The reason is this very lesson: §2 now forbids the agent to build on a reading of its own and gives it nowhere else to go.

### 2. The agent marks as the user's what is its own

- **What happened.** Found by **all three** audits of that project. First pass: "markers wrongly placed". Second: four `[G]` markings "too generous, brought back to `[C]`" (#121). Third: five more, among them the ending "as the author poses it", a finite lifespan, and a denial about emotions (#168). Three times, on the same corpus, the agent had signed its own inferences with the author's name.
- **What the skill says today.** §2 says to keep track of who said what, by name, and gives the marker table. It says how to *form* a marker. It never says which way to err.
- **[opus-5] What it should say.** One sentence, the default when in doubt: never attribute to the user what you inferred, reformulated or completed — mark it yours and ask. Carried in by decision #53. It is cheap, and it is the only one of the seven that three independent audits each found again.

### 3. A reversal is propagated to its note and not to its relays

- **What happened.** The most repeated failure of the project. A reversal was dutifully applied to the note it concerned, and left standing in: the **index**, the **glossary**, the **author's intent file**, the **headers of other notes**, the **Open questions** sections, and the **deliverable already written**. The second audit's sixteen corrections are almost all of this kind — "propagating the stasis and the neutrality into notes 09, 11, 15, 16, the index, the glossary, the intent and the éclairages" (#167). Two reversals had emptied a deliverable of its premise without the deliverable being touched (#126, #132).
- **What the skill says today.** §5 has the right instruction and only the instruction: *"When the user changes their mind, hunt through the corpus and the deliverables for everything this makes false, correct it, and then record the reversal."* An agent reads that, corrects the note the reversal is about, and believes it has complied.
- **[opus-5] What it should say.** Name the relays. The failure is not of will but of imagination: the agent does not think of the glossary. Carried in by decision #51, as a half-sentence listing them, plus the explicit statement that correcting the note concerned is not enough.

### 4. The agent does not check its own batches

- **What happened.** Twice, in two different projects. **Here**: a script failed silently in the middle of a batch — decisions #18 to #21 were never written to the log, and the `-ics` rename was not propagated to twelve paths. Discovered only by the first audit (#22). Later a blanket `sed`, run to fix that very audit, rewrote the author's own words in the prompt log; the verification pass caught it (#23). **There**: the two logs have holes nobody ever noticed — decisions **#127** and **#185** and author message **#82** were given numbers and never written; they appear in no commit of that repository. Three audits missed them, because an audit compares content and no one was counting.
- **What the skill says today.** Nothing. §5 forbids retrofitting the logs, which is the rule the `sed` broke, but the skill never asks the agent to look at what its own edits actually did.
- **[opus-5] What it should say.** One bullet in §2: after a batch, and above all after a script, re-read the result and count — a half-failed script leaves a corpus that is wrong in silence. Carried in by decision #54. The specific instance of counting log numbers for gaps is left to the audit prompt rather than put in the skill.

### 5. The consistency audit is the method's best tool and is barely in the skill

- **What happened.** Three passes on that corpus: **22, 15 and 18 findings**. No other device in the method produced at that rate — the blind reading of this repository's two guides, for comparison, produced 81 questions but 13 real contradictions. The audits found the invented disagreement, the mis-signed markers, every missed relay, the dead cross-references, false counts in a deliverable, and four substantive contradictions the author alone could settle. The shape that works is specific:
  - a **fresh agent**, which has not written any of it, **read-only**, so that it reports instead of patching;
  - told the **semantics of the markers** — a line in the agent's name is a proposal, not a fact — and that the two logs are dated, not wrong;
  - told **what is not a finding**: a claim marked Unverified, a deliberate blank, a question left open, a log entry using superseded names. Without this the report fills with noise;
  - returning a **graded report**: contradictions, bookkeeping errors, and the points that need a decision of the user's, kept apart;
  - followed, **after the corrections**, by a **second pass by another fresh agent**. That pass is what found that the correcting sweep had rewritten the logs. The correction is more dangerous than the fault.
- **What the skill says today.** §8, first bullet: *"Re-read the whole corpus to hunt for contradictions, then resolve them point by point with the user. Do not fix anything yourself that calls for a decision of theirs."* The last clause is right. The rest leaves the agent re-reading its own work, which is exactly the thing it cannot do, and says nothing about the briefing or the second pass.
- **[opus-5] What it should say.** The recipe, compactly, in a section of its own beside the blind reading. Carried in by decision #50, which also drops that first bullet of §8 as superseded.

### 6. The exhaustivity audit is a second, different tool

- **What happened.** One pass, on the same corpus, asking a different question: not *does the corpus contradict itself* but *does the corpus match what the author actually said*. Run against `prompt-log.md`, **in both directions**. It found four omissions, including a date boundary for an era that the author had stated and that had been silently rewritten, and his explicit refusal of multiple-choice questions, which had never been recorded. Another instance of the same class, caught later: a duration the author had given ("200 years to max out H-1") had turned into an invented calendar date.
- **What the skill says today.** Nothing. The prompt log is specified in §1.3 as versioning option (c) and then never used again. A clean rewrite of every user message, losing nothing, is the one artefact that makes this check possible, and the skill does not say what it is for.
- **[opus-5] What it should say.** A short paragraph beside the consistency audit, stating the two directions and that it needs versioning (c). Carried in by decision #50. This also finally gives option (c) a reason beyond bookkeeping, which is worth saying when the user is asked to choose.

### 7. When quantities appear, compute

- **What happened.** The scripts decided the world, three times.
  - A table of growth stages, asked for by the author, revealed that the dates he had independently chosen for his world's eras **fell exactly on his character's growth stages** — a coincidence nobody had seen, which became a structural decision (#170).
  - A population script showed that the reproduction rule the author had set, left free, gives **10⁶⁵ individuals in a year**. The rule survived; the demography had to be rebuilt around industrial production of growth substrate, with an inverted age pyramid (#184).
  - A scale script turned a vague "a quarter of an inch" into a level on the size scale, which fixed the terms of reproduction.
  In each case prose had been reasoning happily about figures that did not work.
- **What the skill says today.** §3 names `instrumenta/` as the directory for *"the scripts (calculations, simulations)"*, and offers an optional register of key figures. It never says **when** to reach for them. An agent will therefore keep arguing in sentences.
- **[opus-5] What it should say.** A trigger, not a section: as soon as the subject carries quantities, write the script and run it rather than reasoning in prose, because the result is frequently a decision. Carried in by decision #55.

## What this settles [opus-5]

- **The skill's blind spot has a shape.** Sections 2 and 5 govern the user's words well and the agent's own output hardly at all. Lessons 1, 2, 3, 4 and 6 are all the same failure seen from five angles: something the agent produced was treated as more reliable than it was — its inference as a fact, its marker as attribution, its correction as complete, its script as having run, its memory of the conversation as the conversation.
- **Hence the remedy, and why it is one tool and not five rules.** No instruction makes an agent see its own gaps; another agent has to. That is why lesson 5 ranks first: the audit is the only device here that does not rely on the agent noticing.
- **The second pass is not a nicety.** In both projects the sweep that fixed the findings did more damage than the findings — it rewrote the author's words here, it left relays untouched there. Any corpus-wide correction has to be verified by someone who did not make it.

## Open questions

- **[opus-5]** Whether the audits should be *offered* at named moments, as the blind reading is, rather than only run on request. The evidence says after a reversal, after a batch of corrections, and before a deliverable; the risk is one more thing the agent proposes unbidden.
- **[opus-5]** Whether the exhaustivity audit should also cover the *reverse* direction mechanically — numbering gaps in both logs, as in lesson 4 — or whether that belongs in the audit's briefing rather than in the skill.

## History
- 2026-10-04 — The *éclairages* question of lesson 1 is instructed in note 11 and retained; it leaves the open questions here.
- 2026-10-04 — Note opened: seven failures observed in a real one-day project, instructed against the state of the skill; decisions #50–#55 carried the mature ones into `partus/maieutics/SKILL.md`.
