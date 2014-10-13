import pymuxinator.config as config
from pymuxinator.project import Project
from pymuxinator import exceptions, utils

class CLI(object):
    def start(self, project_name):
        project = None

        try:
            project = Project.from_name(project_name)
        except exceptions.ProjectNotFoundError:
            print u"Project `%s` does not exist" % project_name
        except exceptions.ConfigParseError as e:
            print u"Project `%s` config could not be parsed (%s)" % (project_name, e.message)
        except exceptions.NoWindowsError:
            print u"Project `%s` contains no windows. Please include some windows." % project_name
        except exceptions.NoNameError:
            print u"Project `%s` didn't specify a `project_name`." % project_name
        else:
            utils.execute_cmd(project.render())
