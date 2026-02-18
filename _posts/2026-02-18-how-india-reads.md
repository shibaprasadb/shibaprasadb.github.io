---
title: "Reading the Numbers: How India Reads"
tags: ["data-stories"]
date: 2026-02-18
description: "Utility, trade books, and what the numbers actually say about Indian reading habits."
image: "https://shibaprasadb.github.io/images/posts/2026-02-18-how-india-reads/trade_book_spending.png"
---

Guardian published an article on 9th Feb 2025. The post titled ["Most Indians don't read for pleasure - so why does the country have 100 literature festivals?"](https://www.theguardian.com/global-development/2026/feb/09/books-india-literature-festivals-readers) garnered a lot of attention (the title was changed later). [Outlook India](https://www.outlookindia.com/culture-society/the-guardian-cant-question-profusion-of-lit-fests-india-reads-writes-and-celebrates-words) refuted some of the claims in their own way. And Anurag Minus Verma penned down a brilliant essay on [why don't Indians read for pleasure](https://www.theculturecafe.in/p/why-dont-indians-read-for-pleasure).

I related a lot to the essay by Anurag Verma. He argued that most of our readings are utility driven i.e. we read because we have to.

Among all these debates and discussions, I felt we were missing one point: how is India different from other nations?

I don't have a lot of foreign associates. But from the little I have accumulated, it didn't feel like others were drowning themselves in books while India alone wasn't reading. It is a contemporary issue that transcends borders, regions and seas.

So the question arose:

## How do Indians read compared to other countries?

And the only way we can answer this is through data.

I looked at this from two angles:

- What is the buying pattern of different countries with respect to genre?
- How much, on average, is an Indian spending on trade books?

Let's dissect the first one:

![Revenue share for different genres](/images/posts/2026-02-18-how-india-reads/ranked_genres.png)

In terms of revenue share, Indians are spending far more on educational books than the US, UK or European countries. So Anurag's point is not completely wrong. And intuitively, that makes sense.

But now, let's look at it from another angle: as a percentage of GDP, how much are Indians spending on trade books (i.e. excluding educational books)?

![Trade book spending as a % of GDP](/images/posts/2026-02-18-how-india-reads/trade_book_spending.png)

An average Indian is actually spending more on trade books than an average US and European citizen. But less than the UK.

This shows that when it comes to buying non-educational books, Indians are more intentional compared to more developed nations. Because when you are spending more of your hard earned money, inspite of being a poorer country per-capita GDP wise, you need to be more intentional.

One methodological note: this analysis uses nominal GDP per capita as the denominator. Book prices vary across markets. A $10 US paperback might be ₹400-600 in India, depending on the publisher and format - but books are globally traded goods with some price convergence, unlike purely local services. Using nominal figures keeps the comparison straightforward, though a full [PPP adjustment](https://en.wikipedia.org/wiki/Purchasing_power_parity) could be explored in future work.

As usual, reality is far from a clean black-and-white thing. It is much more nuanced. On average, Indians tend to read more for utility, but we also tend to spend more on non-utility books.

This also raises an interesting question: what happens when India’s per capita GDP rises? More surplus should lead to more spending on pleasure?

---

### Notes & Sources

**Trade books** are commercially published books sold to the general public, excluding educational textbooks, academic journals, and professional reference materials. In this analysis, trade books = Fiction + Non-Fiction.

**Data note:** All book market figures reflect 2024 actuals from industry sources (Horizon Databook, FEP, Nielsen). GDP per capita figures are from 2024-2025; US figures use 2025 IMF projections. Year-on-year differences are negligible (<2%) and do not materially affect the conclusions.

**Calculation methodology:** Trade book spending per capita was derived by multiplying total market size by the trade book revenue share (Fiction + Non-Fiction %), then dividing by population. This was then expressed as a percentage of nominal GDP per capita.

| Country | Market Size | Trade Share | Trade Per Capita | GDP Per Capita | % of GDP    |
|---------|-------------|-------------|------------------|----------------|-------------|
| India   | $10.37B     | 29–51%      | $2.05–$3.56      | $2,730         | 0.08%–0.13% |
| US      | $40.44B     | 52–56%      | $61.76–$66.47    | $85,000        | 0.07%–0.08% |
| UK      | $8.94B      | 65–75%      | $85.44–$98.53    | $56,000        | 0.15%–0.18% |
| Europe  | $29.03B     | 51%         | $32.89           | $49,000        | 0.07%       |

The plot uses the mean of each range as the representative value.

---

**India**
- Market size: $10.37B (Horizon Databook) [1]
- Educational: 60.2% mean revenue share (Horizon [1], IBEF [2])
- Fiction: 17.5% revenue share, +30.7% YoY growth [1][2]
- Children's: 9.8% revenue share [1]

**United States**
- Market size: $40.44B (Horizon Databook) [3]
- Fiction: 32.8% ($3.26B), +12.6% YoY (AAP) [4]
- Children's: 24.7% [3]
- Educational: 19.8% [3]
- Non-Fiction: 19.2% ($2.88B), +1.3% YoY (AAP) [4]
- Religious/Professional: 3.5% [3]

**United Kingdom**
- Market size: £1.82B physical (Nielsen) [5]
- Fiction: 42.5% mean revenue share, record high, +18% YoY [6]
- Non-Fiction: 27.5% [7]
- Educational: 17.4% (Horizon) [8]
- Children's: 12.6% [5][8]

**Europe**
- Market size: €24.9B (FEP) [9]
- Fiction: 27.5% [9]
- Educational: 23.3% mean (FEP [9], Horizon [10])
- Non-Fiction: 22.5% [9]
- Academic/Professional: 16.7% [9]
- Children's: 14.6% [9]

---

**Citations**

[1] Grand View Research/Horizon Databook. India Books Market Size & Outlook, 2025–2033. https://www.grandviewresearch.com/horizon/outlook/books-market/india

[2] IBEF. India's Meteoric Rise as a Publishing Hub. https://www.ibef.org/blogs/india-s-meteoric-rise-as-a-publishing-hub

[3] Grand View Research/Horizon Databook. US Books Market Size & Outlook, 2025–2033. https://www.grandviewresearch.com/horizon/outlook/books-market/united-states

[4] AAP via Publishing Perspectives. December StatShot: US Book Market Up 6.5% Year-to-Date. https://publishingperspectives.com/2025/03/aaps-december-statshot-us-market-up-6-5-percent-year-to-date/

[5] Nielsen BookData. Bestsellers & trends in the UK & Ireland in 2024. https://nielseniq.com/global/en/insights/commentary/2025/bestsellers-trends-in-the-uk-ireland-in-2024/

[6] Friedman, Jane. Book sales update: UK market. https://janefriedman.com/book-sales-update-uk-market/

[7] LoveReading. Fiction Book Sales in 2024 Top The Lot. https://www.lovereading.co.uk/blog/fiction-book-sales-in-2024-top-the-lot-while-non-fiction-lags-behind-9226

[8] Grand View Research/Horizon Databook. UK Books Market Size & Outlook, 2025–2033. https://www.grandviewresearch.com/horizon/outlook/books-market/uk

[9] Federation of European Publishers (FEP). European Book Publishing Statistics 2024. https://www.fep-fee.eu/European-Book-Publishing-Statistics-2024

[10] Grand View Research/Horizon Databook. Europe Books Market Size & Outlook, 2025–2033. https://www.grandviewresearch.com/horizon/outlook/books-market/europe
