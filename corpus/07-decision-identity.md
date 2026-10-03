# 07 — Who said what: identity in the corpus

## Current
- **[ploki]** The user should be **identified by their git id**; failing that, by their first name if the agent knows it; failing that, asked for.
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

## Still open
- Whether to prefer the git **handle** (`ploki`) or the git **name** (`Guillaume Gimenez`). The handle is shorter, stable, and already public; the name is friendlier. This project uses the handle.
- What a session does when it cannot determine either — ask once and record it in the index, which is what the skill now says.
- Whether the agent's id should carry the exact model string (`claude-opus-5`) rather than the short form.

## History
- 2026-10-03 — Scheme introduced by the author; markers rewritten across the whole corpus.
