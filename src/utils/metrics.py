import numpy as np


def mse(image1, image2):
    """
    Tính Mean Squared Error (MSE) giữa hai ảnh.

    MSE càng nhỏ thì hai ảnh càng giống nhau.
    """
    image1 = np.asarray(image1, dtype=np.float64)
    image2 = np.asarray(image2, dtype=np.float64)

    if image1.shape != image2.shape:
        raise ValueError("Hai ảnh phải có cùng kích thước.")

    return np.mean((image1 - image2) ** 2)


def mae(image1, image2):
    """
    Tính Mean Absolute Error (MAE) giữa hai ảnh.

    MAE càng nhỏ thì sai khác giữa hai ảnh càng ít.
    """
    image1 = np.asarray(image1, dtype=np.float64)
    image2 = np.asarray(image2, dtype=np.float64)

    if image1.shape != image2.shape:
        raise ValueError("Hai ảnh phải có cùng kích thước.")

    return np.mean(np.abs(image1 - image2))


def psnr(image1, image2, max_pixel=255.0):
    """
    Tính Peak Signal-to-Noise Ratio (PSNR).

    PSNR càng lớn thì chất lượng ảnh so với ảnh gốc càng tốt.
    """
    error = mse(image1, image2)

    if error == 0:
        return float("inf")

    return 10 * np.log10((max_pixel ** 2) / error)