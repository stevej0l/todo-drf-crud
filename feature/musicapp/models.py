from django.db import models
from feature.artist.models import Artist


class Music(models.Model):
    title = models.CharField(max_length=200)
    duration = models.IntegerField()  # seconds
    release_date = models.DateField()

    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,
        related_name="songs"
    )

    def __str__(self):
        return self.title

    # ---------- DB LOGIC ----------

    @classmethod
    def create_song(cls, data):
        return cls.objects.create(
            title=data.title,
            duration=data.duration,
            release_date=data.release_date,
            artist_id=data.artist_id
        )

    @classmethod
    def update_song(cls, song_id, data):
        cls.objects.filter(id=song_id).update(
            title=data.title,
            duration=data.duration,
            release_date=data.release_date,
            artist_id=data.artist_id
        )
        return cls.objects.get(id=song_id)

    @classmethod
    def delete_song(cls, song_id):
        cls.objects.filter(id=song_id).delete()
