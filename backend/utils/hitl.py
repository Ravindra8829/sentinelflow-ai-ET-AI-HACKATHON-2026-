def human_review(step, confidence):
    if confidence < 0.85:
        print("⚠️ Human review required for step:", step)
        return True
    return False
