# Maieutics — corpus index

**This is a maieutics project about the maieutics skill itself.** The method is used to design the thing that defines the method.

## How this project works
We talk. Substance gets written down as notes. Every structural decision and every change of mind goes in the decision log. When the author judges the corpus good enough, we produce deliverables, which can then be handed to a blind reader.

## Conventions
- Notes are `NN-type-subject.md`. `NN` is creation order, not hierarchy. Types: framing, concept, case, source, hypothesis, objection, decision.
- Every note opens with a **Current** section (what holds today), followed by the **History** of the reasoning.
- **Provenance markers name their source.** In this project:
  - **`[ploki]`** — Guillaume Gimenez, from the git identity;
  - **`[opus-5]`** — Claude Opus 5, the agent; unvalidated when it stands alone;
  - **`[opus-5.5]`** — Claude Opus 5.5, the agent from the session of 2026-10-03 onwards; same rules;
  - **`[opus-5 → ploki]`** — proposed by the agent, validated by ploki;
  - **`[S]`** a cited source · **`[Unverified]`** an unsourced fact;
  - **`[opus-5 as ploki]`** — decided by proxy, during a `metamaieutics` session.
- Versioning: git, one commit per iteration, plus `prompt-log.md`, a clean rewrite of every author message, **newest first**.

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

## Deliverables
- `README.md` at the root — the shop window: tagline, the copyable install prompt, what the skill is for, the layout.
- `partus/maieutics/` and `partus/metamaieutics/` — both skills. First received as installed on 2026-10-03, worked on here since: **this repository is the source** (note 04). See `partus/README.md`.

## Notes
| Note | Status | Summary |
|---|---|---|
| 01-reference-glossary.md | living | Project terms |
| 02-framing-multilingual.md | in force | What published skills do about languages; **English only** — no translations of the skill, the banner or the README; the conversation follows the user |
| 03-framing-banner.md | in force | Why the banner was slow; `cat` is hidden by Claude Code, so the agent reproduces a small buste with spaces for blank cells (1 320 → 188 Braille characters); the full one archived |
| 04-decision-working-rule.md | in force | The installed skill is never touched here; `partus/` is the source and holds the installable shape; the agent refreshes the installation only on request |
| 05-framing-front-door.md | in force | How a visitor is meant to arrive: the README invites them to have their own agent read the skill before installing it |
| 06-decision-english-skill.md | in force | The skill in English, and only in English; what translating it out of French had to decide, markers above all |
| 07-decision-identity.md | in force | Who said what: the human by git id, the agent by model name |
| 08-framing-contribution.md | in force | Freedom and contribution. **No specialisation: thought is general**; it forms during the exercise. Corrections come back by pull request |
