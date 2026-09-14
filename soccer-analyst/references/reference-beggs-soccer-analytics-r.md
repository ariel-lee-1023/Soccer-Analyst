# Soccer Analytics: An Introduction Using R — Clive Beggs
**Format**: supplied Markdown | **Edition**: first edition, 2024 | **Sections**: 11 | **Depth**: study
**Use for**: selecting a football analysis, preparing its inputs, reproducing calculations, evaluating forecasts, and interpreting networks or regressions.

## Mental Model (read first)
A football question determines the analysis; software makes that analysis repeatable. Begin by understanding what each variable measures and when it became available. Distinguish a description of completed matches from a prediction of unseen matches and from an explanation of what causes performance. An impressive fit or graph is useful only if its assumptions and interpretation survive inspection.

**Source boundary:** Chapter numbers below follow the 2024 text. Some supplied equations and code are damaged by conversion. Formulas below use coherent mathematical notation reconstructed from the surrounding definitions; they are not verbatim transcriptions. Software/package names identify the source's methods, not verified current APIs. Explicitly labelled advisor safeguards extend the source workflow.

## Frameworks & Structure

### Chapter 1 — Purpose, prediction and communicating results
Ask whether the task is descriptive, predictive or explanatory. Identify the outcome and unit: shot, possession, player-match, match or team-season. A seasonal association between shots and points does not establish that forcing extra shots will improve a team's results. A manager comparison needs comparable exposure and circumstances; a result streak may reflect regression towards ordinary performance.

Use tables for exact comparisons and plots for distributions or relationships. State units, sample and reference period. Betting odds provide market expectations, not certainty: decimal odds imply raw probabilities 1/odds, and their sum generally includes a bookmaker margin. Report a probability distribution rather than turning the most likely outcome into a promise.

### Chapters 2–3 — R, data preparation and missingness
**Required inputs:** source snapshot, field definitions, dates, team/player identifiers, units and a record of exclusions. Preserve the imported original and work on a copy. Inspect types, ranges, duplicates and missing values before calculating derived variables. Use explicit date parsing, consistent names and meaningful grouping; distinguish a missing measurement from an observed zero.

The book introduces vectors, data frames, indexing, loops, functions, packages, plotting, tests and regression, then importing files and harvesting web data. Use a saved script so cleaning and derivation can be rerun. Functions such as `na.omit` and `na.rm` perform operations; they do not justify the missing-data assumption. A complete-case result should disclose how much and which data disappeared. Selective absence, such as poorly covered leagues, can change a recruitment conclusion.

**Advisor reproducibility record:** data source/version and date retrieved; observation window; schema and units; cleaning and exclusion rules; denominators; formula/model; training cutoff; seed where random; software versions; outputs and diagnostics. If tools or data are unavailable, supply a calculation plan or code and say it was not executed. Do not imply that the book's live web sources or package interfaces were checked today.

### Chapter 4 — Match data, league tables and point-in-time features
Compile results in chronological order and calculate appearances, goals for/against, wins/draws/losses and points under the competition's actual rules. Verify totals, match identifiers and home/away treatment. Head-to-head statistics can describe a sample but do not isolate a persistent matchup effect across different coaches and squads.

**Point-in-time (PiT)** tables reconstruct what the standings or features were at a particular moment. Example 4.5 builds a table from the first 98 EPL games of 2020–21. **Advisor safeguard:** use only results completed before the forecasted kickoff, handle games in hand and simultaneous matches explicitly, and never attach the season's final rank to an earlier prediction. Both team-rows from one match must stay in the same train/test partition.

### Chapter 5 — End-of-season points, shot ratios and expected goals
**Pythagorean expectation** uses scoring and conceding to estimate performance; the chapter discusses football-specific fitted exponents and point predictions. These coefficients are empirical fits to historical competition data, not universal constants. Use this family as a baseline only after establishing sample and calibration; do not import baseball win formulas directly into a league with draws.

Useful descriptive quantities, with denominators checked:

- Goal difference = goals for − goals against.
- Goal ratio = goals for / (goals for + goals against).
- Total shots ratio (TSR) = shots for / (shots for + shots against).
- Total shots on target ratio (TSoTR) applies the same idea to on-target attempts.
- Goals-to-shots ratio = goals / shots, describing realized conversion rather than chance quality alone.
- **Expected goals (xG)** = sum of the estimated conversion probabilities of the shots. Record the provider/model and its inputs; distinguish penalties and open play where the decision needs it.

