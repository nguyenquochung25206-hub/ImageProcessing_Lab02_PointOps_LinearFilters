import numpy as np

from src.point_operations.threshold import threshold_image


def test_threshold_binary_output():
    """Kết quả threshold phải chỉ chứa 0 và 255."""
    image = np.array([
        [50, 100],
        [150, 200]
    ], dtype=np.uint8)

    result = threshold_image(image, 128)

    expected = np.array([
        [0, 0],
        [255, 255]
    ], dtype=np.uint8)

    np.testing.assert_array_equal(result, expected)


def test_threshold_lower_values():
    """Pixel nhỏ hơn ngưỡng phải trở thành 0."""
    image = np.array([
        [10, 50],
        [80, 100]
    ], dtype=np.uint8)

    result = threshold_image(image, 128)

    expected = np.zeros((2, 2), dtype=np.uint8)

    np.testing.assert_array_equal(result, expected)


def test_threshold_upper_values():
    """Pixel lớn hơn hoặc bằng ngưỡng phải trở thành 255."""
    image = np.array([
        [150, 180],
        [200, 250]
    ], dtype=np.uint8)

    result = threshold_image(image, 128)

    expected = np.full((2, 2), 255, dtype=np.uint8)

    np.testing.assert_array_equal(result, expected)


def test_threshold_output_dtype():
    """Kết quả phải có kiểu dữ liệu uint8."""
    image = np.array([
        [20, 100],
        [150, 220]
    ], dtype=np.uint8)

    result = threshold_image(image, 128)

    assert result.dtype == np.uint8