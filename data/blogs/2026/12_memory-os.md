title: Memory Os
---
Coded an implementation of the paper "MemOS: A Memory OS for AI System". The screenshot is the accompanying dashboard showing the type of memory that gets autmatically added as a conversation progresses.

I published it as a library as some people squatted over the name memos on github and is pushing their memos cloud business. This is a free implementation focusing on the concepts.

The MemOS paper outlines how agentic memory should be, based on the human mind, introducing even policy access for memories.

Implementation-wise, i added Chroma, networkX and shamelessly borrowed the lane-based pattern to keep the code simple.

"""
we propose MemOS, a memory operating system that treats memory as a manageable system resource. It unifies the representation, scheduling, and evolution of plaintext, activation-based, and parameter-level memories, enabling cost-efficient storage and retrieval. As the basic unit, a MemCube encapsulates both memory content and metadata such as provenance and versioning. MemCubes can be composed, migrated, and fused over time, enabling flexible transitions between memory types and bridging retrieval with parameter-based learning. MemOS establishes a memory-centric system framework that brings controllability, plasticity, and evolvability to LLMs, laying the foundation for continual learning and personalized modeling.
"""

```
from angel_recall import MemOS

memos = MemOS(persist_directory="./my_vault")

memos.process("Remember that I prefer technical deep-dives.")

response = memos.process("How should you format the report for me?")
print(response["response"])
```

It's also available as a tool for agents.
