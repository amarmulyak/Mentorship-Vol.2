from src.the_cat_api.votes import Votes
from src.utils.utils import cfg


def test_get_vote():
    votes = Votes()
    r = votes.get_vote()
