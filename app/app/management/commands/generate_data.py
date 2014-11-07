from app.models import PlayerDeath
from django.core.management.base import NoArgsCommand
import random

class Command(NoArgsCommand):
  help = "Creates 100 randomized, sample events for the map."
  
  def handle_noargs(self, **options):
    width = 280
    height = 70
    for x in range(0, 1000):
      event = PlayerDeath()
      event.player_id = random.randrange(1, 10)
      event.source_player_id = random.randrange(1, 10)
      event.weapon_id = random.randrange(1, 5)
      event.pos_x = (random.random() * width) - (width / 2)
      event.pos_y = (random.random() * height) - (height / 2) + 45
      event.save()
