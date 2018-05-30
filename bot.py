#!/usr/bin/env python3


import warnings

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=DeprecationWarning)

from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.policies.memoization import MemoizationPolicy

def run(serve_forever=True):
    interpreter = RasaNLUInterpreter("models/nlu/default/instruction_nlu")
    agent = Agent.load("models/dialogue", interpreter=interpreter)
    if serve_forever:
        agent.handle_channel(ConsoleInputChannel())
    return agent


def main():
    run()

if __name__ == "__main__":
    main()

