# How to Win the Premier League: The Inside Story of Football's Data Revolution — Ian Graham
**Format**: supplied Markdown | **Edition**: first published 2024 | **Sections**: 16 numbered chapters, plus conclusion | **Depth**: study
**Use for**: turning player and team data into recruitment, role-fit and managerial decisions; evaluating possession value and the limits of event data.

## Mental Model (read first)
Separate performance from the result, then ask whether the performance will transfer to the role and team being considered. Data can challenge reputation and reveal undervalued contribution, but it needs people who understand its omissions and can turn evidence into decisions. Better recruitment means reducing several ways a move can fail, including deciding that the current squad is the better option.

**Source boundary:** Graham's club experience, model estimates and historical examples are his account. They are not independently verified observations by this advisor or descriptions of today's club personnel. Chapter titles locate the material. The integrated evidence-to-finance workflow in the core is this library's synthesis, not a framework named by Graham.

## Frameworks & Structure

### Chapters 1–5 — The road to Anfield: evidence needs an organization
These chapters move from Liverpool's success and Graham's work at Tottenham to Liverpool under Rodgers, the arrival of Klopp and the later winning team. Their analytical thread is the interaction between model evidence, scouting, management and the sporting director.

**Question:** Does the club have a supported recommendation and the organizational ability to use it? Require a specified role, model evidence, video assessment, incumbent alternatives and a manager who intends to use the signing. Model agreement with scouting is useful; disagreement is an investigation request, not a reason to suppress either view.

Graham separates player classification (what kinds of actions define a style) from performance valuation (how useful those actions are). A player can be excellent at a role the new side does not need. Joe Allen's high completion rate reflected his assignment; Christian Benteke's target-man strengths did not imply that he would become the different forward Liverpool wanted. Changing shirt does not establish changed style.

**Small-sample lesson:** Graham explicitly regrets underemphasizing that Giovani dos Santos' strong rating came from about 1,400 minutes. State exposure and sample limitations as part of the recommendation, not in a footnote. **Availability bias:** spectacular goalkeeper errors can overwhelm memory of routine good saves. Judge the relevant full sample without pretending that shot-stopping measures every part of goalkeeping.

### Chapter 6 — Gambling on data and forecasting strength
Estimate team attack and defence from historical evidence and express match outcomes probabilistically. Forecasting provides an expectation against which a season can be compared. Result-only data provide less diagnostic depth than shots and chance quality; low probability is not impossibility.

**Required checks:** what was known before the match, model calibration on unseen games, comparison with market expectations, and changing squads/opponents. A profitable retrospective betting example does not prove a current edge. A model of team strength describes its target; it cannot alone explain exactly which coaching action caused overperformance.

### Chapter 7 — What to expect if you're expecting goals
**Expected Goals** conditions a shot's conversion chance on observed features such as position and phase. Assess chance generation separately from finishing outcomes and penalties. One season's excess goals may reflect skill, chance or omitted shot detail; repeated evidence and a suitable model are needed to separate them.

**Post-Strike Expected Goals**, introduced earlier and relevant here, conditions on the shot's trajectory. It better addresses the shot-stopping difficulty a goalkeeper faced than pre-shot xG or raw save percentage. It does not by itself measure positioning before the shot, cross collection, sweeping or distribution. Keep provider definitions consistent and distinguish the model benchmark from the realized result.

The historical conversion rates for different shooting zones explain why location matters; they are not current player-independent scoring probabilities. More dangerous opportunities can matter more than spectacular low-probability finishes.

### Chapter 8 — The value of possession
**Question:** How much does an action improve scoring prospects after accounting for risk? **Required inputs:** ordered events, ball locations, possession phases, transition/outcome definitions and enough comparable historical data.

A **Possession Value** model estimates scoring chances from game states. Graham's event-based version uses location and possession type, with a Markov approximation: once the chosen state is known, the past is treated as unnecessary for the next transition. This is an approximation to football, not a statement that real attacks have no history. Estimate transitions and resulting scoring chances, then credit or debit an action for the change in prospects, including the opponent's opportunity after a turnover.

