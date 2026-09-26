import numpy as np
from src.linear_filters.sharpening import sharpening


def test_sharpening_output_shape():
    image = np.random.randint(
        0, 256, (10, 10), dtype=np.uint8
    )

    result = sharpening(image)

    assert result.shape == image.shape


def test_sharpening_output_dtype():
    image = np.random.randint(
        0, 256, (10, 10), dtype=np.uint8
    )

    result = sharpening(image)

    assert result.dtype == np.uint8


def test_sharpening_changes_image():
   def test_sharpening_changes_image():
    image = np.array([
        [50, 60, 70, 80, 90],
        [60, 70, 80, 90, 100],
        [70, 80, 100, 110, 120],
        [80, 90, 110, 120, 130],
        [90, 100, 120, 130, 140]
    ], dtype=np.uint8)

    result = sharpening(image)

    assert result.shape == image.shape
    assert not np.array_equal(result, image)


def test_sharpening_constant_image():
    image = np.full(
        (10, 10),
        128,
        dtype=np.uint8
    )

    result = sharpening(image)

    np.testing.assert_allclose(
        result,
        128,
        atol=1
    )