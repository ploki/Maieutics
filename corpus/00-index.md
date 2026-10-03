# Maieutics — corpus index

**This is a maieutics project about the maieutics skill itself.** The method is used to design the thing that defines the method.

## How this project works
We talk. Substance gets written down as notes. Every structural decision and every change of mind goes in the decision log. When the author judges the corpus good enough, we produce deliverables, which can then be handed to a blind reader.

## Conventions
- Notes are `NN-type-subject.md`. `NN` is creation order, not hierarchy. Types: framing, concept, case, source, hypothesis, objection, decision.
- Every note opens with a **Current** section (what holds today), followed by the **History** of the reasoning.
- Provenance markers: **[G]** the author · **[C]** Claude, unvalidated · **[C → validated]** · **[S]** a cited source · **[Unverified]** · **[P]** decided by proxy during a `metamaieutics` session.
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
- `partus/maieutique/` and `partus/metamaieutique/` — both skills, received as installed on the author's machine on 2026-10-03. A snapshot, not the live copy. See `partus/README.md`.

## Deliverables
| Note | Status | Summary |
|---|---|---|
| 01-glossary.md | living | Project terms |
| 02-multilingual.md | framing | What published skills do about languages; one `SKILL.md` in English, translated README, localised banner |
| 06-the-english-skill.md | **in force** | The English `SKILL.md`; what the translation had to decide, markers above all |
| 05-the-front-door.md | **in force** | How a visitor is meant to arrive: the README invites them to have their own agent read the skill before installing it |
| 04-working-rule.md | **in force** | The installed skill is never touched here; `partus/` is the source; only the running session's behaviour adapts |
| 03-the-banner.md | framing | Why the banner is slow (1 320 Braille characters through the LLM) and what could be done |
