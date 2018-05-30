#!/usr/bin/env python3


from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy


def train_dialogue(domain_file="instruction_domain.yml",
                   model_path="models/dialogue",
                   training_data_file="data/stories.md"):
    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(max_history=3),
                            KerasPolicy()])

    # training_data = agent.load_data(training_data_file)
    agent.train(
            training_data_file,
            epochs=500,
            batch_size=25,
            validation_split=0.2
    )

    agent.persist(model_path)
    return agent


def main():
    train_dialogue()

if __name__ == "__main__":
    main()

