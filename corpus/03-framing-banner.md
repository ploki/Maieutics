# 03 — The banner

## Current
- **[ploki]** The banner is **slow to appear, because it goes through the LLM.**
  - **[opus-5]** The diagnosis is right, and the measurements below confirm it.
- **Measured** (2026-10-03): `assets/banner.txt` is 41 lines, **2 254 characters, of which 1 320 are Braille** (U+2800–U+28FF), 5 475 UTF-8 bytes.
  - **[opus-5]** Braille characters are not in any tokeniser's common vocabulary: each one costs roughly a token, often more. **The buste alone is on the order of 1 300 to 2 000 output tokens**, generated one by one, before the session can say anything. That is the whole of the latency.
- **[opus-5]** The skill instructs the agent to **read the file and reproduce it verbatim in its reply**, precisely because the output of a shell command is not always visible to the user.

## Settled, 2026-10-03
- **[ploki]** **Stop burning millions of tokens for nothing.** The skill now says: show the banner with `cat assets/banner.txt`, **never by retyping it**. Only if the user reports seeing nothing does the agent reproduce it once, and note that this host hides command output.
  - **[opus-5]** Saving: the whole of it. Roughly 1 300–2 000 output tokens and several seconds, at every project opening, down to the cost of one shell call.
- **[ploki]** **The banner was localised, and that is fixed.** `banner.txt` is English, `banner.fr.txt` is French; the agent picks by the user's language and falls back to English. The French original keeps the Theaetetus quotation in French, which is where it belongs.
  - **[opus-5]** It is the only asset that needed this, exactly as note 02 predicted. The pipeline labels, the tagline and the quotation were the French; the buste and `ΣΩΚΡΑΤΗΣ` are language-neutral and unchanged.

## Settled, 2026-10-03, later still
- **[ploki]** **The small buste becomes the banner**: 22 columns, 15 rows, blank cells as spaces — **188 Braille characters**, against 1 320 originally. "This banner works for me."
  - ↺ *Replaces the full 44-column buste kept a moment earlier with only the blank-cell fix (710).*
  - **[opus-5.5]** The title, tagline and quotation sit beside the smaller buste, in both languages; the pipeline is unchanged.
  - **[opus-5.5]** Trade-off accepted by ploki: a head, a brow and a beard rather than a recognisable portrait — earlier judged "no longer Socrates" by opus-5.5.
- **[ploki]** **The full buste is archived**: `archive/banner-full.txt` and `archive/banner-full.fr.txt`. `make_bust.py` now defaults to 22 columns and writes spaces for blank cells; `make_bust.py 44` regenerates the large one.

## Found, 2026-10-03, later
- **[opus-5.5]** **In Claude Code, `cat` shows the user nothing.** The host collapses command output; the agent sees the banner, the user does not. The fallback ("reproduce it if the user says they cannot see it") therefore fires on almost every opening, and brings back the cost #30 meant to remove.
- **[opus-5.5]** **610 of the 1 320 Braille characters were blank cells** (U+2800), visually identical to a space but each costing tokens.
- **[ploki]** Apply the blank-cell fix to the full banner. **Done** in `banner.txt` and `banner.fr.txt`: blank cells replaced by spaces, trailing spaces trimmed. **1 320 → 710 Braille characters**, the picture unchanged.
  - **[opus-5.5]** Caveat: where the title and the quotation sit to the right of the buste, alignment now relies on a Braille cell being as wide as a space. True in common monospace fonts; [Unverified] in all.
- **Explored** [opus-5.5]: a 22-column Braille buste (330 → 188 Braille characters with the fix) — adopted, see above; ASCII art at 24–40 columns — cheaper still, the likeness gone. Kept in no file.
- **Token figures remain estimates**: no tokenizer and no API key were available. Measuring with the `count_tokens` endpoint is the way to settle them.

## Options weighed [opus-5] — kept for the record
| Option | Gain | Cost |
|---|---|---|
| `cat assets/banner.txt` through Bash | Zero LLM tokens, instantaneous | Relies on the host showing command output; the skill's own caution is exactly about this |
| A **session hook** printing the banner | Zero tokens, and outside the model entirely | Needs installation beyond dropping a skill folder — friction for adopters |
| **Shrink the buste** | Proportional | Loses the picture that makes the skill feel like something |
| **Title and pipeline only**, buste on request | ~90 % of the tokens saved; the ASCII title and the diagram are cheap | Two tiers of welcome |
| Keep as is | The effect is genuinely good | A few seconds, once per session |

*The first option was taken. The skill's original caution — that shell output is not always visible — survives as a fallback rather than as the default.*

- ~~**[opus-5]** A few seconds of latency, once, is a defensible trade.~~ ↺ *Wrong: the trade was never necessary. `cat` costs nothing and the picture is identical.*

## Still open
- How the banner should reach the user in Claude Code, where `cat` output is hidden: reproduce the fixed banner, ask the user to run `! cat`, a hook, or a smaller welcome.
- Whether the banner needs a light-background variant shipped alongside (`assets/make_bust.py` can invert it).

## History
- 2026-10-03 — Opened; the author observed the latency and asked that the skill not be changed.
