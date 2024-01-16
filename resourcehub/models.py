from resourcehub import db


class User(db.Model):
    # schema for the User model
    id = db.column(db.Integer, primary_key=True)
    username = db.column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    resources = db.relationship("Resource", backref="user", cascade="all, delete", lazy=True)
    comments = db.relationship("Comment", backref="user", cascade="all, delete", lazy=True)

    def __repr__(self):
        return f"#{self.id}, Username: {self.username}, Email: {self.email}"


class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    resource_name = db.Column(db.String(50), unique=True, nullable=False)
    resource_description = db.Column(db.Text, nullable=False)
    url = 
    date_created = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        return self 


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    resource_id = db.Column(db.Integer, db.ForeignKey("resource.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        return self.text


class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name



class AgeRange(db.model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.String(10), unique=True, nullable=False)

    def __repr__(self):
        return self.age


# Resource and Subject many-to-many relationship
class ResourceSubject(db.Model):
    resource_id = db.Column(db.Integer, db.ForeignKey("resource.id"), primary_key=True)
    subject_id = db.Column(db.Integer, db.ForeignKey("subject.id"), primary_key=True)


# Resource and AgeRange many-to-many relationship
class ResourceAgeRange(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    resource_id = db.Column(db.Integer, db.ForeignKey("resource.id"))
    age_range_id = db.Column(db.Integer, db.ForeignKey("age_range.id"))


# Subject and AgeRange many-to-many relationship
class SubjectAgeRange(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(db.Integer, db.ForeignKey("subject.id"))
    age_range_id = db.Column(db.Integer, db.ForeignKey("age_range.id"))
