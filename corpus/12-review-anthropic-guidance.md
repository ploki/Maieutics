# 12 — Review: the skills against Anthropic's authoring guidance

## Current
- **[ploki]** The skills checked against Anthropic's own guidance for writing skills, "Skill authoring best practices" [S] (platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices, read 2026-10-06), rather than adopting one rule from it on its own.
- **[opus-5.5]** Overall the skills conform: frontmatter valid, descriptions well under 1 024 characters, bodies far under 500 lines (149 and 97), no nested references, no Windows paths.
- **Adopted** (decision #108):
  - **[opus-5.5 → ploki]** Metamaieutics no longer points at `~/.claude/skills/maieutics/SKILL.md`, which only exists for a hand install; it names the `maieutics` folder beside its own, wherever the two are installed, and the orchestrator gives the agent the full path.
  - **[opus-5.5 → ploki]** The model-name example no longer says "today": a model name *such as* `opus-5`. The guidance warns against time-sensitive text, and "today" was already a version behind.
  - **[opus-5.5 → ploki]** "Buste", left over from the French, becomes "bust" in the skill, the getting started, `partus/README.md` and the notes. Logs and archive untouched.

## Open questions
Recorded at ploki's request, not acted on. All **[opus-5.5]**.
- **Testing.** The guidance asks for at least three written evaluations and for testing on Haiku, Sonnet and Opus. Neither has been done; as far as the record shows, the skill has run on Opus only. Real projects, blind readings and audits are this project's equivalent of its "Claude A writes, Claude B uses" loop, but a smaller model may follow rules such as "a general 'fine, go on' validates nothing" far less reliably. The one finding about quality rather than tidiness.
- **The descriptions.** The guidance wants them in the third person ("Explores…", not "Explore…"); ours are imperative. It also wants each to say when to use the skill: maieutics does; metamaieutics names only `/metamaieutics`, so the host never starts it from a plain request — possibly a choice, given what a run does, but not recorded as one.
- **Mixed terms.** The skill says "user" 57 times and "author" 5, the latter around the author's intent; metamaieutics names one party "Claude", "you" and "the orchestrator". The guidance asks for one term throughout. Minor.
- **The banner script.** The skill points at `make_bust.py` without saying whether to run or read it, without naming Pillow (only the getting started does), and the script writes into the installed skill's own folder. At most, "needs Pillow" in the skill.
- **Where the guidance does not fit.** "Claude is already very smart" asks to cut every explanation not needed; the skill gives a reason for almost every rule. The agent's view: keep them — the reasons are what let the agent handle the cases a rule does not cover, and they suit the author's dislike of over-specification. Splitting into reference files is not needed at this length.

## History
- 2026-10-06 — ploki proposed a check: any reference file over 100 lines in the skills gets a contents list matching its headings. **[opus-5.5]** It would find nothing: the skills have no reference files, and the rule (from the same guidance) is for files the agent previews partially. ploki withdrew it — "forget about what I said" — and asked to look at the guidance itself. The review followed; points 2, 4 and 5 adopted, the rest recorded here (#108).
