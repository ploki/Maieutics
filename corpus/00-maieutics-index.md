# Maieutics — corpus index

**This is a maieutics project about the maieutics skill itself.** The method is used to design the thing that defines the method.

## How this project works
We talk. Substance gets written down as notes. Every decision and every change of mind goes in the decision log. When the author judges the corpus good enough, we produce deliverables, which can then be handed to a blind reader.

## Conventions
- Notes are `NN-type-subject.md`. `NN` is creation order, not hierarchy. Types: framing, concept, case, source, hypothesis, objection, decision.
- Every note opens with a **Current** section (what holds today), followed by the **History** of the reasoning.
- **Provenance markers name their source.** The roster, one line per contributor (#100):
  - **`[ploki]`** — git name Guillaume Gimenez, handle `ploki`;
  - **`[opus-5]`** — Claude Opus 5, the agent; unvalidated when it stands alone; exact model ID not recorded at the time;
  - **`[opus-5.5]`** — Claude Opus 5.5 (`claude-opus-5-5`), in sessions from 2026-10-03; Opus 5 also worked on the project on 2026-10-04 (notes 10–11, decisions #49–#58); same rules;
  - **`[opus-5 → ploki]`** — proposed by the agent, validated by ploki;
  - **`[S]`** a cited source · **`[Unverified]`** an unsourced fact;
  - **`[opus-5 as ploki]`** — decided by proxy, during a `metamaieutics` session.
- Versioning: git, one commit per iteration, plus `prompt-log.md`, a clean rewrite of every author message that modifies something else (#78), **newest first**; messages about the project's upkeep go to `prompt-chores.md` instead (#76).

## Layout
| Directory | What's in it |
|---|---|
| `corpus/` | The written memory: this index, the notes, the glossary, the intent, the logs |
| `partus/` | The deliverables — *partus*, Latin for a birth, a delivery, that which is brought forth |
| `instrumenta/` | Scripts: calculations, simulations — *instrumenta*, the midwife's own instruments |
| `archive/` | Abandoned notes and deliverables, kept for the record |

## Tracking files
- `corpus/author-intent.md` — **read this first** on every resumption.
- `corpus/decision-log.md`
- `corpus/prompt-log.md`
- `corpus/prompt-chores.md`

## Deliverables
- `README.md` at the root — the shop window: tagline, the copyable install prompt, what the skill is for, the layout.
- `CONTRIBUTING.md` at the root — corrections welcome, domain variants declined; a contribution comes with the decision log of the project it was tried on (decision #29).
- `partus/getting-started.md` — the first session, step by step. `partus/guide.md` — everything the method does and how to ask for it, `metamaieutics` included. Both linked from the README, neither installed with the skill.
- `partus/agora/` — a third skill, first draft (2026-10-06): agora, the one project that sessions start from and return to, with a worklog of each outing (note 13).
- `partus/maieutics/` and `partus/metamaieutics/` — both skills. First received as installed on 2026-10-03, worked on here since: **this repository is the source** (note 04). See `partus/README.md`. The skill's sections, as they now stand: 1 on loading · 2 how to conduct yourself · 3 the corpus · 4 the author's intent · 5 the decision log · 6 deliverables · 7 the blind reading · 8 **the audits** · 9 other tools · 10 memory.

## Notes
| Note | Status | Summary |
|---|---|---|
| 01-reference-glossary.md | living | Project terms |
| 02-framing-multilingual.md | in force | What published skills do about languages; **English only** — no translations of the skill, the banner or the README; the conversation follows the user |
| 03-framing-banner.md | in force | Why the banner was slow; `cat` is hidden by Claude Code, so the agent reproduces a small bust with spaces for blank cells (1 320 → 188 Braille characters); the full one archived |
| 04-decision-working-rule.md | in force | The installed skill is never touched here; `partus/` is the source and holds the installable shape; the agent refreshes the installation only on request |
| 05-framing-front-door.md | in force | How a visitor is meant to arrive: the README invites them to have their own agent read the skill before installing it; then a getting started and a guide |
| 06-decision-english-skill.md | in force | The skill in English, and only in English; what translating it out of French had to decide, markers above all |
| 07-decision-identity.md | in force | Who said what: the human by local git identity matched against a roster in the index, marked by handle when known; the agent by short model name (exact ID in the roster) |
| 08-framing-contribution.md | in force | Freedom and contribution. **No specialisation: thought is general**; it forms during the exercise. Corrections come back by pull request |
| 09-review-blind-reading-guides.md | in progress | Blind reading of the getting started and the guide: 81 questions, A 12 · P 39 · N 30; 13 contradictions with the skills; follow-up list closed (#91); the other N and P questions not revisited |
| 10-case-lessons-from-a-real-project.md | in force | Seven failures observed in a real one-day project (a hard-SF world): the agent's own proposals hardening into facts, markings wrongly signed with the author's name, reversals left in their relays, unchecked batches, the two audits, and when to compute. **The audits are now §8 of the skill**; no open questions left |
| 11-decision-glosses-note.md | in force | The *éclairages* file of that project, instructed: a `glosses.md` for the agent's own readings, kept unvalidated, with two exits — promotion to a fact, or struck with its reason. **Retained**, as an optional file the agent offers; §3 and §5 of the skill. Named `glosses.md`, fixed name, no scheduled re-read (#58, #67, #68) |
| 12-review-anthropic-guidance.md | in force | The skills against Anthropic's "Skill authoring best practices": they conform; three fixes made (metamaieutics' path to maieutics, no "today", "bust"); open: no evaluations nor tests on smaller models, the descriptions, mixed terms, the banner script |
| 13-decision-agora.md | in force | `agora`, a third skill: agora, the one project sessions start from and return to, with a worklog; "hub" dropped, it is called agora (#118). Built after a successful experiment; general enough to belong (#109). Covered by the version check (#111); the experiment not written up (#112); talking to agora is talking to one's own agora (#115); first real run: the why witnessed and a question to agora told from a return, both left to the agent (#116, #117); memento while away covers agora, the draft unchanged (#119). Open: the version check for a user without agora; four points from the first run |
