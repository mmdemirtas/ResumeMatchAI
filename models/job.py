class Job:

    def __init__(self):

        # General Information
        self.file_name = ""
        self.title = ""
        self.text = ""
        self.sections = {}

        # Requirements
        self.required_skills = []
        self.preferred_skills = []

        self.required_education = ""
        self.required_experience = ""

        # Optional Requirements
        self.required_languages = []
        self.required_certifications = []

        # Responsibilities
        self.responsibilities = []

        # Nice to Have
        self.nice_to_have = []

        # Other
        self.location = ""
        self.employment_type = ""
        self.salary = ""