A risky line-breaking pass can add more than a safe completed pass. Compare expected reward, failure cost and success probability, rather than raw completion. A role's instructions can explain the chosen action mix; absence of demonstrated progressive passing does not prove incapacity, but it is weak evidence for paying as though that capacity were established.

**The Ridgewell Problem:** event data reward tackles, blocks and clearances while often failing to observe poor positioning or the prevention of danger without touching the ball. A busy defender in a weak defence can look outstanding. Graham's positional responsibility debits are an approximation, not direct measurement of who caused every chance. For defensive recruitment, increase the weight of appropriate video/tracking evidence instead of interpreting missing events as no contribution.

**Usage and per-possession contribution:** usage concerns the possessions a player ends through losing the ball, shooting or scoring. Separate value added while continuing possession from value added while consuming it. Graham's **triple threat** adds value through shooting, passing and dribbling. A side needs compatible passing, carrying and shooting contributions; eleven high-volume shooters cannot each consume the same possession. Compare action mix, opportunity and quality, not only a single per-90 ranking.

For cross-league recruitment, Graham adjusts contribution for opposition strength; raw production against weak opponents is not directly portable. Team quality can also leak into a model through possession history: long chains may identify a strong team rather than show that extra passes cause more danger. This is unwanted attribution, distinct from using future data in a forecast. Richer context must earn its place against the question the model is intended to answer.

### Chapter 9 — Track your man
Tracking adds synchronized player/ball positions and movement. **Pitch Control** asks how likely each team is to reach and control a location, considering movement, ball travel and uncertain control. Being nearest is insufficient: speed, direction, reaction, first touch and interception opportunities matter.

Useful possession requires three connected ingredients: control at the destination, scoring value there, and a pass that can actually arrive. A free player in a valuable location may not be reachable; a safe backwards option may add little; a moderately risky pass into usable space can be best. Event-based average values can miss these differences.

Uncertainty remains even with tracking: fatigue, orientation, reaction and tactical permissions are imperfectly observed. Added detail must improve validated prediction or decisions. When no video/tracking is available, do not invent specific runs, defensive positions or a player's response to an alternative pass.

### Chapter 10 — Paying for performance
Graham models market salaries using **PRAISE**: position; ratings (team and player); age; inflation; signing route; experience. The sample covered estimated salaries for only part of the market over a stated historical period, checked against club totals. The model supplies negotiation context, not a public database of exact wages or a universal price formula.

Market price and contribution differ. A prestigious club, experience and negotiation context can raise pay without a proportionate increase in performance. Compare the player with the current option and feasible alternatives at full terms. A cheap fee can conceal high wages; a market model predicting a high price is not a recommendation to pay it. Not signing is a valid outcome when few available players improve the team.

### Chapter 11 — Schrödinger's manager
**Question:** Is the manager producing something better than the relevant expectation, and can we identify what? Compare team performance against resources and pre-match expectations over an appropriate period, including uncertainty. Use better evidence where available: Dortmund's poor results could be distinguished from underlying performance with chance data; earlier Mainz seasons allowed less explanation.

A percentile for overperformance is conditional on a forecasting model. It is not the posterior probability that the manager is good, that luck caused the season, or that sacking him will help. Consider repeated seasons, player changes, opponents and model error. A replacement decision still needs a candidate, costs and fit. Preserve uncertainty about causal attribution while making the practical choice the evidence supports.

### Chapter 12 — Goat war
Cross-player comparisons depend on what is counted and how role and possession are treated. Goals, passing contribution, dribbling and opportunity can produce different rankings. Make the comparison criterion explicit and inspect where the models omit work. The chapter's Messi/Ronaldo comparisons are historical worked comparisons, not a timeless answer to every definition of “best.”

### Chapter 13 — Zebra farmers: why transfers fail
**The 50% Rule:** Graham classifies a transfer as successful if the player starts at least half the club's league games over the next two years. In his sample of Premier League arrivals costing at least €10m from 1992 to January 2021, 46% missed that threshold. This is a participation benchmark, not an all-purpose measure of sporting value; it can misclassify valuable squad players and approve expensive regular starters who do not improve results. Fee inflation and intended role affect comparisons.

