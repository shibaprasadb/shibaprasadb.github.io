---
title: "Cursorbench Evals: The Effect of Family & Cost"
date: 2026-07-09
tags: ["product", "technical"]
description: "Running some statistical analyses for Cursor Bench evals"
image: "https://shibaprasadb.github.io/images/posts/2026-07-09-cursorbench-analysis/cursorbench_revamped.png"
---

I was going through the [Cursor Bench](https://cursor.com/evals) evals.

The plot that they had used was a bit deceiving & counter intuitive. It had the X axis starting from 20 (the highest value).

![Cursor Bench - Different AI models](/images/posts/2026-07-09-cursorbench-analysis/cursor_bench_models.png)

So, I thought of cleaning the plot a bit, in order to have a better clarity.

I reversed the X axis, and added all the numbers that they had mentioned in the table but were not included in the plot. After that, it looked like this:

![Cursor Bench - Revamped ](/images/posts/2026-07-09-cursorbench-analysis/cursorbench_revamped.png)

Now, this cleaned plot, looked interesting to me.

- The cost vs accuracy kinda follow a concave curve. (logarithmic)
- Composer 2.5 (Cursor's own model) looks like an outlier.

So, let's run two simple linear regressions.


Let's gather all the outputs in this table:
 
| Model characteristics | n | R² | p-value |
|---|---|---|---|
| score ~ cost, with Composer | 36 | 0.593 | 3.97e-08 |
| score ~ cost, without Composer | 34 | 0.664 | 4.56e-09 |
| score ~ log(cost), with Composer | 36 | 0.545 | 2.74e-07 |
| score ~ log(cost), without Composer | 34 | 0.815 | 2.79e-13 |


Now, we got some idea about this. Before summarising what is happening, let's run another type of regression. Linear mixed effects model.
 
A linear mixed model is a regression that separates two things at once: an overall slope you care about (here, the effect of log(cost) on score), and group-level variation you want to account for but not estimate one-by-one (here, each model family's own baseline). It's useful whenever your rows aren't fully independent, like model variants nested inside families, because it stops that internal correlation from making your effect look more certain than it actually is.

Here is the result:

```
Random effects:
 Groups   Name        Std.Dev.
 family   (Intercept) 6.843   
 Residual             2.873   
 
Fixed Effects:
(Intercept)    log(cost)  
     45.522        9.666  
```

Now the story time, what this means?

1. **Cost does buy score, but the returns are sharply diminishing.**

All the models that we used, roughly agrees with this. Log(cost) beats raw cost if Composer is removed. And the slope of the mixed model also confirms it - doubling cost buys roughly 6.7 points [^1], consistently, once you control for which family you're in.

2. **Curios case of Composer**

Composer is developed by Cursor, and it broke the log(cost) structure completely. For the statistical analysis, we filtered it out as an outlier. But the more honest reading might be (if the numbers to be believed) : it is a well optimised cheap model.

3. **Family matters**

The mixed model splits the leftover variance (whatever cost doesn't explain) into two parts: how much comes from which family versus everything else. Squaring the standard deviations and comparing them, family accounts for ~85% of that leftover variation, noise only ~15%. In plain terms: pick two model variants at the same price, and which family they belong to explains most of the score gap between them.

---

So, putting together, the cost component has two parts. More spending gives you better accuracies, but the family of the model matters too. Family seems to be a coarse lever, you move from one to another, and get a bump in the accuracy. Turning efforts within a family seems like a finer scale.

One analogy I can think of - hiring vs overtime problem. Hiring the right people can yield better results than the wrong people working on weekends. No amount of overtime can fix that hiring gap.

This is where the judgement of the operator using the tool would be very important. You should ideally want to use a "weaker" model for more trivial problems. If you want to optimise the token cost. In data science, it is important to know which model to use when. This translates to that philosophy roughly - one needs to know which API call is needed for a particular problem.

-----

[^1]: The mixed model gives predicted score as f(cost) = 45.522 + 9.666 · ln(cost). To find the effect of doubling cost, compare f(2c) to f(c):

        f(2c) − f(c) = 9.666 · [ln(2c) − ln(c)]
                     = 9.666 · ln(2c / c)
                     = 9.666 · ln(2)
                     = 9.666 × 0.693
                     ≈ 6.7

    The intercept and c cancel out entirely, so this ≈6.7-point gain is constant regardless of starting cost, the defining property of a log-linear relationship.