Shot ratios separate opportunity volume from the final score but do not measure opportunity quality. xG adds modelled quality, while goals minus xG mixes finishing, chance and model error. Summing expected goals is justified by expectation; turning that sum into an exact-match score distribution requires further assumptions. A post-match xG total is not a pre-match forecast, and a low conversion rate alone cannot identify shot distance or goalkeeper performance.

### Chapter 6 — Match forecasting
**Poisson regression:** arrange historical games into team/opponent scoring observations, estimate attack/defence and home effects, then predict positive goal means. A coherent notation is `G ~ Poisson(lambda)`, `log(lambda) = linear predictor`, so `lambda = exp(linear predictor)`. The link concerns the mean, not the observed goal count; zero goals remain possible. Do not use the malformed sum of exponentials appearing in the supplied equation rendering.

Under an independent-goals baseline, score probability is `Poisson(h; lambda_home) × Poisson(a; lambda_away)`. Sum cells with h>a, h=a and h<a for home win, draw and away win. Choose a sufficiently wide score grid and report omitted tail mass; do not silently normalize a short grid and call it exact. Rates based on match results differ from shot-level xG even if both are called expected goals.

**Dixon–Coles:** adjust the low-score cells 0–0, 1–0, 0–1 and 1–1 to address dependence the simple model misses. Its parameter must be estimated under valid probability constraints. The book's implementation is a simplified extension, not a complete specification of every time-weighted Dixon–Coles variant; it does not justify asserting that every corrected low-score cell increases.

The chapter also demonstrates random forests using betting odds and conditional inference trees. Compare their performance against sensible simpler and market baselines on unseen games. If odds are inputs, the model is partly using market knowledge; it is not an independent discovery of the same information.

**Advisor validation:** split by prediction time, select/tune using training/development data, and reserve final evaluation. Report probability calibration and a proper score such as log loss or Brier score, not accuracy alone. A small last-round demonstration cannot establish durable profitability or superiority across leagues. Forecast uncertainty also includes estimated rates and changing teams, not merely the conditional Poisson randomness.

### Chapter 7 — Betting strategies as a probability check
The chapter covers roulette, value betting, arbitrage and money management. For decimal odds o and a defensible win probability p, expected net return per unit stake is `p*o − 1`. An edge exists only under that probability estimate and actual attainable terms. An overround calculation or a profitable historical backtest does not establish a future edge. Football advising does not need to turn these methods into betting recommendations; their useful role here is exposing the difference between likelihood, payoff and uncertainty.

### Chapter 8 — Passing networks
**Required evidence:** passes with identified passer/receiver, team, period and preferably timestamp/location. Build a directed adjacency matrix; specify whether an edge means an available connection or a weight counting completed passes. Use separate team graphs and describe the selected lineup/time window.

**Size** is node count. For k nodes without self-loops and L observed directed connections, **density** is `L/[k*(k−1)]`; it is not the maximum edge count. **Diameter** is the longest shortest path; **average path length** summarizes shortest paths. **Degree centrality** counts adjacent connections; in/out-degree differ, and weighted pass volume is strength rather than binary degree. **Betweenness** concerns shortest-path brokerage; **closeness** concerns path distance; **PageRank** incorporates the importance of incoming connections. Define the metric, graph direction and weight treatment before ranking players.

**Advisor safeguards:** report disconnected nodes and how distances are handled. High pass counts are connection strengths, so do not feed them blindly as path lengths. Whole-match aggregation can invent apparent routes between players who were never on the pitch together; segment by lineup and game state when needed. A central player can circulate safely while adding little threat. Network prominence alone is not possession value, causal indispensability or evidence of an off-ball run.

### Chapter 9 — Rankings answer different questions
- **Colley:** solves a schedule-adjusted rating system with a wins-minus-losses component and smoothing. Draws do not add to the wins-minus-losses vector, but match counts/opponent structure still matter. Its omission of winning margin is a deliberate choice, not lack of any opponent adjustment.
- **Massey:** fits differences in team ratings to scoring margins by least squares. Fix a location constraint, inspect disconnected schedules and consider whether large margins dominate the intended comparison.
- **Elo:** updates ratings sequentially by `new = old + K*(result − expected result)`, with wins/draws/losses conventionally scored 1/0.5/0. That expected score is not automatically the win probability when draws are possible. Starting ratings, update size, home advantage and ordering affect output.

