from crewai import Crew, Process
from dotenv import load_dotenv
from resume_agents import ResumeAgents
from resume_tasks import ResumeTasks

load_dotenv()

# Load agents
agents = ResumeAgents()
writer, reviewer = agents.get_all()

# Load tasks with agents
tasks = ResumeTasks(writer, reviewer)
analysis_task, review_task = tasks.get_all()

# Build crew
crew = Crew(
    agents=[writer, reviewer],
    tasks=[analysis_task, review_task],
    process=Process.sequential,
    verbose=True
)

def run():
    inputs = {
        'job_description': """​This role focuses on the design, development, and implementation of information technology (IT) solutions in order to meet the organization's needs through new and existing applications, systems architecture, network systems and applications infrastructure and the management of the IT infrastructure
In addition, this role focuses on performing the following Analytics related duties: Performs complex data research and analysis to support business operations, creates data mining architectures/models/protocols, statistical reporting, and data analysis methodologies to identify trends in large data sets, researches and applies knowledge of existing and emerging data science principles, theories, and techniques to inform business decisions, and may conduct scientific research projects with the goal of breaking new ground in data analytics
A professional individual contributor role that may direct the work of other lower level professionals or manage processes and programs
The majority of time is spent overseeing the design, implementation or delivery of processes, programs and policies using specialized knowledge and skills typically acquired through advanced education
An experienced level role that applies practical knowledge of job area typically obtained through advanced education and work experience
Works independently with general supervision, problems faced are difficult but typically not complex, and may influence others within the job area through explanation of facts, policies and practices
This position is responsible for providing oversight of the production cycle and ensuring that data loading, report production, and distribution meet the defined Service Level Agreements (SLAs) for the department
Works with the contracting department and payors to define, monitor, and enforce SLAs between TMIN and the payors for data acquisition and report production
Other duties and responsibilities may be assigned
Supports the development, productionization, and distribution of data and reports to internal and external customers, supporting contract performance and strategic initiatives
Works with the data architecture team to ensure the data models support the reporting needs of the business, and provides business and/or technical requirements as necessary for any architectural change requests
Communicates the schedule of reporting requirements to the responsible parties and the broader TMIN organization when required
Triages new reporting requests to determine priority and proper solution, and communicates this back to requestor(s)
Supports central repository of technical report development documentation (technical designs)
Creates the long-term vision and strategy for the Production Management team
Prioritizes reporting requests and strategic determination of optimal solution (new report required vs. leveraging and enhancing existing report)
Develops SQL queries to solve intricate reporting needs of the business
Maintains collaborative, team relationships with peers and colleagues in order to effectively contribute to the working group’s achievement of goals, and to help foster a positive work environment"""
    }
    result = crew.kickoff(inputs=inputs)
    print(result.raw)

if __name__ == "__main__":
    run()

