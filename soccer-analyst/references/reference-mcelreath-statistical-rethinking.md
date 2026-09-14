# Statistical Rethinking: A Bayesian Course with Examples in R and Stan — Richard McElreath
**Format**: supplied Markdown | **Edition**: first edition, 2016 | **Sections**: 15 | **Depth**: study
**Use for**: small samples, extreme performances, Bayesian updating, model checking, causal restraint, partial pooling and missing evidence.

## Mental Model (read first)
A statistical model is a deliberately limited machine: it obeys its assumptions, not the analyst's hopes. Bayesian updating is coherent inside the model's **small world**, but coherence does not show that the model represents the **large world**. Build the generative story, inspect what it predicts, and revise it when its implications conflict with evidence. The useful outcome may be that the data cannot distinguish the explanations.

**Source boundary:** This is the 2016 first edition, including `map`/`map2stan`, WAIC, multilevel models and measurement error. Do not attribute the second edition's chapter structure or later software workflow to it. Equations below are reconstructed notation, not converted-page transcriptions. Football examples and model adaptations are this library's synthesis; the book is not a football dataset or a source of player-specific priors.

## Frameworks & Structure

### Chapters 1–2 — The golem, small worlds and Bayesian updating
**Question:** How much should the observations change a prior assessment? **Required evidence:** a clearly defined outcome, sample/exposure, observation process and a defensible set of alternative parameter values or models.

Specify likelihood, parameters and priors. The posterior satisfies `p(theta | y) ∝ p(y | theta) p(theta)` and remains conditional on the chosen model. Likelihood describes data given parameter values; it is not the probability that a claim or model is true. A parameter can represent uncertainty about an otherwise missing or imperfect datum.

The **garden of forking data** motivates updating by counting ways observations can arise. **Grid approximation** makes that logic explicit for simple low-dimensional problems; quadratic approximation is convenient near Gaussian posteriors but can misrepresent boundaries, skew or multiple modes. Complexity can require simulation rather than a more confident approximation.

Priors are assumptions to examine, not hidden evidence or arbitrary knobs for a preferred answer. Use substantive scale constraints and prior predictive implications. When several priors are plausible, show whether the decision changes across them. Do not count the same season once in the prior and again in the likelihood. An unchanged-ability model and a changing-ability model make different claims; shrinking a hot streak is not proof that improvement is impossible.

### Chapter 3 — Sampling the imaginary and deciding under loss
Posterior samples support interval estimates, threshold probabilities and contrasts. Define the event before reporting its probability: exceeding last season's rate, exceeding a replacement's rate, or scoring next match are different events. A credible interval summarizes parameter uncertainty under the model; a predictive interval includes new-outcome variation as well.

**Posterior predictive simulation:** draw parameters from their posterior, simulate observations conditional on each draw, then inspect distributions and relevant features against real data. Plugging in a mean parameter can understate uncertainty. A predictive check asks whether the model generates plausible data, not whether it has discovered the true mechanism.

**Loss functions** connect uncertainty to action. The posterior mean, median and mode need not give the same decision because different errors have different costs. In football, overpaying for a fragile starter and missing a cheap squad option may warrant different thresholds. State those stakes and assumptions; do not manufacture a numerical expected utility when costs are unknown.

### Chapter 4 — Linear models and coherent prediction
Write the outcome distribution and linear predictor separately, including scale parameters and priors. Center or standardize predictors when it aids interpretation, preserving the transformation. Inspect implied predictions across the data range before extrapolating. Polynomial terms can bend a curve without supplying a plausible mechanism outside the observed range.

A regression line for expected performance is narrower than the distribution of individual future performances. Report which one is displayed. A very confident line can coexist with noisy match outcomes and uncertainty about model applicability.

### Chapter 5 — Spurious association, masking and bad controls
Multiple regression addresses conditional comparisons; it does not automatically turn observational data into an experiment.

- **Spurious association:** two quantities can correlate because of a common influence. More possession and more wins could both reflect team strength, or possession can respond to score state.
- **Masked relationship:** correlated predictors with opposing associations can conceal one another in separate regressions. Inspect a substantively motivated joint model rather than declaring either effect absent from its bivariate plot.
- **Multicollinearity:** several combinations of coefficients can explain almost the same data. Wide individual coefficients need not mean a variable is useless for prediction. Adding near-duplicate possession/progression measures can make attribution unstable.
- **Post-treatment bias:** controlling for a consequence of an intervention can remove the pathway being estimated. To estimate the total effect of a pressing change, conditioning on the regains it produces asks a different question. Decide the estimand and causal ordering first.
- **Categorical variables:** use an explicit coding/reference scheme and compare the desired contrasts. A contrast between coefficients requires its own uncertainty; “significant here, not there” is not evidence that two effects differ.

