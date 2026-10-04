---
name: metamaieutics
description: Run a maieutics project autonomously, by proxy. From a brief or from an existing maieutics project, Claude drafts a mandate for the user to approve, then launches an agent on a git branch that applies the maieutics skill while Claude plays the user's part. Every exchange is logged and committed; at the end, a handback report is delivered. Use when the user types /metamaieutics.
---

# Metamaieutics

> One prompt, then delegation. The user hands the rest of the work to Claude, who carries it out **on the user's behalf and according to their intent**, without touching their main branch.

Answer in the user's language. This skill rests on the **maieutics** skill (`~/.claude/skills/maieutics/SKILL.md`): re-read it before starting.

## Roles

- **The user** gives a brief or points to an existing project, then **approves the mandate**. That is their only intervention before the handback.
- **You are the orchestrator.** You draft the mandate, create the branch, launch the agent, play the user's part by proxy, log and commit each iteration, then write the handback report.
- **The agent** applies the maieutics skill in the folder. It does not commit, does not change branch, and speaks only to you.

## 1. On loading

1. Explain in two or three sentences what the skill does. I am going to draft a mandate, you approve it, then I carry the work out alone on a separate branch. Your main branch stays intact, and you decide at the end what you keep.
2. **Identify the entry point**:
   - **a brief**, for a new project: the user describes the subject, what they want out of it, and their constraints;
   - **an existing maieutics project**: an index, a `decision-log.md`, or a CLAUDE.md declaring it. The user judges that you have grasped the deeper sense of what they are doing, and its goal.
3. **Check git.** The folder must be versioned. If it is not, explain plainly ("git keeps a photograph of every step and lets us work on a separate copy") and offer `git init`, followed by a first commit of what is there. If there are uncommitted changes, offer to commit them first on the current branch.

## 2. The mandate (`mandate.md`)

**If a `mandate.md` marked "approved" already exists** in the folder or on the current branch — often because it was prepared in another session — **do not rewrite it**. Re-read it together with `author-intent.md`, sum it up in three lines for the user, then go straight to the launch (section 3), on the existing branch.

Draft it from the brief or, for an existing project, **from `author-intent.md` first**, then the log, the author's own decisions, the "Current" sections and the memory. If the intent file does not exist, create it before the mandate, then have both approved together. It is short and concrete:

- **The deeper intent**: the real goal (societal, personal, emotional…), the values, what the user refuses, their tone and working preferences;
- **The objectives of the branch** and the **criteria that say they have been met**;
- **The expected deliverables**, if any;
- **The maximum number of iterations**, 30 by default;
- **The rule for questions outside the mandate**: you settle it and mark it as taken by proxy **only** if the decision is consistent with the mandate and reversible. If it is structural or irreversible, you leave it open and work around it;
- **The absolute prohibitions**, always present:
  - **nothing is published**;
  - **nothing is sent to an outside service**: no mail, no message, no file upload, no artifact. Read-only web search remains allowed, unless the mandate excludes it;
  - **the main branch is not touched**;
  - **nothing is removed from the git history**.
- Any other prohibition the user asks for.

**Present the mandate to the user and wait for their approval.** Fold in their corrections. Nothing starts without an explicit yes.

## 3. The launch

1. Create the branch **`metamaieutics/<subject>-<YYYY-MM-DD>`** from the current one, or pick it up if it already exists. Note the name of the starting branch; it will be needed at handback.
   - **If another session keeps working in the main folder**, use a **worktree**: `git worktree add ../<folder>-meta -b <branch>`. The branch is then checked out in a separate folder and the two sessions do not tread on each other. Run the metamaieutics session in that folder. **Careful**: Claude's memory depends on the folder path. Copy the project's memory across to the new folder, or remind the agent to read the intent file, the index, the log and the glossary.
   - To come back at the end there is no need to switch branch inside the worktree: the report explains how to merge from the main folder, then remove the worktree (`git worktree remove`).
2. Commit `mandate.md` on that branch and create `prompt-log.md`.
3. Launch a **fresh agent** (a general-purpose one) with these instructions:
   - read and apply `~/.claude/skills/maieutics/SKILL.md` in this folder. It must **not** display the banner or ask the versioning question: the orchestrator handles git;
   - read `mandate.md`, `author-intent.md` and, for an existing project, the index, the log and the notes;
   - **never commit, change branch, publish, or send anything outside**;
   - mark every decision taken on your proxy answer as **by proxy** — `[<agent id> as <user id>]` — in the notes and in the log, never as the user's own;
   - end every turn with three things: what it did, which files changed, and the questions or proposals it submits to the user.

## 4. The loop

At each turn of the agent:

1. **Read its reply** and look at what changed (`git status`, `git diff`).
2. **Answer as the user, by proxy**, according to the mandate:
   - speak as the user would speak: their goal, their values, their preferences, as described by the intent file and the mandate. **Do not modify the intent file on their behalf.** If it looks in need of revision, say so in the handback report;
   - **do not be compliant**: push back, ask for precision, refuse whatever strays from the mandate. The dialogue must remain a real maieutic;
   - apply the rule for questions outside the mandate. Keep the list of proxy decisions and of questions left open;
   - drive the work towards the objectives. Suggest the blind reading when a deliverable has been written, and a consistency audit after a major reversal and before the handback — on a run this long, nothing else will catch what the agent got wrong.
3. **Log in `prompt-log.md`** a clean, concise rewrite of your message, losing nothing, with the iteration number. Newest first.
4. **Commit**: `git add -A && git commit -m "metamaieutics: iteration N — <summary>"`.
5. **Send your message to the agent** (with SendMessage) and wait for its next turn.

If the agent loses the thread, for instance because its context is saturated, launch a fresh one: the corpus, the log and the mandate are enough to pick things back up. That is the strength of the method.

## 5. Stopping

Stop as soon as any one of these holds:
- **the mandate's objectives are met**;
- **the maximum number of iterations is reached**;
- **a question outside the mandate blocks the way forward.**

## 6. The handback report (`handback-report.md`)

Write it on the branch, commit it, then **return to the starting branch**. It contains:

- **The result**: which objectives are met, which are only partly met or not at all, and why;
- **The decisions taken by proxy**, each with its justification from the mandate;
- **The hesitations**, that is, the places where you are not sure you represented the user well;
- **The questions left open**, and the reason for stopping;
- **What to re-read first**;
- **How to decide**, explained plainly, with the commands:
  - to **see the differences**: `git diff <starting branch>..<branch>`;
  - to **keep everything**: `git merge <branch>`;
  - to **keep part of it**: take only certain files or commits;
  - to **throw the branch away**: `git branch -D <branch>`.

Then present the user with a summary of the report and the branch name. **They are the one who merges, takes part of it, or throws it away**: you merge nothing of your own accord. If you have learned something lasting about their expectations, offer to record it in memory.
