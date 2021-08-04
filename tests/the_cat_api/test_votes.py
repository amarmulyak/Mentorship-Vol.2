from http import HTTPStatus

import pytest

from src.the_cat_api.votes import Votes
from src.utils.api import parse_response, get_response_attribute, get_response_attribute_type
from src.utils.utils import cfg
from src.the_cat_api.images import Images
from src.the_cat_api.vote_params_data import VoteValueParam


def get_random_image_id(image_api):
    random_image = parse_response(image_api.get_images())[0]

    return random_image.get('id')


def test_get_vote_response_code():
    votes = Votes(cfg().the_cat_api.url, cfg().the_cat_api.x_api_key)
    response = votes.get_votes()

    assert response.status_code == HTTPStatus.OK


def test_get_vote_limit():
    limit = 5
    votes = Votes(cfg().the_cat_api.url, cfg().the_cat_api.x_api_key)
    response = votes.get_votes(limit=limit)
    parsed_response = parse_response(response)

    assert len(parsed_response) == limit


def test_create_vote_status_code():
    images = Images(cfg().the_cat_api.url, cfg().the_cat_api.x_api_key)
    votes = Votes(cfg().the_cat_api.url, cfg().the_cat_api.x_api_key)

    image_id = images.get_random_image_id()
    vote = votes.create_vote(image_id, VoteValueParam.VALUE_UP)

    assert vote.status_code == HTTPStatus.OK


def test_create_vote_response():
    images = Images(cfg().the_cat_api.url, cfg().the_cat_api.x_api_key)
    votes = Votes(cfg().the_cat_api.url, cfg().the_cat_api.x_api_key)

    image_id = get_random_image_id(images)
    vote = votes.create_vote(image_id, VoteValueParam.VALUE_UP)

    vote_id = get_response_attribute(vote, 'id')
    assert get_response_attribute_type(vote_id) == int

    vote_message = get_response_attribute(vote, 'message')
    assert vote_message == 'SUCCESS'


def test_get_specific_vote():
    images = Images(cfg().the_cat_api.url, cfg().the_cat_api.x_api_key)
    votes = Votes(cfg().the_cat_api.url, cfg().the_cat_api.x_api_key)

    image_id = get_random_image_id(images)
    vote = votes.create_vote(image_id, VoteValueParam.VALUE_UP)
    vote_id = get_response_attribute(vote, 'id')

    specific_vote = votes.get_specific_vote(vote_id)

    assert specific_vote.status_code == HTTPStatus.OK


@pytest.mark.parametrize('vote_value, expected_value',
                         [(VoteValueParam.VALUE_UP, 1), (VoteValueParam.VALUE_DOWN, 0)])
def test_create_value_vote(vote_value, expected_value):
    images = Images(cfg().the_cat_api.url, cfg().the_cat_api.x_api_key)
    votes = Votes(cfg().the_cat_api.url, cfg().the_cat_api.x_api_key)

    image_id = get_random_image_id(images)
    vote = votes.create_vote(image_id, vote_value)
    vote_id = get_response_attribute(vote, 'id')

    specific_vote = votes.get_specific_vote(vote_id)
    value = get_response_attribute(specific_vote, 'value')

    assert value == expected_value

