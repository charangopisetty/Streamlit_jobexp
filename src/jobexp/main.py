#!/usr/bin/env python
import sys
import warnings
import os

from datetime import datetime
from jobexp.crew import Jobexp

from crewai.agents.agent_builder.base_agent_executor_mixin import CrewAgentExecutorMixin
import time

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'job_description': 'You are a experieneced java developer with 5 years of experience in the field. You have worked on various projects and have a strong understanding of Java programming language.',
    }
    Jobexp().crew().kickoff(inputs=inputs)