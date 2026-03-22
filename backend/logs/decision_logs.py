def log_decision(message):

    with open("decision.log", "a") as f:
        f.write(message + "\n")