The first edition's plant-treatment example illustrates how controlling for fungus hides a treatment operating through fungus reduction. Football applications inherit the reasoning, not experimental identification. Do not claim causation merely because a longer list of controls was fitted.

### Chapter 6 — Overfitting, regularization and information criteria
**Overfitting** learns peculiarities of the observed sample that fail on new data. **Regularizing priors** restrain implausibly strong associations and can trade worse training fit for better prediction; excessive restraint underfits. Choose scales using the meaning of variables and check sensitivity. A Gaussian prior on a standardized slope is interpretable only alongside the outcome's units.

Information theory compares predictive distributions through log probability and information loss. AIC, DIC and **Widely Applicable Information Criterion (WAIC)** estimate predictive performance under their assumptions; they are not votes for causal truth. WAIC uses each observation's posterior likelihood and its uncertainty. In conventional notation, `WAIC = -2*(lppd - p_WAIC)`; damaged minus signs in the supplied conversion must not reverse the criterion.

Compare like outcomes and data, show the difference and its uncertainty, and avoid announcing a winner from a negligible gap. The book explicitly warns that pointwise exchangeability can fail for time series and that predictive targets matter in multilevel models. **Football application:** hold out the time period, match or group relevant to the intended future use; randomly splitting correlated rows can answer an easier question than forecasting a new season. Tuning on a set makes it development data, not untouched final evidence.

### Chapter 7 — Interactions
An interaction lets an association depend on another variable. For `mu = a + b*x + c*z + d*x*z`, the slope for x is `b + d*z`. Evaluate and visualize relevant combinations, preferably as predicted outcomes and contrasts rather than isolated coefficients. The interpretation is symmetric: x modifying z and z modifying x describe the same term unless outside knowledge supplies direction.

**Football application:** a striker's output may depend on delivery style or teammate support. Check whether the data include the proposed combinations. An estimated interaction cannot justify transporting the player to an unseen tactical environment without uncertainty.

### Chapter 8 — Markov chain Monte Carlo
**MCMC**, including **Hamiltonian Monte Carlo (HMC)**, samples a complex posterior; more iterations do not make the model's assumptions true. Distinguish warmup/adaptation from retained posterior draws. Inspect chains, convergence evidence, effective sample size and sampler warnings before reporting intervals. Effective sample size differs from raw draws, and tail probabilities need more information than posterior means.

The first edition's sampler interfaces and numerical advice are historical. If executing today, verify the installed implementation and applicable diagnostics. No executed model means no claimed convergence. A small numerical error estimate describes computation under a model, not total uncertainty about football.

### Chapters 9–11 — Outcome distributions, links and mixtures
**Maximum entropy** helps motivate distributions under specified constraints; it is not permission to ignore domain structure. A **generalized linear model** connects a linear predictor to an outcome mean/probability through a link appropriate to its support.

- **Binomial with logit link:** successes out of a known number of trials. Shots vary in difficulty, so one common conversion probability is a simplification requiring justification.
- **Poisson with log link:** counts conditional on a mean; a log-exposure offset can distinguish scoring rate from time played. Do not compare raw counts as though all players had identical minutes.
- **Other count models:** categorical/multinomial outcomes and relative probabilities require their own likelihood; a win/draw/loss outcome is not a normally distributed score.
- **Ordered categorical outcomes:** ordered-logistic models retain order without assuming equal numerical distance between ratings.
- **Zero-inflated outcomes:** distinguish a separate zero-generating process from ordinary zeros. Do not infer that every goalless appearance belongs to an “unable to score” class.
- **Over-dispersed outcomes:** beta-binomial and gamma-Poisson mixtures let probabilities or rates vary beyond a simple homogeneous model. Diagnose the heterogeneity rather than assuming every extra parameter improves inference.

Each choice encodes how the data could arise. Check exposure, dependence, support and simulated predictions before trusting a convenient family.

