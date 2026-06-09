title: Pageinde-Open
---
Implemented a real open version of PageIndex RAG from scratch during the weekend, inspired by Tandava Appadoo's TS implementation obviously.

PageIndex is good but is focused on the SaaS platform. I implemented a version that is not ML-heavy. 

The idea is find the relevent section from docs then add it in context without chunking, using a tree-based approach. 

This is great to trace where the LLM took it's info from and works best where the PDF is well-strcutured, filled with useful content like in legal, finance etc

This is a version with minimal features, more on the ROADMAP.

pip install pageindex-open
