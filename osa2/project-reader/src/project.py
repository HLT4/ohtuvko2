class Project:
    def __init__(self, tiedot):
        self.name = tiedot["name"]
        self.description = tiedot["description"]
        self.dependencies = list(tiedot["dependencies"].keys())
        self.dev_dependencies = list(tiedot["group"]["dev"]["dependencies"].keys())
        self.license = tiedot["license"]
        self.authors = tiedot["authors"]


    def _stringify_dependencies(self, dependencies):
        return "\n- ".join(dependencies) if len(dependencies) > 0 else "-"

    def _ranskalaiset_viivat(self, lista):
        tulos = ""
        for i in range(len(lista)):
            tulos += f"\n- {lista[i]}"
        return tulos

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license}\n"
            f"\nAuthors: {self._ranskalaiset_viivat(self.authors)}\n"
            f"\nDependencies: {self._stringify_dependencies(self.dependencies)}\n"
            f"\nDevelopment dependencies: {self._stringify_dependencies(self.dev_dependencies)}"
        )
