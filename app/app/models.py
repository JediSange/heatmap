from mongoengine import *
import datetime

class PlayerDeath(Document):
  player_id = IntField(required=True, min_value=1)
  pos_x = DecimalField(required=True)
  pos_y = DecimalField(required=True)
  source_player_id = IntField(required=True, min_value=1)
  time = DateTimeField(required=True, default=datetime.datetime.now)
  weapon_id = IntField(required=True)
  