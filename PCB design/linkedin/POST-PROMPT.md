# Post-pack prompt · used for every LinkedIn topic

Topics come from `../MASTER-CHECKLIST.md`. Ask with `Post: <topic>`. The answer is saved to `posts/YYYY-MM-DD-<topic>.md`.

## The prompt (verbatim, given 15 Oct 2026)

```
Topic: <checklist topic>

Please give me a 2-part response:

1. THE LEARNING MODULE: Explain the core concepts of this topic in simple, practical terms.
   Include common mistakes engineers make in the layout/schematic, industry-standard values
   or rules of thumb, and how a testing/ATE background helps avoid errors here.

2. THE LINKEDIN POST GENERATOR: Write a professional, engaging, and readable LinkedIn post
   about this topic. Focus it on how proper implementation of this skill ensures design
   reliability, scalability, and seamless hardware validation. Include functional hardware
   hashtags and ideas for a visual to attach.
```

## Output rules (so the feed stays non-repetitive)

Part 2 must also pass the voice rules in `LINKEDIN-PLAN.md` §1:

- Opens with a moment or a number from **this week's work** (project, module, mock), not with the topic name.
- Contains at least one number and exactly one rule the reader can reuse.
- Anything not yet measured or not from your real experience is written as `[bracket]` for you to fill or delete. Never publish a bracket.
- 120–200 words, one visual, ≤ 5 functional hashtags, ends with a question.
- The format follows the calendar's rotation column (war story / decision / before-after / numbers / checklist / opinion).

Part 1 doubles as the week's 📱 Tuesday reading.
