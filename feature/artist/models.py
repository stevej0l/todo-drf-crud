from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    # ---------- DB LOGIC ----------

    @classmethod
    def create_artist(cls, data):
        return cls.objects.create(**data.__dict__)

    @classmethod
    def update_artist(cls, artist_id, data):
        cls.objects.filter(id=artist_id).update(**data.__dict__)
        return cls.objects.get(id=artist_id)

    @classmethod
    def delete_artist(cls, artist_id):
        cls.objects.filter(id=artist_id).delete()
