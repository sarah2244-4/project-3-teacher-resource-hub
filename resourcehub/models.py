from resourcehub import db
from flask_login import UserMixin
from datetime import datetime
from enum import Enum


class User(db.Model, UserMixin):
    """ Schema for the User Model """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    resources = db.relationship("Resource", backref="user", cascade="all, delete", lazy=True)
    comments = db.relationship("Comment", backref="user", cascade="all, delete", lazy=True)

    def __repr__(self):
        return f"#{self.id}, Username: {self.username}, Email: {self.email}"


class Resource(db.Model):
    """ Schema for the Resource Model """
    id = db.Column(db.Integer, primary_key=True)
    resource_name = db.Column(db.String(50), unique=True, nullable=False)
    resource_description = db.Column(db.Text, nullable=False)
    url = db.Column(db.String(250), nullable=False)
    date_created = db.Column(db.DateTime(), default=datetime.utcnow, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    comments = db.relationship("Comment", backref="resource", cascade="all, delete", lazy=True)

    def __repr__(self):
        return f"#{self.id}, name: {self.resource_name}"


class Comment(db.Model):
    """ Schema for the Comment Model """
    id = db.Column(db.Integer, primary_key=True)
    comment_text = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime(), default=datetime.utcnow, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    resource_id = db.Column(db.Integer, db.ForeignKey("resource.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        return self.comment_text


class SubjectEnum(Enum):
    BIOLOGY = "Biology"
    CHEMISTRY = "Chemistry"
    PHYSICS = "Physics"


class Subject(db.Model):
    """ Schema for the Subject Model """
    id = db.Column(db.Integer, primary_key=True)
    subject_name = db.Column(db.Enum(SubjectEnum), unique=True, nullable=False)

    def __repr__(self):
        return self.subject_name


class EducationLevelEnum(Enum):
    """ Enum for the Education levels """
    KS3 = "KS3"
    GCSE = "GCSE"
    ASLEVEL = "AS-Level"
    ALEVEL = "A-Level"


class EducationLevel(db.Model):
    """ Schema for the Education Level Model """
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.Enum(EducationLevelEnum), nullable=False)

    def __repr__(self):
        return self.level


class ResourceSubject(db.Model):
    """ Schema for the Resource and Subject many-to-many relationship """
    resource_id = db.Column(db.Integer, db.ForeignKey("resource.id"), primary_key=True)
    subject_id = db.Column(db.Integer, db.ForeignKey("subject.id"), primary_key=True)


class ResourceEducationLevel(db.Model):
    """ Schema for the Resource and EducationLevel many-to-many relationship """
    id = db.Column(db.Integer, primary_key=True)
    resource_id = db.Column(db.Integer, db.ForeignKey("resource.id"))
    education_level_id = db.Column(db.Integer, db.ForeignKey("education_level.id"))


class SubjectEducationLevel(db.Model):
    """ Schema for the Subject and EducationLevel many-to-many relationship """
    id = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(db.Integer, db.ForeignKey("subject.id"))
    education_level_id = db.Column(db.Integer, db.ForeignKey("education_level.id"))
