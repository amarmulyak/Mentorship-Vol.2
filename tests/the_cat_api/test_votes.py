from src.the_cat_api.votes import Votes


def test_get_vote(cfg):
    votes = Votes(f"{cfg.the_cat_api}/votes")
    r = votes.get_vote()
