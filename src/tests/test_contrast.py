import numpy as np

from src.point_operations.contrast import change_contrast


def test_increase_contrast():
    image = np.array(
        [
            [10, 20],
            [30, 40]
        ],
        dtype=np.uint8
    )

    result = change_contrast(image, 2.0)

    expected = np.array(
        [
            [20, 40],
            [60, 80]
        ],
        dtype=np.uint8
    )

    np.testing.assert_array_equal(result, expected)


def test_decrease_contrast():
    image = np.array(
        [
            [20, 40],
            [60, 80]
        ],
        dtype=np.uint8
    )

    result = change_contrast(image, 0.5)

    expected = np.array(
        [
            [10, 20],
            [30, 40]
        ],
        dtype=np.uint8
    )

    np.testing.assert_array_equal(result, expected)


def test_contrast_upper_limit():
    image = np.array(
        [
            [100, 150],
            [200, 255]
        ],
        dtype=np.uint8
    )

    result = change_contrast(image, 2.0)

    expected = np.array(
        [
            [200, 255],
            [255, 255]
        ],
        dtype=np.uint8
    )

    np.testing.assert_array_equal(result, expected)


def test_contrast_lower_limit():
    image = np.array(
        [
            [0, 10],
            [20, 30]
        ],
        dtype=np.uint8
    )

    result = change_contrast(image, 0.5)

    expected = np.array(
        [
            [0, 5],
            [10, 15]
        ],
        dtype=np.uint8
    )

    np.testing.assert_array_equal(result, expected)