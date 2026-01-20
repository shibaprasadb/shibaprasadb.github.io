---
title: "From 75% to 99.6%: The Math of LLM Ensembles"
tags: ["technical"]
date: 2026-01-20
image: "https://shibaprasadb.github.io/images/posts/2026-01-20-llm-ensemble/flow_LLM_Ensemble.jpg"
---

The last project I worked on involved a lot of LLM API calls. One subtask seemed simple: count elements from a specific list. Straightforward, right? Not quite.

This needed production-level accuracy. But the simple API approach wasn't cutting it. After testing 50 cases, I was only hitting around ~75% accuracy (37 out of 50). For production, that's a non-starter.

## The Problem with Single API Calls

The LLM was doing the task correctly for some instances but missing elements in others. Sometimes it would catch all 10 items, other times only 7 or 8. The pattern was clear: when it failed, it undercounted. It never hallucinated extra elements or went above the true count. It just missed things.

This directional bias turned out to be the key insight.

## So I "Random Forest" It

I decided to apply the "wisdom of crowds" principle. The same concept that makes Random Forest work. Instead of relying on a single API call, use multiple calls and aggregate intelligently.

The evaluation rule was simple: **Max(API_call_1, API_call_2, ..., API_call_n)**

Example: If there are 10 elements and three API calls return [7, 10, 3], the final output is 10.

Why this works: The undercounting errors get filtered out. The max function naturally finds the correct answer as long as at least one call succeeds. Since the LLM never overcounts, the highest value is almost always the right one.

Here's how the two approaches compare:

![LLM Ensemble Flow](https://shibaprasadb.github.io/images/posts/2026-01-20-llm-ensemble/flow_LLM_Ensemble.jpg)

## The Math Behind It

With a single API call, the question is: What's the probability of success?

With ensemble, it becomes: What's the probability of at least one success?

The math changes drastically:

**P(correct) = 1 - P(all calls wrong)**

For n=3 calls with p=0.75 success rate:
- P(all wrong) = (1-p)ⁿ = 0.25³ = 0.015625
- P(at least one correct) = 1 - 0.015625 = **98.4%**

Going from 75% to 98.4% with just 3 calls? Not bad at all.

## Finding the Sweet Spot

But I couldn't just pick any number. Each API call costs money and adds latency. I needed to balance accuracy against cost.

Here's how the numbers break down:

| n calls | Accuracy | Cost Multiplier |
|---------|----------|-----------------|
| 1 | 75.0% | 1x |
| 2 | 93.8% | 2x |
| 3 | 98.4% | 3x |
| 4 | 99.6% | 4x |
| 5 | 99.9% | 5x |

![Success Rate](https://shibaprasadb.github.io/images/posts/2026-01-20-llm-ensemble/APICall_success_rate.png)

![Cost vs Accuracy](https://shibaprasadb.github.io/images/posts/2026-01-20-llm-ensemble/APICall_cost_accuracy.png)

The diminishing returns kick in hard after n=3. Going from 98.4% to 99.6% costs an entire extra API call for just 1.2 percentage points. But for production-level reliability, I decided that extra margin was worth it.

**I settled on n=4: 99.6% accuracy at 4x the cost.**

## When This Breaks

This approach only works because my LLM had a directional bias (like undercounting - in this case). The evaluation function must match your error pattern:

- **Undercounting errors** → Use Max()
- **Overcounting errors** → Use Min()
- **Random errors** (sometimes high, sometimes low) → Use majority voting with odd n (3, 5, 7) to avoid ties

The key is understanding *how* your model fails, not just *that* it fails. Directional biases can take many forms - summarization models that are consistently too brief, classifiers that favor certain categories, extractors that miss edge cases. Each needs its own aggregation strategy.

If you don't understand your failure mode, you're just burning money on redundant calls.

(Now that I think about it, we can dedicate a separate blogpost on designing Eval functions)

## The Takeaway

Sometimes the best solution isn't a better prompt or a bigger model. It's understanding your failure mode and exploiting it mathematically.

A single API call gave me 75% accuracy. Four calls with a simple Max() aggregator got me to 99.6%. Same model, same prompt. Just smarter approach.

The real lesson? When you can't improve the model's performance, improve how you use it. In an constrained space, solving a problem becomes more interesting.
