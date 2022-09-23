from nbgrader.plugins.zipcollect import FileNameCollectorPlugin
from nbgrader.apps import NbGraderAPI
import os.path
import datetime



class Moodle(FileNameCollectorPlugin):
    def __init__(self, **kargs):
        super().__init__(**kargs)
        api  = NbGraderAPI()
        self.students = {}
        for st in api.get_students():
            name = f'{st["first_name"]} {st["last_name"]}'
            if name in self.students:
                raise Exception(f"Duplicated name:{name}:{self.students}")
            self.students[name] = st['id']
        self.log.debug("Estudiantes cargads")

    def collect(self, submmited_file):
        path, filename = os.path.split(submmited_file)
        filename, ext = os.path.splitext(filename)

        if ".ipynb_checkpoints" in path:
            self.log.info(f"Skipping .ipnbb_checkpints {submmited_file}")
            return None

        if "__MACOSX" in path:
            self.log.info(f"Skipping __MACOSX {submmited_file}")
            return None

        if ".DS_Store" in filename:
            self.log.info(f"Skipping .DS_Store {submmited_file}")
            return None

        if filename[-4:] == "json":
            self.log.info(f"Skipping .json file {submmited_file}")
            return None

        if ext not in self.valid_ext:
            self.log.debug(f'Invalid extension {submmited_file} {ext}')
            return None

        for name, username in self.students.items():
            if name in path:
                return {
                    'file_id': filename,
                    'student_id': username
                }
            self.log.error(f'user not found {submmited_file}')
        return None
        # super().collect(submmited_file)
