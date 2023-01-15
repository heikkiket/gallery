from pathlib import Path

import pytest

from Imagegallery import Image
from viewer.logic import Viewer


@pytest.fixture
def viewer():
    viewer = Viewer()
    images = [Image(Path("img1"), "jpg"),
              Image(Path("img2"), "jpg"),
              Image(Path("img3"), "jpg")]
    viewer.add_images(images)
    return viewer


def test_viewer_is_empty():
    viewer = Viewer()
    assert not viewer.has_images()

def test_after_load_is_not_empty(viewer):
    assert viewer.has_images()

def test_counts_image_amount(viewer):
    assert viewer.count() == 3

def test_has_current_image(viewer):
    assert viewer.current_image().name == "img1"

def test_go_next_returns_viewer(viewer):
    assert viewer.go_next().count() == 3

def test_go_next_changes_state(viewer):
    assert viewer.go_next().current_image().name == "img2"

def test_go_prev_works_as_well(viewer):
    viewer.go_next()
    assert viewer.go_prev().current_image().name == "img1"

def test_prev_cant_go_out_of_bounds(viewer):
    assert viewer.go_prev().current_image().name == "img1"

def test_next_cant_go_out_of_bounds(viewer):
    viewer.go_next()
    viewer.go_next()
    viewer.go_next()
    assert viewer.go_next().current_image().name == "img3"

def test_can_empty_viewer(viewer):
    viewer.empty()
    assert not viewer.has_images()
