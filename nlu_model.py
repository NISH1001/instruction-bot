#!/usr/bin/env python3


import warnings

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=DeprecationWarning)

import argparse
import sys

from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer, Interpreter
from rasa_nlu import config

def train_nlu(data, config_json, model_dir):
    print("Training NLU model...")
    training_data = load_data(data)
    trainer = Trainer(config.load(config_json))
    trainer.train(training_data)
    model_directory = trainer.persist(model_dir, fixed_model_name = 'instruction_nlu')

def run_nlu(query):
    print("Running NLU model...")
    model_dir = "models/nlu/default/instruction_nlu"
    interpreter = Interpreter.load(model_dir)
    response = interpreter.parse(query)
    return response

def run():
    arg = sys.argv[1:]
    if not arg:
        raise ValueError("Please supply arguments like: --train or --run")
    if arg[0] == "--train":
        train_nlu('data/data2.json', 'config_spacy.json', 'models/nlu')
    elif arg[0] == "--run" and arg[1:]:
        query = arg[1:]
        response = run_nlu(' '.join(query))
        print(response)
    else:
        print("Invalid arguments...")


def main():
    run()

if __name__ == "__main__":
    main()

