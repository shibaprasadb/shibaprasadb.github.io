Title: Notes on Vibe Coding
Date: 2025-09-05
Category: Blog
Tags: technical


I have been using LLMs (Claude and ChatGPT) for coding a lot, especially for my secondary languages (like Python).

I am fairly comfortable using them as a co-pilot: I design everything, solve smaller tasks with them, and then patch everything together.

Over the weekend, I did some vibe-coding, coupled with my old style of using LLMs, to create my professional website. I had tried doing something like this long back, but my lack of knowledge in HTML/CSS was holding me back. So I had a very basic WordPress page. Thanks to LLMs, I could easily create my website.

Here are some notes and observations:

<h3>Importance of software engineering</h3>

I am not a software engineer in any shape or form. I just have a basic understanding because of my work, and that proved to be quite crucial in this whole exercise. The biggest hurdle I found while doing vibe-coding was that the code wasn’t modular enough most of the time. I had to give constant nudges like this:

[![Don't just vibe code.](/images/posts/2025-09-05-notes-vibecoding/vibe_nudge.png)](/images/posts/2025-09-05-notes-vibecoding/vibe_nudge.png)


And once prompted, it did a good job of modifying.

<h3>Smaller chunks, small tasks</h3>

Be it vibe-coding or simple prompting, I never try to do multiple things in one go. I break down the bigger task into smaller buckets, then ask the LLM to perform those smaller tasks. In that way, things don’t break. It is also quite easy to write prompts, and the room for ambiguity reduces to a huge extent.

<h3>Commit frequently</h3>

I don’t know if I have some kind of insecurity about it, or if it is just a generally good practice. Whenever I am building anything with the help of LLMs, I commit my code changes very frequently. That way, I don’t have to worry about ‘losing’ anything. Even if a new update is badly designed, I can just ignore it and stay with my older one.

<h3>Start over</h3>

It is not a very common thing, but it has happened to me when the output produced was quite subpar (both in vibe-coding and in general prompting). The model will often just not get it at all! The best thing at that point is to start over. If the project is small, you can just upload the files directly in a new chat. Or in the previous chat, just ask for a detailed documentation of what you have done, then paste it in a new chat, and start again.  

If you have too many files, then probably something like Cursor or Codex might help more.


These have been my observations and experience so far. I’ll be experimenting more and plan to update this in 2–3 months. Curious to know: how has your experience been when coding with LLMs?
