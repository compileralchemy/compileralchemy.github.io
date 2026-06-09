title: RAG paper review: Dense Passage Retrieval for Open-Domain Question Answering (3/50)
---
The DPR paper predates RAG and gives nascent ideas about Vector databases.

This paper was a bit hard to read as there are no diagrams. I mean i spent sometimes drawing the diagram in my head. There were also steps that left me confused as to the actual implementation.

Dense means dense vectors, vectors consisting of non-zero elements.
Passage here means answers.

> the advances of reading comprehension models suggest a much simplified two-stage framework: (1) a context retriever first selects a small subset of passages where some of them contain the answer to the question, and then (2) a machine reader can thoroughly examine the retrieved contexts and identify the correct answer

Before, answering questions relied on keyword matching. This paper proposes a fine-tuning approach to create great vector embeddings using only pairs of q&as. "the embedding is optimized for maximizing inner products of the question and relevant passage vectors, with an objective comparing all pairs of questions and passages in a batch."

> With special in-memory data structures and indexing schemes, retrieval can be done efficiently using maximum inner product search (MIPS) algorithms 

> Assume that our collection contains D documents, d1, d2, · · · , dD. We first split each of the documents into text passages of equal lengths as the basic retrieval units3 and get M total passages in our corpus ..., where each passage pi can be viewed as a sequence of tokens ... . Given a question q, the task is to find a span ... from one of the passages ... that can answer the question. 

Basically, it cuts the documents into chunks and selects the answer from that.

> We focus our research ... on improving the retrieval component in open-domain QA. Given a collection of M text passages, the goal of our dense passage retriever (DPR) is to index all the passages in a low-dimensional and continuous space, such that it can retrieve efficiently the top k passages relevant to the input question for the reader at run-time.

> Our dense passage retriever (DPR) uses a dense encoder EP (·) which maps any text passage to a d dimensional real-valued vectors and builds an index for all the M passages that we will use for retrieval.

> At run-time, DPR applies a different encoder EQ(·) that maps the input question to a d-dimensional vector, and retrieves k passages of which vectors are the closest to the question vector. We define the similarity between the question and the passage using the dot product of their vectors

Each training sample has: question, answer and irrelevant words (negative). It's loss function maximizes the similarity score between the query and its positive passage while minimizing the score between the query and all the negative passages.

> We test these alternatives and find that L2 performs comparable to dot product, and both of them are superior to cosine

A very clear paper IMO.
