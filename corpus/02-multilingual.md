# 02 — Framing: one language, or several?

## Current
- **[ploki]** The repository ships its **outputs in English**; language variants of the skill were initially meant to live in their own directories (`corpus/author-intent.md`).
- **[opus-5, to confirm]** After looking at what published skills actually do, that plan looks like the wrong shape. See below.

## What published skills do [S]
Searched 2026-10-03. The dominant pattern is **one `SKILL.md`, in English, with translated documentation beside it** — never a translated skill body.

- `ForceInjection/awesome-skills` has a standing rule: every Chinese-facing document has an English counterpart with an `-en` suffix (`README.md` / `README-en.md`, `AGENTS.md` / `AGENTS-en.md`). The translation covers the docs, not the skill instructions.
- `xiaomoBoy/claude-writing-skills` uses `README.zh-CN.md` next to `README.md` — the ordinary BCP-47 suffix convention of GitHub at large.
- `zhuyansen/awesome-claude-video-skills` and `O0000-code/awesome-academic-skills` advertise "English / 中文"; again it is the index that is bilingual.
- Fully Chinese repositories such as `claude-code-skills-zh` are **monolingual**: no English variant at all. They pick an audience.
- Where a skill is *about* translation (`translate-book`, the iOS localisation skills), what is multilingual is its **working material** — a `references/` folder holding `glossary.yaml` and `language-guide.yaml`. The skill itself stays in one language.

**No example was found of a skill shipped as several language variants of its `SKILL.md`.**

## The technical constraint [opus-5]
A skill is **one directory plus one `SKILL.md`**, with a unique `name` in frontmatter. `fr/SKILL.md` and `en/SKILL.md` inside the same skill folder are not two skills — only the root `SKILL.md` is loaded. Shipping two variants means **two skill directories with two different names**, hence two commands (`/maieutics` and `/maieutique`), double maintenance, and a split user base. **[Unverified: the exact discovery rules for nested skill folders.]**

## The argument against variants [opus-5]
A `SKILL.md` is **not a text to be read: it is instructions addressed to Claude.** The skill already carries the line that settles the matter — *"Answer in the user's language."* An English `SKILL.md` therefore produces a French project when the user writes in French. That is exactly what happened on 2026-10-03, in reverse: a French skill ran an English project.

## Proposed shape [opus-5]
- **One `SKILL.md`, in English.**
- **A translated README**, `README.fr.md`.
- **The banner, in `assets/`, with one variant per language** — it is the only genuinely localised asset.

## Still open
- **[ploki]** Is the banner the only thing to translate? *(The author's question, 2026-10-03.)*
- **The names the skill creates**: `corpus/`, `partus/`, `decision-log.md`. Fixed, they make projects recognisable and tooling reusable; translated, they are more welcoming. None of the repositories examined settles this, because none of them creates a project structure.
- **The provenance markers.** `[ploki]` stands for the user in the French skill. In English it would want to be `[A]` for author or `[U]` for user — so the markers are a localisation question too, and they appear on every line of every note.

## History
- 2026-10-03 — Opened after a web search on how published skills handle several languages.
