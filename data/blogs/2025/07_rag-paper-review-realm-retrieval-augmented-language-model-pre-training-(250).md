title: RAG paper review: REALM: Retrieval-Augmented Language Model Pre-Training (2/50)
---
This is the paper preceding the RAG paper. It is the paper RAG based itself on and modified some parts.

I very much like the intro where it clearly states the problem with relying on models for adding more knowledge. As we know training is expensive, so we need another way to add infos on the fly. It expands on the problem more than the RAG paper.

One very important thing to keep in mind is that the purpose of the paper is to answer a question or fill in the blank using the external memory. It has a retriever model (transformer-based) that finds the most relevant document and an encoder model that takes the query and the documents to make predictions.

> The retriever is defined using a dense inner product model: ..., where Embedinput and Embeddoc are embedding functions that map x and z respectively to d-dimensional vectors. The relevance score f(x, z) between x and z is defined as the inner product of the vector embeddings. The retrieval distribution is the softmax over all relevance scores.

> We implement the embedding functions using BERT-style Transformers ... As in Devlin et al. (2018), we pass this into a Transformer, which produces one vector for each token, including the vector corresponding to [CLS] ... Finally, we perform a linear projection to reduce the dimensionality of the vector, denoted as a projection matrix W: Embedinput(x) = WinputBERTCLS(joinBERT(x)) Embeddoc(z) = WdocBERTCLS(joinBERT(ztitle, zbody)) where ztitle is the document’s title and zbody is its body. We let θ denote all parameters associated with the retriever, which include the Transformer and projection matrices.

The paper uses Marginal Likelihood Maximization to achieve two things:

1. It trains the model to assign a higher probability to the correct output by encouraging the retriever to find useful documents. It's designed to reward the retriever for finding what improves predictions

2. It mathematically transforms the step of retrieving documents into a value that does not breaks gradient-based optimizations like backpropagation.

Since for each training step we backpropagate, if we have a million document, it becomes a lot. So, the paper only considers the feedback from the most relevant documents (top k documents). Now to find the top k documents, it uses Maximum Inner Product Search (MIPS). 

The retriever model is used to create embeddings and the index to search documents are created from the embeddings. The index is used to search documents quickly. Since the models gets trained better, it creates better embedding and the index must be updated. The paper implements methods to update the index to keep it always fresh.

Another very clever paper!
