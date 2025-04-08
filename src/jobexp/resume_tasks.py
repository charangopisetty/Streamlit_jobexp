from crewai import Task
import os
import yaml

class ResumeTasks:
    def __init__(self, writer_agent, reviewer_agent):
        path = os.path.join(os.path.dirname(__file__), 'config', 'tasks.yaml')
        with open(path, 'r') as f:
            config = yaml.safe_load(f)

        self.job_description_analysis = Task(
            agent=writer_agent,
            **config['job_description_analysis']
        )

        self.job_experience_review = Task(
            agent=reviewer_agent,
            **config['job_experience_review']
        )

    def get_all(self):
        return self.job_description_analysis, self.job_experience_review
