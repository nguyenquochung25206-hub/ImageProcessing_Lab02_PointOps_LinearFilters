import numpy as np


def validate_image(image):
    """
    Kiểm tra ảnh đầu vào có hợp lệ hay không.

    Parameters
    ----------
    image : numpy.ndarray
        Ảnh cần kiểm tra.

    Returns
    -------
    bool
        True nếu ảnh hợp lệ.

    Raises
    ------
    TypeError
        Nếu image không phải numpy.ndarray.
    ValueError
        Nếu ảnh rỗng hoặc có kích thước không hợp lệ.
    """
    if not isinstance(image, np.ndarray):
        raise TypeError("Ảnh phải là numpy.ndarray.")

    if image.size == 0:
        raise ValueError("Ảnh không được rỗng.")

    if image.ndim not in (2, 3):
        raise ValueError(
            "Ảnh phải là ảnh grayscale (2 chiều) "
            "hoặc ảnh màu (3 chiều)."
        )

    return True


def validate_kernel_size(kernel_size):
    """
    Kiểm tra kích thước kernel.

    Kernel phải là số nguyên dương và thường phải là số lẻ.
    """
    if not isinstance(kernel_size, int):
        raise TypeError("kernel_size phải là số nguyên.")

    if kernel_size <= 0:
        raise ValueError("kernel_size phải lớn hơn 0.")

    if kernel_size % 2 == 0:
        raise ValueError("kernel_size phải là số lẻ.")

    return True


def validate_threshold(threshold):
    """
    Kiểm tra giá trị threshold trong khoảng 0-255.
    """
    if not isinstance(threshold, (int, float)):
        raise TypeError("threshold phải là số.")

    if threshold < 0 or threshold > 255:
        raise ValueError("threshold phải nằm trong khoảng 0-255.")

    return True


def validate_sigma(sigma):
    """
    Kiểm tra sigma của Gaussian filter.
    """
    if not isinstance(sigma, (int, float)):
        raise TypeError("sigma phải là số.")

    if sigma <= 0:
        raise ValueError("sigma phải lớn hơn 0.")

    return True


def validate_same_shape(image1, image2):
    """
    Kiểm tra hai ảnh có cùng kích thước hay không.
    """
    validate_image(image1)
    validate_image(image2)

    if image1.shape != image2.shape:
        raise ValueError(
            "Hai ảnh phải có cùng kích thước."
        )

    return True