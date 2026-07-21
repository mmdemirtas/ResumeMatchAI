class RequirementExpander:

    def __init__(self):

        self.expansions = {

            "C#":
                "Experience developing backend applications using .NET framework.",

            "SQL":
                "Experience using SQL databases, writing queries and working with relational databases.",

            "Docker":
                "Experience building, deploying and maintaining containerized applications using Docker.",

            "Git":
                "Experience using Git version control for software development.",

            "Linux":
                "Experience working with Linux operating systems and command line tools.",

            "REST API":
                "Experience designing, developing or maintaining RESTful APIs.",

            "FastAPI":
                "Experience developing backend applications using FastAPI framework.",

            "Django":
                "Experience developing web applications using Django.",

            "Flask":
                "Experience developing backend applications using Flask framework.",

            "React":

            "Experience developing frontend applications using React.",

            "Next.js":
                "Experience developing server-side rendered applications using Next.js.",

            "Vue":
                "Experience developing frontend applications using Vue.",

            "Angular":
                "Experience developing applications using Angular.",

            "JavaScript":
                "Experience writing modern JavaScript.",

            "TypeScript":
                "Experience developing applications using TypeScript.",

            "HTML":
                "Experience building responsive web pages using HTML.",

            "CSS":
                "Experience styling web applications using CSS.",

            "Redux":
                "Experience managing application state using Redux.",

            "Tailwind CSS":
                "Experience building interfaces using Tailwind CSS.",

            "Bootstrap":
                "Experience using Bootstrap.",

            "REST API":
                "Experience integrating frontend applications with REST APIs.",

            "GraphQL":
                "Experience consuming GraphQL APIs.",

            "Git":
                "Experience using Git.",

            "Webpack":
                "Experience configuring Webpack.",

            "Vite":
                "Experience using Vite.",

            "Jest":
                "Experience writing frontend unit tests.",

            "Cypress":
                "Experience writing end-to-end tests."
        }

    def expand(self, requirement):

        return self.expansions.get(
            requirement,
            requirement
        )