Select a ranking for the decision: relative season strength, strength of schedule or evolving predictive strength. Validate forecast use separately. Colley and Massey do encode opponents; the source's broad contrast with Elo should be read as emphasizing sequential updating, not as removing their schedule matrices. No rating is a measure of a coach's isolated causal contribution.

### Chapters 10–11 — Regression, variable importance and analytical judgment
OLS finds a linear prediction minimizing squared residuals. Multiple regression estimates conditional relationships; correlated predictors can substitute for one another. Variable importance depends on model, scale and sample, not only on football importance. A dropped variable or wide coefficient interval does not prove irrelevance.

Check functional form, residual patterns, unequal variance, dependent errors, influential observations and collinearity. Normal errors concern the model's inferential assumptions, not a demand that all predictors are normal. Repeated matches and derived features require care: adding several transformations of the same quantities does not supply several independent pieces of evidence.

Plan the analysis before searching for a pleasing result; understand data provenance and what matters to the sport. Beggs warns against both treating correlation as causation and dismissing every association without investigation. Use the association to generate a mechanism and discriminating evidence; do not relabel the regression coefficient as the effect of a coaching intervention.

Beggs retains classical tests as useful tools while warning against a rigid p=0.05 decision boundary; McElreath builds inference without significance testing. Preserve that methodological difference. A p-value is a tail probability under the null model and test assumptions, not the probability that chance caused the result or that the hypothesis is false. Neither a non-significant comparison nor a narrow Bayesian interval settles the football decision. For continuous forecasts, Beggs also demonstrates mean absolute error: average the absolute prediction errors, not signed errors that can cancel.

## Worked Example — Reconstruct the book's held-out Poisson exercise
Chapter 6, Example 6.2 fits the first 370 EPL matches of 2018–19 and forecasts the remaining ten. Reconstruct it by preserving chronological data, reshaping only the training matches into home/away scoring rows, fitting a log-link team/opponent/home model and predicting each held-out fixture. Inspect the low-score assumptions before adding Dixon–Coles. The supplied book data were not downloaded or refitted for this distillation; no replicated match probabilities are claimed.

Original base-R implementation of the score-grid step, runnable after obtaining two fitted means:

```r
score_probs <- function(home_mean, away_mean, max_goals = 20L) {
  stopifnot(length(home_mean) == 1L, length(away_mean) == 1L,
            is.finite(home_mean), is.finite(away_mean),
            home_mean >= 0, away_mean >= 0,
            length(max_goals) == 1L, is.finite(max_goals),
            max_goals >= 0, max_goals == floor(max_goals))
  g <- 0:max_goals
  joint <- outer(dpois(g, home_mean), dpois(g, away_mean))
  c(home = sum(joint[row(joint) > col(joint)]),
    draw = sum(diag(joint)),
    away = sum(joint[row(joint) < col(joint)]),
    omitted_tail = max(0, 1 - sum(joint)))
}
# Hypothetical rates, not a forecast of an actual fixture:
score_probs(1.5, 1.0)
```

Expected arithmetic check: probabilities are approximately home 0.488, draw 0.260 and away 0.252, with negligible tail at this grid size. This is conditional on fixed independent rates; it does not include uncertainty in the fitted means. The R snippet was not run in R during this build; the same equations were checked independently in Python and the verification record states that distinction.

## Decision Rules & Judgment
- If a feature was unavailable at kickoff, exclude it from that forecast even if it improves retrospective fit.
- If two metrics share a denominator or underlying events, inspect dependence before treating them as separate evidence.
- If a model predicts well, retain it for that tested task; do not infer an intervention effect from prediction alone.
- If a network crowns a player, ask which kind of centrality and which possessions produced the ranking.
- If performance improves only on training data, investigate overfitting and selection before increasing confidence.
- If the input, formula or code has not been executed, say so; distinguish a proposed method from a computed result.

## Key Takeaways
1. Preserve data provenance, timing and definitions so another analyst can reproduce the result.
2. Match method to question: opportunity quality, outcome forecasting, network role and causal explanation differ.
3. Make uncertainty and out-of-sample performance part of the result, not an afterthought.
