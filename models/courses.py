from tortoise import fields, models 
from tortoise.contrib.pydantic import pydantic_model_creator

from .base import BaseModel


# class Course(BaseModel):
#     name = fields.CharField(max_length=100, required=True)


# class CourseChapter(BaseModel):
#     course = fields.ForeignKeyField('models.courses.Course', related_name="CourseChapter")
    
