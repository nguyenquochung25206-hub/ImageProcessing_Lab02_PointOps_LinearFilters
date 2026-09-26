import numpy as np

from src.linear_filters.mean_filter import mean_filter


def test_mean_filter_output_shape():
    """Kết quả phải giữ nguyên kích thước ảnh."""
    image = np.random.randint(0, 256, (10, 10), dtype=np.uint8)

    result = mean_filter(image, 3)

    assert result.shape == image.shape


def test_mean_filter_output_dtype():
    """Kết quả phải có kiểu dữ liệu uint8."""
    image = np.random.randint(0, 256, (10, 10), dtype=np.uint8)

    result = mean_filter(image, 3)

    assert result.dtype == np.uint8


def test_mean_filter_smooths_image():
    """Mean filter phải làm mượt ảnh."""
    image = np.array([
        [0, 0, 0],
        [0, 255, 0],
        [0, 0, 0]
    ], dtype=np.uint8)

    result = mean_filter(image, 3)

    # Pixel trung tâm không còn giữ nguyên giá trị 255.
    assert result[1, 1] < 255


def test_mean_filter_constant_image():
    """Ảnh đồng nhất sau Mean filter vẫn giữ nguyên giá trị."""
    image = np.full((10, 10), 128, dtype=np.uint8)

    result = mean_filter(image, 3)

    np.testing.assert_allclose(result, 128, atol=1)