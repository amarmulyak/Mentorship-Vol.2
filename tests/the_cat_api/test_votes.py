import pytest

from src.the_cat_api.votes import Votes
from src.utils.utils import cfg
from src.the_cat_api.images import Images
from src.the_cat_api.vote_params_data import VoteValueParam
from http import HTTPStatus


def test_get_vote_limit():
    limit = 5
    votes = Votes(cfg().the_cat_api.url, cfg().the_cat_api.x_api_key)
    response = votes.get_votes(limit=limit)

    assert len(response.response_json()) == limit


def test_create_vote_response():
    images = Images(cfg().the_cat_api.url, cfg().the_cat_api.x_api_key)
    votes = Votes(cfg().the_cat_api.url, cfg().the_cat_api.x_api_key)

    image_id = images.get_images().get_response_attribute('id')
    vote = votes.create_vote(image_id, VoteValueParam.VALUE_UP)

    vote_message = vote.get_response_attribute('message')

    assert vote_message == 'SUCCESS'


def test_get_specific_vote():
    images = Images(cfg().the_cat_api.url, cfg().the_cat_api.x_api_key)
    votes = Votes(cfg().the_cat_api.url, cfg().the_cat_api.x_api_key)

    image_id = images.get_images().get_response_attribute('id')
    vote_id = votes.create_vote(image_id, VoteValueParam.VALUE_UP).get_response_attribute('id')
    votes.get_specific_vote(vote_id)


@pytest.mark.parametrize('vote_value, expected_value',
                         [(VoteValueParam.VALUE_UP, 1), (VoteValueParam.VALUE_DOWN, 0)])
def test_create_value_vote(vote_value, expected_value):
    images = Images(cfg().the_cat_api.url, cfg().the_cat_api.x_api_key)
    votes = Votes(cfg().the_cat_api.url, cfg().the_cat_api.x_api_key)

    image_id = images.get_images().get_response_attribute('id')
    vote_id = votes.create_vote(image_id, vote_value).get_response_attribute('id')
    specific_vote_value_attribute = votes.get_specific_vote(vote_id).get_response_attribute('value')

    assert specific_vote_value_attribute == expected_value


def test_delete_vote():
    images = Images(cfg().the_cat_api.url, cfg().the_cat_api.x_api_key)
    votes = Votes(cfg().the_cat_api.url, cfg().the_cat_api.x_api_key)

    image_id = get_random_image_id(images)
    vote = votes.create_vote(image_id, VoteValueParam.VALUE_UP)
    vote_id = get_response_attribute(vote, 'id')

    votes_before_delete = len(votes.get_votes().json())

    delete_vote = votes.delete_vote(vote_id)
    message = get_response_attribute(delete_vote, "message")

    votes_after_delete = len(votes.get_votes().json())

    assert message == "SUCCESS"
    votes.get_specific_vote(vote_id, expected_status_code=HTTPStatus.NOT_FOUND)

    assert votes_after_delete == votes_before_delete - 1
