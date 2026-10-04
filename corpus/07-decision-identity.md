# 07 — Who said what: identity in the corpus

## Current
- **[ploki]** The user should be **identified by their git id**; failing that, by their first name if the agent knows it.
- **[opus-5]** Failing both, ask once and record the answer in the index.
- **[opus-5 → ploki]** **The handle first**, then `git config user.name`: short, stable and already public, and it keeps markers readable (decision #70).
- **[ploki]** **The agent identifies itself too** — today, by its **model name**.
- **[ploki]** The reason: **a repository with several philosophers would need this. We want to track whose ideas are whose.**

### The scheme now in force
| Marker | Means |
|---|---|
| `[ploki]` | said by that person |
| `[opus-5]` | proposed by that agent, not yet validated |
| `[opus-5 → ploki]` | the agent proposed it, that person validated it |
| `[S]` | a cited source |
| `[Unverified]` | an unsourced fact |
| `[opus-5 as ploki]` | decided by proxy, in a `metamaieutics` session |

## Why this is better than single letters [opus-5]
- **It scales.** Two humans and two agents on one corpus, and the letters collapse. Names do not.
- **It survives the model.** A corpus outlives the thing that wrote it. A reader in two years wants to know *which* model thought this — `opus-5` says it, "Claude" does not. The same argument applies to the human: `ploki` is a handle that will still resolve to someone.
- **It makes attribution checkable.** The git identity is already in every commit, so the markers and the history agree by construction.
- **It replaces one of the markers with a relation.** `[C → validated]` said that something had been validated; `[opus-5 → ploki]` says **by whom**. In a corpus with several readers, that is the difference between a fact and a fact someone stands behind.
- **And it exposes a question the letters hid**: when nobody validates an agent's proposal, it stays in that agent's name forever. The corpus therefore shows, at a glance, how much of itself nobody has signed.

## Open questions
- Whether the agent's id should carry the exact model string (`claude-opus-5`) rather than the short form.

## History
- 2026-10-03 — Scheme introduced by the author; markers rewritten across the whole corpus.
- 2026-10-03 — Pruned: the fallback when no id can be found, settled in the skill, removed from the open questions.
- 2026-10-04 — ploki: the handle first, then the git name (#70); the question leaves the open questions.
