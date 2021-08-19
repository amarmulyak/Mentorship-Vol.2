import pytest

from src.the_cat_api.votes import Votes
from src.utils.utils import cfg
from src.the_cat_api.images import Images
from src.the_cat_api.vote_params_data import VoteValueParam
from http import HTTPStatus


def test_get_vote_limit():
    limit = 5
    votes = Votes(cfg().the_cat_api.url, cfg().the_cat_api.x_api_key)
    response = votes.get_votes(limit=limit).json

    assert len(response) == limit


def test_create_vote_response():
    images = Images(cfg().the_cat_api.url, cfg().the_cat_api.x_api_key)
    votes = Votes(cfg().the_cat_api.url, cfg().the_cat_api.x_api_key)

    image_id = images.get_images().get_response_item('$.[0].id')
    vote_message = votes.create_vote(image_id, VoteValueParam.VALUE_UP).get_response_item('message')

    assert vote_message == 'SUCCESS'


@pytest.mark.parametrize('vote_value, expected_value',
                         [(VoteValueParam.VALUE_UP, 1), (VoteValueParam.VALUE_DOWN, 0)])
def test_get_specific_vote(vote_value, expected_value):
    images = Images(cfg().the_cat_api.url, cfg().the_cat_api.x_api_key)
    votes = Votes(cfg().the_cat_api.url, cfg().the_cat_api.x_api_key)

    image_id = images.get_images().get_response_item('$.[0].id')
    vote_id = votes.create_vote(image_id, vote_value).get_response_item('id')
    specific_vote_value_attribute = votes.get_specific_vote(vote_id).get_response_item('value')

    assert specific_vote_value_attribute == expected_value


def test_delete_vote():
    images = Images(cfg().the_cat_api.url, cfg().the_cat_api.x_api_key)
    votes = Votes(cfg().the_cat_api.url, cfg().the_cat_api.x_api_key)

    image_id = images.get_images().get_response_item('$.[0].id')
    vote_id = votes.create_vote(image_id, VoteValueParam.VALUE_UP).get_response_item('id')

    votes_before_delete = len(votes.get_votes().json)

    delete_vote_message_attribute = votes.delete_vote(vote_id).get_response_item('message')

    votes_after_delete = len(votes.get_votes().json)

    assert delete_vote_message_attribute == "SUCCESS"
    votes.get_specific_vote(vote_id, expected_status_code=HTTPStatus.NOT_FOUND)

    assert votes_after_delete == votes_before_delete - 1
