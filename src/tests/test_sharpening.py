import numpy as np

from src.linear_filters.sharpening import sharpen_image


def test_sharpening_output_shape():
    """Kết quả phải giữ nguyên kích thước ảnh."""
    image = np.random.randint(0, 256, (10, 10), dtype=np.uint8)

    result = sharpen_image(image)

    assert result.shape == image.shape


def test_sharpening_output_dtype():
    """Kết quả phải có kiểu dữ liệu uint8."""
    image = np.random.randint(0, 256, (10, 10), dtype=np.uint8)

    result = sharpen_image(image)

    assert result.dtype == np.uint8


def test_sharpening_changes_image():
    """Sharpening phải tạo ra thay đổi trên ảnh có biên."""
    image = np.array([
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 255, 255, 255],
        [0, 0, 255, 255, 255],
        [0, 0, 255, 255, 255]
    ], dtype=np.uint8)

    result = sharpen_image(image)

    assert not np.array_equal(result, image)


def test_sharpening_constant_image():
    """Ảnh đồng nhất không nên bị thay đổi đáng kể."""
    image = np.full((10, 10), 128, dtype=np.uint8)

    result = sharpen_image(image)

    np.testing.assert_allclose(result, 128, atol=1)