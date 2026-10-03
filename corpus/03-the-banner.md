# 03 — The banner

## Current
- **[G]** The banner is **slow to appear, because it goes through the LLM.** The author is right about the cause.
- **Measured** (2026-10-03): `assets/banner.txt` is 41 lines, **2 254 characters, of which 1 320 are Braille** (U+2800–U+28FF), 5 475 UTF-8 bytes.
  - **[C]** Braille characters are not in any tokeniser's common vocabulary: each one costs roughly a token, often more. **The buste alone is on the order of 1 300 to 2 000 output tokens**, generated one by one, before the session can say anything. That is the whole of the latency.
- **[G]** The skill currently instructs Claude to **read the file and reproduce it verbatim in its reply**, precisely because the output of a shell command is not always visible to the user.

## Options [C] — none applied, the author asked that the skill not be modified
| Option | Gain | Cost |
|---|---|---|
| `cat assets/banner.txt` through Bash | Zero LLM tokens, instantaneous | Relies on the host showing command output; the skill's own caution is exactly about this |
| A **session hook** printing the banner | Zero tokens, and outside the model entirely | Needs installation beyond dropping a skill folder — friction for adopters |
| **Shrink the buste** | Proportional | Loses the picture that makes the skill feel like something |
| **Title and pipeline only**, buste on request | ~90 % of the tokens saved; the ASCII title and the diagram are cheap | Two tiers of welcome |
| Keep as is | The effect is genuinely good | A few seconds, once per session |

- **[C]** My own reading: the banner is shown **once per project opening**. A few seconds of latency, once, against the thing that gives the skill its identity, is a defensible trade — but only if the buste is the smallest it can be while still reading as a face.

## Still open
- Which option, if any.
- Whether the banner needs a light-background variant shipped alongside (`assets/make_bust.py` can invert it).

## History
- 2026-10-03 — Opened; the author observed the latency and asked that the skill not be changed.
