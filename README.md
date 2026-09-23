# Soccer Analyst — an Agent Skill

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Format: Agent Skill](https://img.shields.io/badge/format-SKILL.md-black.svg)

I give you the football answer first, then show what carries it. If a coach makes everyone eat together, I ask what the arrangement changes: who meets whom, who can speak, whether the substitutes feel included, and whether the players make the routine their own. A full dining room shows attendance. It takes different evidence to show trust, coordinated work or an effect on performance.

I read the space a player leaves on the pitch and the relationships that make a squad work away from it. A pressing system needs coordinated roles; a camp needs people from rival clubs to work together. Neither is explained by the manager’s personality alone. I distinguish the staff’s intention from the players’ response, and both from what results can establish. Quiet authority and emotional intensity can work through different means; a trophy does not validate every rule used by its winner.

For matches, recruitment and club decisions, I connect observed actions, quantitative uncertainty, role fit and financial commitments. When the evidence supports a verdict, I take a position and name what would change it. When it does not, I explain exactly what is missing rather than invent a tactical or cultural story.

This is an Agent Skill for compatible hosts supporting `SKILL.md`. See the [expert core](soccer-analyst/SKILL.md).

---

## What it does

| Capability | What you get |
|---|---|
| **Match reading** | The dominant mechanism supported by match evidence — a pressing trigger, a full-back's starting position, a substitution's timing — in plain language, with a mandatory honesty check that allows "nothing tactical happened here." |
| **Club analysis** | Vague fan questions ("what's going on at United?") get reframed into the actual decision underneath, then answered with a position and the one thing that would change it. |
| **Financial–tactical synthesis** | Wage-bill reasoning brought in *only* when it bears on the decision, with historical estimates checked against their league, era, and timescale, plus an explicit flag when a "tactics problem" is really a budget problem. |
| **Evidence collection** | A repeatable observation plan: actions, players, locations, timestamps, comparable sequences, coding checks and a practical adjustment. |
| **Quantitative analysis** | Data preparation, point-in-time features, xG, forecasting, rankings, passing networks and regression with inputs and assumptions stated. |
| **Uncertainty and recruitment** | Breakout seasons assessed against minutes, prior evidence, role, opponents and alternative signings; model/scouting disagreement investigated. |
| **Club accounts** | Transfer expense separated from cash instalments, wages, contingent commitments and current regulatory constraints. |
| **Team as a social organization** | Meals, hotel rules, punctuality, dress, leisure, captaincy and star treatment examined through identity, status, trust, accountability, authority and motivation. |
| **National-team culture** | Camp routines and player-created practices connected to selection, club rivalries, staff arrangements and institutional history. |
| **Culture evidence** | Coaching intention, player appropriation, proximal change and performance effects separated; competing accounts and causal limits retained. |
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
├── .agents/skills/soccer-analyst -> ../../soccer-analyst
├── fidelity-ledger/              ← source, coverage and validation records
└── soccer-analyst/               ← the installable skill folder
    ├── SKILL.md                  ← expert core + task-based loading triggers
    └── references/               ← loaded on demand, one file per source
        ├── reference-wilson-tactical-history.md
        ├── reference-cox-premier-league-eras.md
        ├── reference-cox-european-styles.md
        ├── reference-szymanski-money-and-soccer.md
        ├── reference-kuper-szymanski-soccernomics.md
        ├── reference-carling-match-analysis.md
        ├── reference-beggs-soccer-analytics-r.md
        ├── reference-mcelreath-statistical-rethinking.md
        ├── reference-graham-football-decisions.md
        ├── reference-maguire-club-finance.md
        ├── reference-nesti-football-psychology.md
        ├── reference-beswick-one-goal.md
        ├── reference-ancelotti-quiet-leadership.md
        ├── reference-obrien-analytical-football.md
        ├── reference-honigstein-klopp-leadership.md
        └── reference-honigstein-das-reboot.md
```

`SKILL.md` is deliberately short. The sixteen files in `references/` are loaded **on demand** —
the Loading depth table after the expert core tells the agent which depth each task needs,
so sources are combined only when their methods bear on the question. A transfer can need tactical depth, and a tactical ambition can need financial context.

## Installation

First clone and enter the repository:

```bash
git clone https://github.com/ariel-lee-1023/soccer-analyst.git
cd soccer-analyst
```

Copy the inner `soccer-analyst/` folder into your agent's documented skill directory.
For agents that use `~/.agents/skills/` for personal skills:

```bash
mkdir -p ~/.agents/skills
cp -r soccer-analyst ~/.agents/skills/
```

For project-local use, this repository already includes a `.agents/skills/soccer-analyst`
link to the canonical skill folder. Agents that support that discovery path can load it
when you open the repository. Otherwise, use your agent's documented project skill directory.

The installed entrypoint should be `<skills-directory>/soccer-analyst/SKILL.md`. The copy
command assumes a fresh installation; update an existing skill in place without nesting
another copy inside it.

If your agent supports skill uploads, package the `soccer-analyst/` folder according to
its documented archive requirements, keeping `SKILL.md` and `references/` together.

Reload skills or start a new session as required by your agent. Automatic discovery and
explicit invocation depend on the host; consult its skill-loading instructions.

## Usage

Ask normally; the skill triggers on football questions.

```
"Arsenal 1–3 at home. What actually went wrong?"
"Should Everton sack the manager in January?"
"Is he finished?"
"What might shared meals and hotel rules change in a national-team camp?"
"Does a star’s exemption from punctuality rules undermine authority?"
"Separate the design of Campo Bahia, players’ own routines and claims about winning."
"Compare Ancelotti and Klopp without assuming one leadership personality is best."
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
rather than recite it from memory. Its sources range from the 2005 match-analysis handbook to 2024 analytics and recruitment books — they supply
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

The skill's frameworks are distilled from sixteen books. The reference files are original
summaries and analytical notes — mental models, decision rules, terminology — not
reproductions of the texts.

| Book | Author(s) | Used for |
|---|---|---|
| *Inverting the Pyramid* | Jonathan Wilson | Why a shape exists, what it fears, what beats it; pressing fundamentals |
| *The Mixer* | Michael Cox | Premier League era context and precedents |
| *Zonal Marking* | Michael Cox | Pressing triggers, positional play, national styles |
| *Money and Soccer* | Stefan Szymanski | Wage–performance, what a club's finances permit |
| *Soccernomics* | Simon Kuper & Stefan Szymanski | Transfer inefficiencies, manager effects, amortization |
| *Handbook of Soccer Match Analysis* (2005; supplied e-library edition 2007) | Christopher Carling, A. Mark Williams & Thomas Reilly | Notation, reliability, contextual interpretation, feedback and training links |
| *Soccer Analytics: An Introduction Using R* (2024) | Clive Beggs | Data preparation, PiT features, xG, forecasting, networks, rankings and regression |
| *Statistical Rethinking*, first edition (2016) | Richard McElreath | Updating, uncertainty, model checking, partial pooling and missing data |
| *How to Win the Premier League* (2024) | Ian Graham | Possession value, recruitment fit, transfer risks and organizational decisions |
| *The Price of Football*, second edition (2021) | Kieran Maguire | Financial statements, player transactions, cash flow, ratios and valuation |

| *Psychology in Football: Working with Elite and Professional Players* (2010) | Mark Nesti | Main foundation for the elite club's psychological and organizational environment |
| *One Goal: The Mindset of Winning Soccer Teams* (2016) | Bill Beswick | Shared purpose, bonds, coachability, accountability, cohesion and tournament demands |
| *Quiet Leadership: Winning Hearts, Minds and Matches* (2016) | Carlo Ancelotti, with Chris Brady & Mike Forde | Relationship-based authority, everyday rules, captaincy and institutional adaptation |
| *Analytical Psychology of Football: Professional Jungian Football Coaching* (2021) | John O'Brien & Nada O'Brien, editors | Optional interpretation of identity, symbolism and team meaning; distinct evidence limits |
| *Klopp: Bring the Noise* (2017) | Raphael Honigstein | Contextual leadership cases, reported player responses and counterexamples |
| *Das Reboot: How German Soccer Reinvented Itself and Conquered the World* (2015) | Raphael Honigstein | Federation and academy reform, national-team organization and camp culture |

If you want the arguments in full, buy the books. They are better than any summary of them.

## Scope and limitations

These sixteen books are the foundation, not the boundary of the sport. Coverage is thin on
women's club football, most non-European leagues, and developments beyond the supplied editions — the skill is
instructed to say so rather than extrapolate with false confidence.

The 2026-09-14 analytical-method expansion preserves the existing installable `soccer-analyst/` folder and all five older references. Its core remains verdict-first; a task loads only the methods it needs. The chain from observation through quantitative comparison, uncertainty, role fit and financial commitment is an original library synthesis, not attributed to any single author. The additions do not amount to a complete modern tactical coaching manual.

The 2026-09-23 extension adds the team as a social organization while preserving all ten earlier references. Nesti is the default organizational source; Beswick and Ancelotti supply mechanisms and contrasting authority practices. Jungian concepts are optional interpretations, and the biographies are contextual cases. The distinction between intended intervention, player appropriation and evidenced effects is this library's synthesis, not a framework attributed to one author. The corpus does not establish the causal benefit of a meal policy, leisure restriction or leadership style, and it cannot reveal current private dressing-room attitudes. Several accounts overlap; repeated anecdotes are not independent corroboration.

Default output is English, matching the represented corpus; an explicit user request changes the output language.

## Validation and source fidelity

The new references contain original method notes, prerequisites, limitations, chapter locators and one reconstructed example per book. Raw books and extraction files are not distributed. Maintainer evidence belongs in [fidelity-ledger/](fidelity-ledger/README.md), outside runtime references.

Structural and instruction scans, arithmetic checks and preservation checks are recorded there. The original nine-case suite and its results remain preserved. The culture update freezes an expanded seventeen-case suite covering application, inapplicability, disagreement and unsupported requests, with development and final groups; see its [audit records](fidelity-ledger/culture-2026-09-23/README.md). **Independent baseline/core/full model evaluation has not been run:** no evaluation endpoint/model was configured. File validation and editorial review do not establish measured improvement in answer quality. R snippets were not executed in R; their stated arithmetic was checked independently in Python.

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

## License

MIT © 2026 Ariel Lee. [See LICENSE](LICENSE).

This license covers the original text in this repository. It does not extend to any
referenced source books, which remain the property of their respective copyright holders.
