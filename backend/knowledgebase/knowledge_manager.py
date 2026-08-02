from backend.knowledgebase.skills_loader import SkillsLoader
from backend.knowledgebase.education_loader import EducationLoader
from backend.knowledgebase.certification_loader import CertificationLoader
from backend.knowledgebase.course_loader import CourseLoader
from backend.knowledgebase.company_loader import CompanyLoader
from backend.knowledgebase.designation_loader import DesignationLoader
from backend.knowledgebase.technology_loader import TechnologyLoader
from backend.knowledgebase.soft_skill_loader import SoftSkillLoader
from backend.knowledgebase.domain_loader import DomainLoader
from backend.knowledgebase.job_loader import JobLoader


class KnowledgeManager:

    def __init__(self):

        self.skills = SkillsLoader().load()

        self.education = EducationLoader().load()

        self.certifications = CertificationLoader().load()

        self.courses = CourseLoader().load()

        self.companies = CompanyLoader().load()

        self.designations = DesignationLoader().load()

        self.technologies = TechnologyLoader().load()

        self.soft_skills = SoftSkillLoader().load()

        self.domains = DomainLoader().load()

        self.jobs = JobLoader().load()