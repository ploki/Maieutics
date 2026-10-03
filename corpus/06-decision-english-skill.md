# 06 — The English skill

## Current
- **[ploki]** `SKILL.md` is **translated into English**, and is authoritative.
- **[ploki]** **There is no French version any more** (decision #45). Both skills exist in English only. The French originals are in `archive/maieutique-SKILL-original.fr.md` and `archive/metamaieutique-SKILL-original.fr.md`; the last French translations in `archive/maieutics-SKILL.fr.md` and `archive/metamaieutics-SKILL.fr.md`.
  - ↺ *First `SKILL.fr.md` was the frozen French original; then, the same day, a French translation kept in step with `SKILL.md`. Dropped because a translation is one more text to keep in step, and the agent already answers in the user's language.*
- **[opus-5.5 → ploki]** **Everything structural stays in English, whatever the user's language**: file and directory names, section headings (*Current*, *History*, *Open questions*) and provenance markers. Only the conversation and the body of the notes follow the user. `SKILL.md` says so (decision #42).
  - ↺ *The French translation had first translated the section names (« En vigueur » for* Current*), leaving a French corpus half one convention and half the other: French headings over `[Unverified]` markers.*
  - **[opus-5.5]** The price, accepted: a French user reads `## Current` and `[Unverified]` in their own notes. Of the markers, only `[Unverified]` and the `as` of `[opus-5 as ploki]` were English words at all; the rest are names, or `[S]`.
- **[ploki]** The **prompt log is written newest first** — prepend, not append — so that whoever picks the project back up reads the freshest entry first. The rule is in the skill; `corpus/prompt-log.md` has been reversed.

## What the translation had to decide [opus-5]
Translating instructions is not translating prose: several things could not simply be carried across.

1. **The skill's name.** The frontmatter says `name: maieutics`, so the command becomes `/maieutics`. Both directories were renamed the same day: `partus/maieutics/` and `partus/metamaieutics/`.
2. **The provenance markers.** `[G]`, for *l'utilisateur*, has no sense in English. It first became `[A]` for *author* — and then, the same day, gave way to **named ids** (note 07). `[À vérifier]` becomes **`[Unverified]`**, `[C → validé]` becomes **`[opus-5 → ploki]`**. This is the heaviest consequence of the translation: the markers appear on every line of every note, and a corpus written under one convention cannot be read under the other.
3. **The file names the skill creates.** `journal-des-decisions.md` → `decision-log.md`, `intention-de-l-auteur.md` → `author-intent.md`. The Latin directories are unaffected, which is precisely why they were a good choice: `corpus/`, `partus/`, `instrumenta/` and `archive/` read the same in both languages.
4. **The blind reading's classification.** `R / P / N` (*répondue, partiellement, non traitée*) becomes **`A / P / N`** (*answered, partially, not addressed*) — `R` would have meant nothing.
5. **"Pas de principe de charité"** is kept as *no principle of charity*: it is a term of art in philosophy of language, and it travels.
6. **Words kept untranslated**, because they carry the project's idea: *maieutics*, *partus*, *instrumenta*, and **piste**, which has no short English equivalent — *lead* is too investigative, *avenue* too grand, *thread* already taken.
7. **The banner remains in French**, including the Theaetetus quotation. It is the only genuinely localised asset (note 02). ↺ *Since localised properly: `banner.txt` in English, `banner.fr.txt` in French (note 03). Then English only (decision #45).*

## Open questions
- None at present.

## History
- 2026-10-03 — Translation done; the prompt log reversed.
- 2026-10-03 — ploki settled the open question: everything structural in English, headings included.
