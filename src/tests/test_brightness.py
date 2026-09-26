import numpy as np

from src.point_operations.brightness import change_brightness


def test_increase_brightness():
    image = np.array(
        [
            [10, 20],
            [30, 40]
        ],
        dtype=np.uint8
    )

    result = change_brightness(image, 20)

    expected = np.array(
        [
            [30, 40],
            [50, 60]
        ],
        dtype=np.uint8
    )

    np.testing.assert_array_equal(result, expected)


def test_decrease_brightness():
    image = np.array(
        [
            [50, 60],
            [70, 80]
        ],
        dtype=np.uint8
    )

    result = change_brightness(image, -20)

    expected = np.array(
        [
            [30, 40],
            [50, 60]
        ],
        dtype=np.uint8
    )

    np.testing.assert_array_equal(result, expected)


def test_brightness_upper_limit():
    image = np.array(
        [
            [240, 250],
            [255, 100]
        ],
        dtype=np.uint8
    )

    result = change_brightness(image, 30)

    expected = np.array(
        [
            [255, 255],
            [255, 130]
        ],
        dtype=np.uint8
    )

    np.testing.assert_array_equal(result, expected)


def test_brightness_lower_limit():
    image = np.array(
        [
            [10, 20],
            [0, 100]
        ],
        dtype=np.uint8
    )

    result = change_brightness(image, -30)

    expected = np.array(
        [
            [0, 0],
            [0, 70]
        ],
        dtype=np.uint8
    )

    np.testing.assert_array_equal(result, expected)