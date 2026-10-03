# 06 — The English skill

## Current
- **[ploki]** `SKILL.md` is **translated into English**; the French original is kept beside it as `SKILL.fr.md`.
- **[ploki]** The **prompt log is written newest first** — prepend, not append — so that whoever picks the project back up reads the freshest entry first. The rule is in the skill; `corpus/prompt-log.md` has been reversed.

## What the translation had to decide [opus-5]
Translating instructions is not translating prose: several things could not simply be carried across.

1. **The skill's name.** The frontmatter now says `name: maieutics`, so the command becomes `/maieutics`. The directory is still `maieutique/`. **[To settle: rename the directory, and what becomes of `metamaieutique`.]**
2. **The provenance markers.** `[G]`, for *l'utilisateur*, has no sense in English. It first became `[A]` for *author* — and then, the same day, gave way to **named ids** (note 07). `[À vérifier]` becomes **`[Unverified]`**, `[C → validé]` becomes **`[opus-5 → ploki]`**. This is the heaviest consequence of the translation: the markers appear on every line of every note, and a corpus written under one convention cannot be read under the other.
3. **The file names the skill creates.** `journal-des-decisions.md` → `decision-log.md`, `intention-de-l-auteur.md` → `author-intent.md`. The Latin directories are unaffected, which is precisely why they were a good choice: `corpus/`, `partus/`, `instrumenta/` and `archive/` read the same in both languages.
4. **The blind reading's classification.** `R / P / N` (*répondue, partiellement, non traitée*) becomes **`A / P / N`** (*answered, partially, not addressed*) — `R` would have meant nothing.
5. **"Pas de principe de charité"** is kept as *no principle of charity*: it is a term of art in philosophy of language, and it travels.
6. **Words kept untranslated**, because they carry the project's idea: *maieutics*, *partus*, *instrumenta*, and **piste**, which has no short English equivalent — *lead* is too investigative, *avenue* too grand, *thread* already taken.
7. **The banner remains in French**, including the Theaetetus quotation. It is the only genuinely localised asset (note 02).

## Still open
- Renaming `partus/maieutique/` to `partus/maieutics/`, and `metamaieutique` likewise.
- Whether `SKILL.fr.md` stays in step, or is frozen as the original and allowed to drift.
- Whether a French user gets the French markers — which would mean two conventions and no portable corpus — or the English ones with a French conversation. **The second is cheaper and is what the current file implies.**

## History
- 2026-10-03 — Translation done; the prompt log reversed.
