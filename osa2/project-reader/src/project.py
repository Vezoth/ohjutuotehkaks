class Project:
    def __init__(self, name, description, lisenssi, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = lisenssi
        self.dependencies = dependencies
        self.authors = authors
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        authors = listaa_osat(self.authors)
        dependencies = listaa_osat(self.dependencies)
        devdep = listaa_osat(self.dev_dependencies)

        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}"
            f"\n"
            f"\nAuthors: {authors}"
            f"\n"
            f"\nDependencies: {dependencies}"
            f"\n"
            f"\nDevelopment dependencies: {devdep}"
        )
    
def listaa_osat(lista):
    acc = ""
    for i in lista:
        acc += f"\n- {i}"
    if len(acc) == 0:
        return "\n -"
    return acc