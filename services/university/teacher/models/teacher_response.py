from pydantic import BaseModel, Field, RootModel

from services.university.teacher.models.teacher_request import TeacherRequest


class TeacherResponse(TeacherRequest):
    id: int = Field(...)


class TeachersResponse(RootModel[list[TeacherResponse]]):
    def __iter__(self):
        return iter(self.root)

    def __getitem__(self, item):
        return self.root[item]
