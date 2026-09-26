import numpy as np
from src.point_operations.negative import negative_image


def test_negative_image():
    image = np.array([
        [0, 50],
        [100, 255]
    ], dtype=np.uint8)

    result = negative_image(image)

    expected = np.array([
        [255, 205],
        [155, 0]
    ], dtype=np.uint8)

    np.testing.assert_array_equal(result, expected)


def test_negative_output_shape():
    image = np.random.randint(
        0, 256, (10, 10), dtype=np.uint8
    )

    result = negative_image(image)

    assert result.shape == image.shape


def test_negative_output_dtype():
    image = np.random.randint(
        0, 256, (10, 10), dtype=np.uint8
    )

    result = negative_image(image)

    assert result.dtype == np.uint8


def test_negative_twice_returns_original():
    image = np.array([
        [10, 20],
        [100, 200]
    ], dtype=np.uint8)

    result = negative_image(
        negative_image(image)
    )

    np.testing.assert_array_equal(result, image)