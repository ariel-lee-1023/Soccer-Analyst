# Soccer Analyst — an Agent Skill

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Format: Agent Skill](https://img.shields.io/badge/format-SKILL.md-black.svg)

A football (soccer) analysis skill for Claude and other agents that read the
[Agent Skills](https://github.com/anthropics/skills) `SKILL.md` format.

It makes the model read matches, clubs and transfers the way a good co-commentator would
if he had also read the economics: **verdict first, concrete mechanisms, uncertainty placed precisely** —
and an explicit refusal to invent a tactical story for a result that was really a red card,
a deflection, or one team simply being better.

---

## What it does

| Capability | What you get |
|---|---|
| **Match reading** | The dominant mechanism supported by match evidence — a pressing trigger, a full-back's starting position, a substitution's timing — in plain language, with a mandatory honesty check that allows "nothing tactical happened here." |
| **Club analysis** | Vague fan questions ("what's going on at United?") get reframed into the actual decision underneath, then answered with a position and the one thing that would change it. |
| **Financial–tactical synthesis** | Wage-bill reasoning brought in *only* when it bears on the decision, with historical estimates checked against their league, era, and timescale, plus an explicit flag when a "tactics problem" is really a budget problem. |
| **Fan-register honesty** | Blunt questions get blunt answers first. Verdict, then reasoning, then jargon — and only if the jargon earns its place. |

## Repository structure

```
.
├── README.md
├── AGENTS.md                     ← default analyst role and project guidance
├── LICENSE
├── NOTICE.md                     ← originality and source-attribution statement
├── CHANGELOG.md
├── .gitignore
└── soccer-analyst/               ← the installable skill folder
    ├── SKILL.md                  ← expert core + task-based loading triggers
    └── references/               ← loaded on demand, one file per source
        ├── reference-wilson-tactical-history.md
        ├── reference-cox-premier-league-eras.md
        ├── reference-cox-european-styles.md
        ├── reference-szymanski-money-and-soccer.md
        └── reference-kuper-szymanski-soccernomics.md
```

`SKILL.md` is deliberately short. The five files in `references/` are loaded **on demand** —
the Loading depth table after the expert core tells the agent which depth each task needs,
so sources are combined only when their methods bear on the question. A transfer can need tactical depth, and a tactical ambition can need financial context.

## Installation

### Claude Code

First clone and enter the repository:

```bash
git clone https://github.com/ariel-lee-1023/Soccer-Analyst.git
cd Soccer-Analyst
```

From the repository root, copy the inner skill folder into either location:

```bash
# personal — available in every project
mkdir -p ~/.claude/skills
cp -r soccer-analyst ~/.claude/skills/

# or project-scoped — checked into the repo you're working in
mkdir -p .claude/skills
cp -r soccer-analyst .claude/skills/
```

The installed entrypoint should be `<skills-directory>/soccer-analyst/SKILL.md`. These commands assume a fresh installation; update an existing skill in place without nesting another copy inside it.

Start a new session. The skill is picked up automatically when a request matches its
description, and is also available as `/soccer-analyst`.

### Claude.ai and the Claude API

Zip the `soccer-analyst/` folder (the zip must contain `SKILL.md` at the top level of that
folder) and upload it as a custom skill. Current instructions:
[claude.ai skills](https://support.claude.com) · [Skills on the API](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview).

### Other agents

The format is the open Agent Skills standard, so the same folder works anywhere `SKILL.md`
files are supported — drop it in that tool's skills directory.

## Usage

Ask normally; the skill triggers on football questions.

```
"Arsenal 1–3 at home. What actually went wrong?"
"Should Everton sack the manager in January?"
"Is he finished?"
"They just paid £55m for a 29-year-old striker who had a great World Cup. Verdict?"
```

Illustrative answer shapes below assume the described incidents and financial comparison have been verified; they are not claims about a particular match or club:

> **The sending-off changed the game.** The incidents supplied point to the numerical
> disadvantage as the main turning point. I would still check the response in shape and
> substitutions before deciding how much of the later pressure was avoidable.

> **Keep him for now unless the replacement solves a specific problem.** The modest gap
> against the stated resource baseline does not by itself establish a coaching failure.
> I would change that verdict if match evidence showed a persistent, avoidable problem
> that the proposed replacement is equipped to fix.

The skill is explicitly instructed to fetch current data (results, tables, squads, fees)
rather than recite it from memory. Its source books end between 2015 and 2022 — they supply
frameworks and precedents, not today's team sheet.

## Design notes

A few decisions worth knowing if you want to fork it:

- **Explain what supports the verdict.** Prefer a concrete mechanism to "they were poor."
  Prioritize multiple causes when the evidence supports them; do not invent specificity.
- **The honesty check is load-bearing.** Inventing a tactical cause for a random result is
  the stated worst failure mode, so "nothing tactical" is an approved answer.
- **Money follows relevance.** Use resources when they constrain the decision, without
  treating a long-run wage relationship as the cause of a particular match incident.
- **No great-man history.** Prefer "the recruitment department" to "the manager" wherever the
  evidence allows.
- **Progressive disclosure.** Files in `references/` carry the detail; `SKILL.md` carries the
  reasoning voice and task triggers.

## Sources

The skill's frameworks are distilled from five books. The reference files are original
summaries and analytical notes — mental models, decision rules, terminology — not
reproductions of the texts.

| Book | Author(s) | Used for |
|---|---|---|
| *Inverting the Pyramid* | Jonathan Wilson | Why a shape exists, what it fears, what beats it; pressing fundamentals |
| *The Mixer* | Michael Cox | Premier League era context and precedents |
| *Zonal Marking* | Michael Cox | Pressing triggers, positional play, national styles |
| *Money and Soccer* | Stefan Szymanski | Wage–performance, what a club's finances permit |
| *Soccernomics* | Simon Kuper & Stefan Szymanski | Transfer inefficiencies, manager effects, amortization |

If you want the arguments in full, buy the books. They are better than any summary of them.

## Scope and limitations

These five books are the foundation, not the boundary of the sport. Coverage is thin on
women's club football, most non-European leagues, and post-2022 developments — the skill is
instructed to say so rather than extrapolate with false confidence.

## Contributing

Issues and pull requests are welcome. Useful contributions:

- tightening a decision rule that produces mushy answers in practice
- adding a reference file for a source that fills a named gap above
- example prompts with the answers the skill actually gave, good or bad

Please add new reference files under `soccer-analyst/references/`, keep them in the existing
structure (Mental Model → Frameworks → Worked Example → Decision Rules → Key Takeaways) and
keep them as original summary, not excerpt. Add a matching row to the routing table in
`SKILL.md` — a reference file the table doesn't point at will never be opened.

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

---

MIT © 2026 Ariel Lee. [See LICENSE](LICENSE).

This license covers the original text in this repository. It does not extend to any
referenced source books, which remain the property of their respective copyright holders.
