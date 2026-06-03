"""
Create the initial commentary markdown file by copying the clean markdown
and inserting commentary markers at key sections.
"""
import re

INPUT = "data/annotated-transformer/annotated-transformer.md"
OUTPUT = "data/annotated-transformer/commentary.md"

# Commentary snippets keyed by line pattern (first line of section)
COMMENTARIES = {
    "# Background": """
> **Commentary:**
> The key insight here is that before the Transformer, 
> sequence-to-sequence models were either RNN-based (processing tokens sequentially, 
> which is slow) or CNN-based (processing in parallel but struggling with long-range 
> dependencies). The Transformer's radical idea: use only attention mechanisms, 
> no recurrence, no convolution. This cuts the path length between any two positions 
> to a constant O(1) -- a huge theoretical advantage.
""",

    "# Model Architecture": """
> **Commentary:**
> The encoder-decoder architecture was the dominant paradigm for sequence transduction 
> at the time. The encoder reads the input sequence and produces a continuous 
> representation, which the decoder then consumes to generate output. The key 
> innovation in the Transformer is how both encoder and decoder are built entirely 
> from attention mechanisms.
""",

    "### Attention": """
> **Commentary:**
> Attention is the core mechanism. The formula \\( \\text{Attention}(Q, K, V) = \\text{softmax}(QK^T / \\sqrt{d_k})V \\) 
> is worth understanding deeply. Queries, Keys, Values come from the same source in self-attention. 
> The dot product QK^T measures similarity between each query and all keys. Scaling by \\(\\sqrt{d_k}\\) 
> prevents the softmax from saturating (having extremely small gradients) when dimensions are large.
""",

    "Multi-head attention allows the model to jointly attend to": """
> **Deep Dive:**
> The intuition behind multi-head attention: instead of one attention computation, 
> we project the same input into \\(h\\) different representation subspaces (8 in the paper). 
> Each head can learn different types of relationships -- syntactic, semantic, positional. 
> Think of it as having 8 different "perspectives" on the same input simultaneously.
> 
> The total computation is similar to single-head attention because each head works 
> in a reduced dimension (\\(d_k = d_{\\text{model}} / h = 64\\)).
""",

    "## Position-wise Feed-Forward Networks": """
> **Commentary:**
> While attention handles interaction between positions, the FFN processes each position 
> independently. The two linear layers with ReLU in between add non-linearity and 
> transform the representation. The inner dimension \\(d_{ff} = 2048\\) is 4x the model dimension, 
> giving the network more capacity.
""",

    "## Positional Encoding": """
> **Commentary:**
> Since the Transformer has no recurrence or convolution, it has no inherent notion 
> of position. Positional encodings inject this information. The choice of sinusoids 
> is deliberate: for any fixed offset \\(k\\), \\(PE_{pos+k}\\) can be expressed as a linear function 
> of \\(PE_{pos}\\), which makes it easy for the model to learn relative positions. 
> The frequencies form a geometric progression, giving a unique encoding for each position.
""",

    "## Optimizer": """
> **Commentary:**
> The learning rate schedule is critical. It increases linearly for \\(\\text{warmup}_\\text{steps} = 4000\\), 
> then decreases proportionally to the inverse square root of the step number. This 
> warmup phase is essential for stable training of Transformers -- without it, the 
> large initial gradients can cause the model to diverge.
""",

    "### Label Smoothing": """
> **Commentary:**
> Label smoothing replaces hard 0/1 targets with soft targets (e.g., 0.9 for correct class, 
> \\(0.1/|V|\\) for others). This prevents the model from becoming over-confident and improves 
> generalization. The KL divergence loss is used instead of cross-entropy. While it hurts 
> perplexity (the model is less "certain"), it consistently improves BLEU score.
""",

    "# Part 3: A Real World Example": """
> **Commentary:**
> This section shows the full pipeline: loading real data (Multi30k German-English), 
> building vocabularies, creating efficient batch iterators, and training with 
> multi-GPU support. The batching strategy is important -- uneven padding wastes 
> computation, so they search over enough sentences to find tight batches.
""",

}


def main():
    with open(INPUT, "r", encoding="utf-8") as f:
        text = f.read()

    lines = text.split("\n")
    out_lines = []
    inserted = set()

    for line in lines:
        out_lines.append(line)
        stripped = line.rstrip('\n')
        for key in COMMENTARIES:
            if key not in inserted and stripped == key:
                out_lines.append(COMMENTARIES[key].strip())
                inserted.add(key)
                break

    result = "\n".join(out_lines)

    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write(result)

    print(f"Written {OUTPUT} with {len(inserted)} commentary sections")
    print(f"  Total lines: {len(result.splitlines())}")


if __name__ == "__main__":
    main()