The **Anna Karenina principle** organizes multiple failure routes: injury; personal/working difficulties; playing out of position; no upgrade over incumbents; overestimated ability; incompatible style; a manager who will not use the player; or youth requiring more time. Investigate each with appropriate evidence and distinguish documented facts from labels or rumours about character.

Graham's illustration multiplies eight 92% success assumptions to obtain roughly 51% overall success **assuming independence**. It is a demonstration of compound risk, not an estimated probability for a real target. Correlated risks such as manager preference and role deployment should not be multiplied as though independent.

Use one standard for newcomers and incumbents. Detailed video became an additional check after Liverpool's Marković experience. Injury history and adoption by the coaching staff remain important beyond event rankings. A player can be talented and a poor purchase for this squad and contract.

### Chapter 14 — Home is where 30% more goals are
Home advantage, crowd effects and scheduling belong in the context of performance and prediction. The chapter title describes a historical aggregate, not a fixed multiplier for every league or match. Separate league averages from particular venues and circumstances; a change in crowd conditions is evidence to investigate, not automatic identification of a single cause. Re-estimate current rates before making forecasts.

### Chapter 15 — Stats and snake oil
**The Tyranny of Metrics:** with enough criteria, many players can be made to look optimal. A **Pareto Frontier** contains players not dominated across the selected metrics; adding metrics can expand it until a supposedly useful shortlist includes much of the market. Select a few role-relevant objectives before examining preferred names, state the tradeoffs, then investigate shortlisted players in depth.

A Pareto frontier in a selected sample does not prove an intrinsic biological tradeoff. Nor does a correlation between corners and goals establish the value of an additional corner without considering opportunity and sample. Check denominators, selection and the action a statistic is supposed to support. Reject impressive-looking certainty without a coherent method or relevant validation.

### Chapter 16 and conclusion — More data, usable decisions
The discussion of future data and tactical modelling extends analysis to transitions, tracking and richer counterfactuals. These possibilities do not make every real tactical intervention predictable. Ask whether the organization can explain, validate and act on the model's findings. Historical Liverpool successes demonstrate the author's experience of collaboration; they do not identify an isolated effect of a model or promise replication at another club.

## Worked Example — A 25% passer can add value
Reconstruction of Chapter 8's illustrative possession calculation. A team begins with a 1% scoring chance; a completed pass reaches a state worth 5%, a gain of 4 percentage points. Failure loses the original 1% and gives the opponent a 0.3% chance, a total cost of 1.3 percentage points.

Across 100 attempts with 25 completions, the model credits `25*0.04 − 75*0.013 = 0.025` net expected goals. At 24 completions it gives `24*0.04 − 76*0.013 = −0.028`. The illustrative break-even completion rate is `0.013/(0.04+0.013)`, about 24.5%.

This is modelled change in expected net goals, not goals observed or an instruction to attempt every speculative pass. It depends on the state values, turnover risk and available alternatives. The arithmetic explains why raw completion can mislead; video/tracking can establish whether a specific pass was actually the right choice.

## Decision Rules & Judgment
- If a rating conflicts with video, locate the omitted action, role or sample issue before choosing which source to trust.
- If the target's value relies on changing an established style, require evidence for that adaptation.
- If the defender looks great because he is always intervening, inspect the danger he helped allow or prevent without an event.
- If a signing does not improve the incumbent at feasible terms, keep the incumbent unless another need is evidenced.
- If several ways to fail are plausible, investigate them separately; do not invent independent percentages.
- If a manager beat expectations, distinguish model surprise from causal credit.
- If every preferred target can win on some metric, reduce the criteria to the role and decision before reopening the shortlist.

## Key Takeaways
1. Contribution, opportunity, role and price are different quantities.
2. Data becomes useful through honest explanation, scouting checks and a team prepared to use the player.
3. Recruitment quality includes avoiding an attractive but unsuitable move.
