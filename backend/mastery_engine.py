import numpy as np
def compute_mastery(data):
    if not data:
        return 0, {}
    concept_scores = {}
    for concept, correct, _ in data:
        if concept not in concept_scores:
            concept_scores[concept] = []
        concept_scores[concept].append(correct)
    overall = np.mean([c for _, c, _ in data]) * 100
    concept_mastery = {
        concept: round(np.mean(scores) * 100, 2)
        for concept, scores in concept_scores.items()
    }
    return round(overall, 2), concept_mastery
