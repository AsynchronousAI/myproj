from services import Players as plrs
from services import BadgeService as badges

BADGEID = 123456789

@plrs.PlayerAdded
def onPlayerAdded(player):
    badges:AwardBadge(player.UserId, BADGEID)