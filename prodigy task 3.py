import random

def build_markov_chain(text, n=2):
    """Builds an n-gram Markov chain from the given text."""
    words = text.split()
    markov_chain = {}

    for i in range(len(words) - n):
        key = tuple(words[i:i+n])
        next_word = words[i+n]
        if key not in markov_chain:
            markov_chain[key] = []
        markov_chain[key].append(next_word)

    return markov_chain

def generate_text(chain, length=50, n=2):
    """Generates text of given length using the Markov chain."""
    start = random.choice(list(chain.keys()))
    result = list(start)

    for _ in range(length - n):
        state = tuple(result[-n:])
        next_words = chain.get(state)
        if not next_words:
            break
        next_word = random.choice(next_words)
        result.append(next_word)

    return ' '.join(result)

if __name__ == "__main__":
    # Sample input text
    sample_text = """
    Prodigy Infotech provides hands-on AI training through innovative tasks.
    Learn machine learning, data science, and deep learning by working on real-world problems.
    Text generation using Markov chains is a powerful tool for statistical modeling.
    """

    n = 2  # bigram
    markov_chain = build_markov_chain(sample_text, n)
    generated = generate_text(markov_chain, length=50, n=n)

    print("📝 Generated Text:")
    print(generated)
