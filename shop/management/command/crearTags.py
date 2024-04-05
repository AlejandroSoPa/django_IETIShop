from faker import Faker
from faker_music import MusicProvider
fake = Faker()
fake.add_provider(MusicProvider)

class Comando(BaseCommand):
    help = 'Crea tags'

    def handle(self, *args, **kwargs):
        for _ in range(10):
            Tag.objects.create(nom=fake.music_genre())
        self.stdout.write(self.style.SUCCESS('Tags creados'))