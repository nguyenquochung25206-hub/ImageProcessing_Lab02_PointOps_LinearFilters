import numpy as np

from src.linear_filters.gaussian_filter import gaussian_filter


def test_gaussian_filter_output_shape():
    """Kết quả phải giữ nguyên kích thước ảnh."""
    image = np.random.randint(0, 256, (10, 10), dtype=np.uint8)

    result = gaussian_filter(image, 3, 1.0)

    assert result.shape == image.shape


def test_gaussian_filter_output_dtype():
    """Kết quả phải có kiểu dữ liệu uint8."""
    image = np.random.randint(0, 256, (10, 10), dtype=np.uint8)

    result = gaussian_filter(image, 3, 1.0)

    assert result.dtype == np.uint8


def test_gaussian_filter_smooths_noise():
    """Gaussian filter phải làm giảm nhiễu/độ biến động của ảnh."""
    image = np.array([
        [0, 255, 0],
        [255, 0, 255],
        [0, 255, 0]
    ], dtype=np.uint8)

    result = gaussian_filter(image, 3, 1.0)

    # Sau khi lọc, ảnh không còn giữ nguyên các giá trị cực đoan ban đầu.
    assert not np.array_equal(result, image)


def test_gaussian_filter_constant_image():
    """Ảnh đồng nhất sau Gaussian filter vẫn gần như đồng nhất."""
    image = np.full((10, 10), 128, dtype=np.uint8)

    result = gaussian_filter(image, 3, 1.0)

    np.testing.assert_allclose(result, 128, atol=1)