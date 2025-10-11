---
title: "LinearLeap: Towards More Intelligent Machine Learning Tools"
date: 2025-05-21
tags: [["data-science"]]
---

Upload data, run regression, get recommendations - powered by LLMs and built with analysts in mind.

LLMs are doing a fantastic job in automating repetitive and mundane day-to-day tasks. However, where they can truly add value is in performing "intelligent" tasks.

With this in mind, I started exploring how I could create "intelligent" ML models. When I say intelligent, I mean models that can provide crisp, actionable recommendations to analysts and stakeholders - not just [stir through piles of data](https://www.explainxkcd.com/wiki/index.php/1838:_Machine_Learning), try 10 different models, and then say "here's everything, select whatever you like."

To address this need, I developed an intelligent Linear Regression assistant. It's currently hosted on Streamlit Cloud and accessible via this link: [LinearLeap](https://linearleap.streamlit.app)

This web application leverages multimodal LLMs (currently configured to use Gemini). While I'm using a free API for demonstration purposes, users can enter their own API keys to use the tool as extensively as they wish.

The Multiple Linear Regression model is still a work in progress, which I plan to enhance later. Nevertheless, I'm moderately satisfied with the Linear Regression tool's current capabilities.

If you're an analyst, data scientist, or stakeholder with some ML knowledge, I invite you to try it out and share your feedback. Your input will be valuable as I continue to improve the application.

## Features

- Upload and analyze your datasets with ease
- Perform linear and multilinear regression analysis
- Visualize relationships between variables
- Get detailed statistical insights and predictions
- Receive tailored recommendations based on your data (GenAI generated)

## Resources

**GitHub repository:**  
[LinearLeap - Github](https://github.com/shibaprasadb/linear-leap)

**Demo video:**
<iframe width="560" height="315" src="https://www.youtube.com/embed/d78AHXw-7TI?start=4" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
(Please excuse my presentation - recording yourself is a humbling experience!!)

## Future enhancements planned

- Fully integrating Multiple Linear Regression
- Better support for categorical variables
- Enhanced visualizations and export options
- More robust handling of multicollinearity
- Even smarter GenAI-generated recommendations