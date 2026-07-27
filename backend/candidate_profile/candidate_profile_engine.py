from backend.candidate_profile.profile_builder import ProfileBuilder

from backend.candidate_profile.profile_validator import ProfileValidator


class CandidateProfileEngine:

    def __init__(self):

        self.builder = ProfileBuilder()

        self.validator = ProfileValidator()


    def build(

        self,

        experience,

        skills,

        education,

        projects,

        certifications

    ):

        profile = self.builder.build(

            experience,

            skills,

            education,

            projects,

            certifications

        )

        valid, invalid = self.validator.validate(

            profile

        )

        return {

            "candidate_profile": valid,

            "invalid_profile": invalid

        }