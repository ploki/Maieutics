# 06 — The English skill

## Current
- **[ploki]** `SKILL.md` is **translated into English**, and is authoritative.
- **[ploki]** **`SKILL.fr.md` is a French translation kept in step with `SKILL.md`** (2026-10-03). The French original moves to `archive/maieutique-SKILL-original.fr.md`. **The same for `metamaieutics`**: its original moves to `archive/metamaieutique-SKILL-original.fr.md`.
  - ↺ *Until then `SKILL.fr.md` was the frozen French original. It had drifted into another, older skill — and its banner step was the one that turned out right (note 03, decision #35).*
  - **[opus-5.5]** The translation translates prose only: file names, directories and markers stay exactly as in English, so a corpus is portable across languages.
- **[opus-5.5 → ploki]** **Everything structural stays in English, whatever the user's language**: file and directory names, section headings (*Current*, *History*, *Open questions*) and provenance markers. Only the conversation and the body of the notes follow the user. Both `SKILL.md` and `SKILL.fr.md` say so (decision #42).
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
7. **The banner remains in French**, including the Theaetetus quotation. It is the only genuinely localised asset (note 02).

## Still open
- Nothing at present. *(The question of French markers for a French user was settled on 2026-10-03: English structure throughout.)*

## History
- 2026-10-03 — Translation done; the prompt log reversed.
- 2026-10-03 — ploki settled the open question: everything structural in English, headings included.
