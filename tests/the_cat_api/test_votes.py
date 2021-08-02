from http import HTTPStatus

from src.the_cat_api.votes import Votes
from src.utils.api import parse_response
from src.utils.utils import cfg
from src.the_cat_api.images import Images
from src.the_cat_api.vote_params_data import VoteValueParam


def test_get_vote_response_code():
    votes = Votes(cfg().the_cat_api.url, cfg().the_cat_api.x_api_key)
    response = votes.get_votes()

    assert response.status_code == HTTPStatus.OK


def test_get_vote_limit():
    # todo: create required number of votes

    limit = 5
    votes = Votes(cfg().the_cat_api.url, cfg().the_cat_api.x_api_key)
    response = votes.get_votes(limit=limit)
    parsed_response = parse_response(response)

    assert len(parsed_response) == limit


def test_create_vote():
    images = Images(cfg().the_cat_api.url, cfg().the_cat_api.x_api_key)
    votes = Votes(cfg().the_cat_api.url, cfg().the_cat_api.x_api_key)

    image_id = images.get_random_image_id()
    vote = votes.create_vote('asf2', VoteValueParam.VALUE_UP)

    assert vote.status_code == HTTPStatus.OK

