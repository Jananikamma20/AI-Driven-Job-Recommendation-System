from backend.skill_engine.skill_engine import SkillEngine
from backend.matching_engine.matcher import ResumeJobMatcher
from backend.skill_gap_engine.skill_gap_engine import SkillGapEngine
from backend.course_engine.course_engine import CourseEngine
from backend.ats_engine.ats_engine import ATSEngine
from backend.project_engine.project_engine import ProjectEngine
from backend.experience_engine.experience_engine import ExperienceEngine
from backend.education_engine.education_engine import EducationEngine
from backend.certification_engine.certification_engine import CertificationEngine


class RecommendationEngine:

    def __init__(self):

        self.skill_engine = SkillEngine()

        self.matcher = ResumeJobMatcher()

        self.skill_gap_engine = SkillGapEngine()

        self.course_engine = CourseEngine()

        self.ats_engine = ATSEngine()

        self.project_engine = ProjectEngine()

        self.experience_engine = ExperienceEngine()

        self.education_engine = EducationEngine()

        self.certification_engine = CertificationEngine()

    # ---------------------------------
    # Complete Resume Analysis
    # ---------------------------------

    def analyze(

            self,

            resume,

            job

    ):

        # Skill Analysis

        skill_analysis = self.skill_engine.analyze(

            resume,

            job

        )

        # Resume-Job Matching

        matching = self.matcher.match(

            resume,

            job

        )

        # Skill Gap

        skill_gap = self.skill_gap_engine.analyze_skill_gap(

            matching

        )

        # Course Recommendation

        recommended_courses = self.course_engine.recommend_courses(

            skill_gap["missing_skills"]

        )

        # ATS Analysis

        ats = self.ats_engine.calculate_ats_score(

            resume,

            job

        )

        # Experience Analysis

        experience = self.experience_engine.analyze(

            resume,

            job

        )

        # Education Analysis

        education = self.education_engine.analyze(

            resume,

            job

        )

        # Certification Analysis

        certification = self.certification_engine.analyze(

            resume,

            job

        )

        # Project Analysis

        projects = self.project_engine.match_projects(

            resume.get(

                "projects",

                []

            ),

            job.get(

                "description",

                ""

            )

        )

        return {

            "skill_analysis": skill_analysis,

            "matching": matching,

            "skill_gap": skill_gap,

            "recommended_courses": recommended_courses,

            "ats": ats,

            "experience": experience,

            "education": education,

            "certification": certification,

            "projects": projects

        }