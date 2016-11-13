# from app import db
#
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     nickname = db.Column(db.String(64), index=True, unique=True)
#     email = db.Column(db.String(120), index=True, unique=True)
#     posts = db.relationship('Post', backref='author', lazy='dynamic')
#
#     def __repr__(self):
#         return '<User %r>' % (self.nickname)
#
# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     title = db.Column(db.string)
#     body = db.Column(db.String(140))
#     timestamp = db.Column(db.DateTime)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#
#     def __repr__(self):
#         return '<Post %r>' % (self.body)
#
#
# class Entry(db.Model):
#     title = CharField()
#     slug = CharField(unique=True)
#     content = TextField()
#     published = BooleanField(index=True)
#     timestamp = DateTimeField(default=datetime.datetime.now, index=True)
#
#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = re.sub('[^\w]+', '-', self.title.lower())
#         ret = super(Entry, self).save(*args, **kwargs)
#
#         # Store search content.
#         self.update_search_index()
#         return ret
#
#     def update_search_index(self):
#         try:
#             fts_entry = FTSEntry.get(FTSEntry.entry_id == self.id)
#         except FTSEntry.DoesNotExist:
#             fts_entry = FTSEntry(entry_id=self.id)
#             force_insert = True
#         else:
#             force_insert = False
#         fts_entry.content = '\n'.join((self.title, self.content))
#         fts_entry.save(force_insert=force_insert)
#
#
# class FTSEntry(FTSModel):
#     entry_id = IntegerField()
#     content = TextField()
#
#     class Meta:
#         database = database