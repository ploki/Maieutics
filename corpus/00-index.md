# Maieutics — corpus index

**This is a maieutics project about the maieutics skill itself.** The method is used to design the thing that defines the method.

## How this project works
We talk. Substance gets written down as notes. Every structural decision and every change of mind goes in the decision log. When the author judges the corpus good enough, we produce deliverables, which can then be handed to a blind reader.

## Conventions
- Notes are `NN-type-subject.md`. `NN` is creation order, not hierarchy. Types: framing, concept, case, source, hypothesis, objection, decision.
- Every note opens with a **Current** section (what holds today), followed by the **History** of the reasoning.
- Provenance markers: **[G]** the author · **[C]** Claude, unvalidated · **[C → validated]** · **[S]** a cited source · **[Unverified]** · **[P]** decided by proxy during a `metamaieutics` session.
- Versioning: git, one commit per iteration, plus `prompt-log.md`, a clean rewrite of every author message.

## Layout
All directory names are Latin, and all of them belong to the midwife's world.

| Directory | Latin | What's in it |
|---|---|---|
| `corpus/` | *the body* | The written memory: this index, the notes, the glossary, the intent, the logs |
| `partus/` | *a birth, a delivery, that which is brought forth* | The deliverables |
| `instrumenta/` | *the instruments* — in Latin medicine, the midwife's own | Scripts: calculations, simulations |
| `limbus/` | *the hem, the edge; limbo* | Abandoned ideas and pistes — what was not brought to term |
| `vestigia/` | *the traces, the footprints* | Superseded versions of deliverables — the path already walked |

**[C, to confirm]** The split between `limbus/` and `vestigia/`: ideas that were dropped go to limbo, texts that were replaced leave traces. If the author meant something else, this is the line to change.

## Tracking files
- `corpus/author-intent.md` — **read this first** on every resumption.
- `corpus/decision-log.md`
- `corpus/prompt-log.md`

## Notes
*(none yet)*
