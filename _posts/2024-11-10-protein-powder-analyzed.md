---
title: "Protein Powders Analyzed: What the Data Says About Safety and Label Accuracy"
tags: ["data-stories"]
date: 2024-11-10
image: "https://shibaprasadb.github.io/images/posts/2024-11-10-protein-powder-analyzed/lead-vs-protein.png"
---

Disclaimer: The data used for analysis here is not owned by me. I have cited the source at the end.

Recently, I was looking for a protein supplement to buy. I’ve been using Nutrabox Whey Protein but wanted to try something new and see what’s currently available on the market.

For this, I used the OG “Protein Project” data shared by The Liver Doc on Twitter, which has since been documented in a paper [1].

On to the analysis. The first thing I wanted to check was the lead content of various protein powders. In his thread, The Doc cautioned about lead, saying it is harmful and that there is no safe limit for it; any amount can potentially cause serious damage. Naturally, I wanted to avoid those with lead content.

Another interesting aspect of the project was the labelling of protein content in these supplements and its accuracy. Some brands were found to have mislabeled the protein content present in their products.

To get a clearer view of these two parameters, let’s take a look at the plot for lead content vs protein percentage difference. The “protein percentage difference” is the difference in percentage points between the labelled protein percentage and the actual protein percentage.

![Lead vs Protein Content Scatterplot](/images/posts/2024-11-10-protein-powder-analyzed/lead-vs-protein.png)

Data Signals from the plot:

The scatterplot shows four major clusters. One with high lead content and highly mislabeled protein percentage (top right); and another with high lead content but low protein percentage differences (top left). The third cluster has lead content below 0.1 mg/kg and moderate to low protein percentage mismatch (bottom left - red). Lastly, there’s a fourth group with zero lead content but some degree of mismatch between actual and labelled protein content (bottom left - blue).

In the top right quadrant—protein supplements with high lead content and highly mislabeled protein percentages—all belong to the same company. I won’t be buying from them, ever.

Out of 36 supplements, 13 have high lead content and are somewhat mislabeled in terms of protein content. These should also be avoided.

Now, looking at the bottom left, there were nine that had relatively lower lead content, but some trace amounts were still present.

Only 12 were entirely clean in terms of lead content. My next protein supplement should be from one of them.

Shifting the focus to these 12 “clean” options, let’s look at how they fare in terms of percentage-point labelling accuracy:

![Protein Percentage Difference Comparison](/images/posts/2024-11-10-protein-powder-analyzed/protein-diff.png)

I really don’t know what’s happening with Muscletech. According to the data, the labelled protein content was around 66%, while the detected protein content was nearly 77%. Their protein powder also seemed a bit unique; it included some creatine. Then there’s British Biologicals, which showed a significant difference in labelled protein content.

My current protein powder is from Nutrabox, and I want something around the same price since it’s just a supplement for me, not my primary protein source—I mostly consume 200-300 grams of chicken every day.

Ultimate Nutrition seemed to fit the bill in terms of both price and quality, so I decided to go with it.

I had considered adding price as another dimension in this analysis. However, prices varied significantly across websites, even for the same brand, so I’ve set that aside for now and may revisit it later.

-----
[1] Philips CA, Theruvath AH, Ravindran R, Chopra P. Citizens protein project: A self-funded, transparent, and concerning report on analysis of popular protein supplements sold in the Indian market. Medicine (Baltimore). 2024 Apr 5;103(14):e37724. doi: 10.1097/MD.0000000000037724. PMID: 38579036; PMCID: PMC10994440.
