title: Review of retrieval-augmented generation for knowledge-intensive NLP tasks
---
I have been reading RAG papers since sometimes. This one was the first paper. Will be posting my observations and hope it will inspire you to dive into RAG. I am aiming to read 50 papers on the topic.

This first RAG paper attempts to bring external memory to seq2seq models to get more accurate answers.

> Finally, we demonstrate that the non-parametric memory can be replaced to update the models’ knowledge as the world changes.

This is a powerful line in the intro. Until now RAG is used to provide real-time updates. Parametric memory is used to denote models where info is stored in the model's parameters (weights and biases). This is used in the paper to reason and write, not to store factual infos.

Non-parametric memory is the contrary. It refers to what we call nowadays vector databases.

>  Each Wikipedia article is split into disjoint 100-word chunks, to make a total of 21M documents. We use the document encoder to compute an embedding for each document, and build a single MIPS index using FAISS [23] with a Hierarchical Navigable Small World approximation for fast retrieval [37]. During training, we retrieve the top k documents for each query

Essentially this sounds like how chromadb works under the hood. 

> We explore RAG models, which use the input sequence x to retrieve text documents z and use them as additional context when generating the target sequence y.

It is to be noted that much of the paper does not make any sense if ever like me, you started using RAG with powerful models like GPT3. For example the end-to-end training part where a BART model is trained to prioritize the non-parametric memory over it's internal knowledge is no longer necessary and we can just tune the prompt to focus on what we need. Or we don't need RAG-token to combine facts.

Marginalization is used in maths to find propability where a hidden factor / latent variable is present. Since z is the latent variable here, this fits naturally. Beam search allows you to find the highest probability and highest-quality (best) next words.

I'd say it's a very clever paper that invented great methods to work around hurdles by using commonly-available, primitive models of the day.
