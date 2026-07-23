---
title: "Why AI Will Continue to Be Good at Bad Strategy"

date: 2026-07-23

tags: ["strategy"]

description: "Good strategy requires a diagnosis and a choice. AI prefers a plausible list."

image: "https://shibaprasadb.github.io/images/posts/2026-07-23-ai-bad-strategy/ai_bad_strategy.png"
---

In one of the recent episodes of Lenny’s Podcast (with the head of Instagram), Lenny made a comment about AI and strategy. He had expected AI to be good at strategy, but that hasn’t been the case.

<iframe width="560" height="315" src="https://www.youtube.com/embed/yQ_EWmtfWvQ" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


I never thought AI could be good at strategy. Even though there has been some hype around that, if we go one level deeper into how GenAI models work and what makes a strategy good, we can easily figure out why they will always be suboptimal at strategy.

But, on the other hand, they will always be quite good at bad strategy. The distinction is real.

Let’s first understand the grains of a good strategy. And a bad one.

## What makes a strategy good?

This is not something that I am spitting out of thin air. I am borrowing the framework of strategy god [Richard Rumelt](https://en.wikipedia.org/wiki/Richard_Rumelt). According to him, a good strategy has three kernels: a diagnosis, a guiding policy and a set of coherent actions.

A diagnosis names or classifies the situation, linking facts into patterns and suggesting that more attention be paid to some issues and less to others. It basically answers: What is going on?

The guiding policy highlights the overall approach for overcoming the obstacles identified by the diagnosis. It creates advantage by anticipating the actions and reactions of others, and by reducing the complexity and ambiguity in the situation.

A set of coherent actions is then designed to carry out the guiding policy.

Rumelt has also defined bad strategy at length. Bad strategies are full of fluff. They are long on goals and vision. But a strategy should give you the tools to face the challenge. And, most importantly, it should identify the challenge at hand. Bad strategies don’t do that.

## How do LLMs work?

Large language models like ChatGPT or Claude are trained on an enormous amount of data: books, websites, articles, code and much more. They learn statistical patterns in language, including how words appear together, how arguments are structured and how concepts relate to one another. From all that data that already existed.

They process text as tokens: small units that may be words, parts of words or even punctuation. The model is autoregressive, generating one token at a time (mostly!) based on everything that came before it. What feels like reasoning therefore emerges from a very sophisticated probabilistic system operating over a vast learned pattern space.

This is, of course, a generalised version of how LLMs work. But it is enough for the argument here.

## Ill-structured vs structured domains

LLMs have seen massive uptake in work related to structured domains, such as software engineering or mathematics. Here, the past training data is quite helpful. The rules of the game don’t change.

The logic for writing a while loop is constant. 2+2 will always be four. The models are trained on that data, so they can produce the output when prompted.

Strategy sits in an ill-structured domain. The real, messy business world. Every case here is different and unique in some way. What helps here is [cognitive flexibility theory](https://www.sciencedirect.com/topics/psychology/cognitive-flexibility-theory). It says that in ill-structured domains, you don’t just learn one rule or framework and apply it everywhere. You learn a set of rules by criss-crossing the same terrain from multiple angles, building a library of cases, and picking the right lens depending on what you’re actually looking at. It’s the opposite of pattern-matching to the nearest precedent, which, awkwardly, is close to the only thing an LLM knows how to do.

And if you look closely at how LLMs are trained, cognitive flexibility is an awkward game for them. Not impossible, but it is not their natural mode either. Their strength lies in finding and recombining patterns from what they have already seen. Good strategy requires a more selective kind of pattern recognition: identifying which previous situations are relevant, where the similarities end and why the current situation may demand a different response.

The same facts can usually support several plausible diagnoses. An LLM tends to preserve many of them and produce a comprehensive answer. (which looks promising!) 

Good strategy requires choosing one diagnosis to govern the others. And accepting what that choice leaves out.

## Connecting the dots

Now say you are inside an organisation. Your organisation is facing an issue, and you want to devise a strategy around it. How can AI help in creating that good strategy? Especially with the underlying training logic that we just discussed.

For example, let’s consider a food-delivery app. Their growth has slowed down for the past 2 months. You need to devise a strategy to improve that situation. Now, you give the whole detailed scenario and ask an LLM for a strategy. It will probably suggest something along the lines of improving retention, introducing loyalty awards, new & better recommendations etc. All of these may sound sensible on the superficial level. But none of them is a strategy yet.

Once you investigate, you may find the actual issue, which can be narrower. Maybe the loyal-frequent users of the company are not ordering not because of the price or poor recommendations, but because delivery times have become unpredictable during the weekday office hours. These peak time deliveries contribute ~30% to the total order volume, but the company has not been able to maintain a stable service level during those hours.

Then the guiding policy might be to improve density and reliability in those neighbourhoods rather than chase growth everywhere. The coherent actions would follow: restrict the delivery radius during peak hours, recruit more delivery executives (maybe temps for weekdays) around those clusters and change restaurant incentives to reduce preparation delays.

An LLM can generate those actions once the diagnosis is given - sometimes. You would need to spend time feeding the info about the competitive landscape, business constraints, etc. But identifying the diagnosis is one of the biggest obstacles of Rumelt’s framework. It requires company-specific data, conversations with the ops team, judgement and an understanding of what is changing underneath the averages.

Without that diagnosis, what would the model do? It would generate fluff. And that would be convincing to many people who might not be well versed in what a good strategy should look like.[^1] It would recommend something like customer centricity. Or Operational excellence. Or say sustainable growth. You get the drift.

This is why AI is good at bad strategy. Bad strategy is linguistically impressive, but it lacks the analytical diligence. It resembles the thousands of strategy documents, consulting decks, annual reports and leadership speeches that the model has already seen. And for that reason, it can reproduce those patterns exceptionally well. But more often than not, they would have no intrinsic value.

Is it totally useless? What can it help with instead? Market research, for one, surely. But even there, one needs to be more specific. “How is Paytm different from PhonePe?” might not yield a structured response like “Compare how Paytm and PhonePe make money, using their latest public filings, and separate reported facts from inference”. The latter gives the model a much tighter research task.

---

I like to think that human and GenAI outputs work something like this. To some extent. This is kind of my mental model of their respective defaults:

![AI & Human](/images/posts/2026-07-23-ai-bad-strategy/ai_bad_strategy.png)

Human judgement is volatile. There are peaks and valleys. We produce plenty of terrible ideas, average ideas and occasionally something brilliant. And the path to brilliant ideas is often full of terrible ideas. There is no strict pattern. Expertise makes us more consistent. But even after that, the AI output is much more consistent.

That consistency is useful in many domains. Specially for well-structured domains. You may write suboptimal code one day - miss the ‘;’ or design something with O(N^2) complexity where a simpler solution already exists for that. AI will never make that kind of mistake. But good strategy is different. It sits above a threshold. It needs a diagnosis that cuts through the noise, a choice that excludes other choices and a set of actions built specifically for the challenge at hand.

The volatility in human output is an asset for strategy work. You need sharper, more coherent minds who can cross the threshold after months of interaction and sitting with other human beings & studying every angle. AI may keep missing it very reliably. Every damn time.

---

[^1] I also think good tech & business consultants will be in huge demand. Pretty soon.
