import toml
from urllib import request
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        kasitelty = toml.loads(content)
        poetry = kasitelty.get('tool').get('poetry')
        nimi = poetry.get('name')
        kuvaus = poetry.get('description')
        lisenssi = poetry.get('license')
        tekijat = poetry.get('authors')
        dependencies = list(poetry.get('dependencies'))
        devdep = list(poetry.get('group').get('dev').get('dependencies'))

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(nimi, kuvaus, lisenssi, tekijat, dependencies, devdep)
