def handle_failure(step, error):

    print(f"Failure detected in step: {step}")
    print(f"Error: {error}")

    print("Retrying...")

    return {"action": "retry"}
