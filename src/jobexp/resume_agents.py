import os
import yaml
from crewai import Agent

class ResumeAgents:
    def __init__(self):
        path = os.path.join(os.path.dirname(__file__), 'config', 'agents.yaml')
        with open(path, 'r') as f:
            config = yaml.safe_load(f)

        self.experience_writer = Agent(**config['experience_writer'])
        self.experience_reviewer = Agent(**config['experience_reviewer'])

    def get_all(self):
        return self.experience_writer, self.experience_reviewer