### Chapter 12 — Multilevel models and partial pooling
**Required evidence:** meaningful clusters, repeated observations and a defensible claim that groups can inform one another. Complete pooling discards real group differences; no pooling lets tiny samples produce unstable extremes. **Partial pooling** estimates group parameters while learning their shared distribution, allowing uneven information to produce appropriately different shrinkage.

The tadpole example models survivors out of each tank's initial count, with tank-specific log-odds drawn from a shared distribution. Football adaptation: player finishing effects can vary around a role/competition population while controlling shot difficulty. That is a proposed model, not proof that every forward belongs to one interchangeable population. Grouping across leagues or roles needs support; otherwise pooled precision can hide transfer error.

A prediction for an existing player uses information about that player. A prediction for a new player requires uncertainty over the group distribution. Setting a new player's effect to the population mean and ignoring variation understates prediction uncertainty. “Shrink toward average” is not an arbitrary fixed discount and does not establish that the population mean applies equally everywhere.

### Chapter 13 — Covariance and varying slopes
Allow both baseline and response to predictors to vary by group when the evidence and question warrant it. Model their covariance rather than treating all variation as independent. Cross-classified effects can represent membership in several kinds of cluster; Gaussian processes extend partial pooling to similarity or distance rather than just identical labels.

**Football application:** player, team and opponent effects overlap; nominal league labels may not capture similarity. Use these models only with adequate data, interpretable structure and successful computation. More elaborate covariance cannot identify separately what the observation design leaves confounded.

### Chapter 14 — Measurement error and missing data
Replace an uncertain measurement with a distribution when its error information is available, propagating it through the model. Treating estimated wages, shot quality or player ratings as exact inputs risks false precision.

The book's missing-neocortex example models missing values jointly with observed predictors and outcomes, retaining information otherwise discarded by complete-case analysis. Its introductory imputation assumes **Missing Completely At Random (MCAR)**. Report that assumption and do not generalize its success to selective missingness. A league lacking tracking, undisclosed transfer clauses or missing injury histories may be systematically different. Imputed values remain model-based uncertainty, never newly observed facts.

### Chapter 15 — Horoscopes
Statistical inference supports structured learning, not ritual certainty. Keep the scientific question, generative explanation and checks visible. The concluding warning is especially relevant to football: a precisely reported probability can still be a horoscope if the model or evidence does not address the decision.

## Worked Example — Six water observations in nine globe tosses
Reconstruction of the first edition's Chapters 2–3 example. Let W be the number of water observations and assume independent tosses with a common unknown probability p. With W=6, n=9 and a uniform prior on p, the binomial likelihood updates the prior to `Beta(7,4)`.

The posterior mean is 7/11, about 0.636; the likelihood's observed proportion is 6/9, about 0.667. Neither is a known true value. A new ten-toss count has expected value `10*7/11`, but its predictive distribution averages binomial outcomes over the whole posterior, not just over the mean p. Changing the prior or observation assumptions can change the result.

Original base-R reconstruction:

```r
set.seed(2016)
p <- rbeta(100000, 7, 4)
quantile(p, c(.055, .945))       # an 89% posterior interval
new_water <- rbinom(length(p), size = 10, prob = p)
mean(new_water)                 # Monte Carlo estimate, near 70/11
```

The script illustrates the method and was not run in R during this build. The conjugate arithmetic was independently checked. **Football transfer boundary:** six goals from nine shots cannot be treated as nine identical trials without addressing shot difficulty, selection and context. Use the toy calculation to understand updating, not to forecast a player's career.

## Decision Rules & Judgment
- If a probability is quoted, identify its event, model, data and assumptions; a verbal hunch is not a fitted posterior.
- If a player looks exceptional in few minutes, compare plausible regularized and changing-ability explanations before extrapolating.
- If controlling for a variable changes the verdict, ask whether it removes confounding, masks a pathway or creates an unstable comparison.
- If two models predict similarly, preserve that uncertainty instead of declaring a winner from a tiny criterion difference.
- If predicting a new group, integrate group uncertainty rather than reusing an existing group's estimated effect.
- If missingness is selective or measurements are noisy, investigate the observation process before adding numerical precision.
- If a model gives a narrow interval around an implausible mechanism, repair the model rather than celebrate the interval.

## Key Takeaways
1. Separate model coherence, computational reliability and fit to the real question.
2. Priors, likelihoods, pooling and observation assumptions all affect how much new evidence should change a judgment.
3. Simulate predictions and show sensitivity; uncertainty should change the decision or the next evidence sought.
