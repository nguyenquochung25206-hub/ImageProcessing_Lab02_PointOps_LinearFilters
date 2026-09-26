# ALGORITHM.md

## 1. Tổng quan

Project thực hiện các kỹ thuật xử lý ảnh gồm:
- Point Operations
- Linear Filters
- Advanced Image Processing
- Metrics
- Visualization

Pipeline tổng quát:

Input Image
    ↓
Read Image
    ↓
Point Operations / Linear Filters / Advanced
    ↓
Save Output
    ↓
Evaluate Results

---

## 2. Point Operations

### 2.1. Brightness

File: `src/point_operations/brightness.py`

Mục đích: thay đổi độ sáng của ảnh.

Công thức:

    I'(x,y) = I(x,y) + beta

Trong đó:
- `I(x,y)`: pixel ảnh gốc.
- `beta`: mức thay đổi độ sáng.
- `I'(x,y)`: pixel sau xử lý.

Nếu `beta > 0`: ảnh sáng hơn.
Nếu `beta < 0`: ảnh tối hơn.

Giá trị pixel được giới hạn trong khoảng `[0,255]`.

---

### 2.2. Contrast

File: `src/point_operations/contrast.py`

Mục đích: thay đổi độ tương phản.

Công thức:

    I'(x,y) = alpha * I(x,y)

Trong đó:
- `alpha > 1`: tăng tương phản.
- `0 < alpha < 1`: giảm tương phản.

Kết quả được giới hạn trong `[0,255]`.

---

### 2.3. Negative

File: `src/point_operations/negative.py`

Mục đích: tạo ảnh âm bản.

Công thức:

    I'(x,y) = 255 - I(x,y)

Pixel sáng trở thành tối và pixel tối trở thành sáng.

---

### 2.4. Threshold

File: `src/point_operations/threshold.py`

Mục đích: chuyển ảnh thành ảnh nhị phân.

Với ngưỡng `T`:

    I'(x,y) = 0       nếu I(x,y) < T
    I'(x,y) = 255     nếu I(x,y) >= T

Kết quả chỉ gồm hai mức:
- `0`
- `255`

---

## 3. Linear Filters

### 3.1. Mean Filter

File: `src/linear_filters/mean_filter.py`

Mục đích: làm mượt ảnh và giảm nhiễu.

Mean Filter thay thế mỗi pixel bằng giá trị trung bình
của các pixel trong vùng kernel.

Với kernel kích thước `k × k`:

    I'(x,y) = (1 / k²) * Σ I(i,j)

Kernel thường sử dụng kích thước lẻ như:
- 3 × 3
- 5 × 5
- 7 × 7

Kernel lớn hơn tạo hiệu ứng làm mờ mạnh hơn.

---

### 3.2. Gaussian Filter

File: `src/linear_filters/gaussian_filter.py`

Mục đích:
- Làm mượt ảnh.
- Giảm nhiễu.
- Giảm ảnh hưởng của các pixel lân cận xa.

Gaussian Kernel được xây dựng dựa trên hàm Gaussian.

Công thức:

    G(x,y) =
    1 / (2πσ²) *
    exp(-(x²+y²)/(2σ²))

Trong đó:
- `σ`: độ lệch chuẩn.
- `σ` lớn → làm mượt mạnh hơn.
- `σ` nhỏ → giữ nhiều chi tiết hơn.

Ảnh được xử lý bằng phép convolution giữa ảnh
và Gaussian Kernel.

---

### 3.3. Sharpening

File: `src/linear_filters/sharpening.py`

Mục đích: tăng độ sắc nét và làm nổi bật cạnh.

Sharpening thường sử dụng kernel có giá trị trung tâm lớn
và các giá trị xung quanh âm.

Ví dụ:

    [ 0 -1  0 ]
    [-1  5 -1 ]
    [ 0 -1  0 ]

Kết quả làm tăng sự khác biệt giữa pixel trung tâm
và các pixel lân cận.

---

## 4. Advanced Processing

### 4.1. Edge Detection

File: `src/advanced/edge_detection.py`

Mục đích: phát hiện các cạnh trong ảnh.

Quy trình tổng quát:

    Input Image
        ↓
    Grayscale
        ↓
    Gaussian Blur
        ↓
    Gradient
        ↓
    Non-maximum Suppression
        ↓
    Double Threshold
        ↓
    Edge Image

Edge Detection giúp xác định những vùng có sự thay đổi
cường độ pixel lớn.

---

### 4.2. Custom Kernel

File: `src/advanced/custom_kernel.py`

Mục đích: cho phép áp dụng kernel tùy chỉnh lên ảnh.

Quy trình:

    Input Image
        ↓
    Validate Kernel
        ↓
    Convolution
        ↓
    Output Image

Custom Kernel có thể được sử dụng cho:
- Blur
- Sharpen
- Edge detection
- Các hiệu ứng xử lý ảnh khác

---

### 4.3. Nonlinear Filter

File: `src/advanced/nonlinear_filter.py`

Mục đích: xử lý nhiễu bằng các bộ lọc phi tuyến.

Các bộ lọc được sử dụng trong project gồm:
- Median Filter
- Bilateral Filter

Median Filter thay pixel bằng giá trị trung vị
của vùng lân cận.

Bilateral Filter làm mượt ảnh nhưng cố gắng
giữ lại các cạnh.

---

### 4.4. Filter Comparison

File: `src/advanced/filter_comparison.py`

Mục đích: so sánh kết quả của nhiều bộ lọc.

Các tiêu chí có thể sử dụng:
- Mức độ làm mờ.
- Khả năng giảm nhiễu.
- Khả năng giữ chi tiết.
- Độ rõ của cạnh.
- Thời gian xử lý.
- MSE.
- MAE.
- PSNR.

Quy trình:

    Input Image
        ↓
    Apply Filters
        ↓
    Calculate Metrics
        ↓
    Compare Results
        ↓
    Generate Report

---

## 5. Metrics

File: `src/utils/metrics.py`

### 5.1. MSE

Mean Squared Error:

    MSE = mean((I1 - I2)²)

MSE càng nhỏ thì sai khác giữa hai ảnh càng thấp.

---

### 5.2. MAE

Mean Absolute Error:

    MAE = mean(|I1 - I2|)

MAE đo sai khác tuyệt đối trung bình giữa hai ảnh.

MAE càng nhỏ thì hai ảnh càng ít khác biệt.

---

### 5.3. PSNR

Peak Signal-to-Noise Ratio:

    PSNR = 10 log10(MAX² / MSE)

Với ảnh 8-bit:

    MAX = 255

Nếu `MSE = 0`, PSNR được xem là vô hạn.

PSNR càng lớn thì ảnh kết quả càng gần ảnh tham chiếu.

---

## 6. Validation

File: `src/utils/validation.py`

Validation được sử dụng để kiểm tra dữ liệu trước khi xử lý.

Các kiểm tra chính:

### validate_image()
- Kiểm tra kiểu `numpy.ndarray`.
- Kiểm tra ảnh không rỗng.
- Kiểm tra ảnh có 2 hoặc 3 chiều.

### validate_kernel_size()
- Kernel phải là số nguyên.
- Kernel phải lớn hơn 0.
- Kernel phải là số lẻ.

### validate_threshold()
- Threshold phải nằm trong `[0,255]`.

### validate_sigma()
- Sigma phải lớn hơn 0.

### validate_same_shape()
- Hai ảnh phải có cùng kích thước.

---

## 7. Visualization

File: `src/utils/visualization.py`

Visualization được sử dụng để:
- Hiển thị ảnh gốc.
- Hiển thị ảnh sau xử lý.
- So sánh nhiều kết quả.
- Hiển thị histogram hoặc kết quả thực nghiệm
  khi cần thiết.

---

## 8. Processing Pipeline

Pipeline tổng quát của project:

    Input
      ↓
    Validation
      ↓
    Image Processing
      ↓
    Output
      ↓
    Metrics
      ↓
    Visualization
      ↓
    Comparison

---

## 9. Output

Kết quả xử lý được lưu trong thư mục:

    data/output/

Các kết quả có thể được phân loại thành:

    data/output/
    ├── point_operations/
    ├── linear_filters/
    └── advanced/

---

## 10. Mục tiêu đánh giá

Project tập trung đánh giá:
- Ảnh sau xử lý.
- Mức độ giảm nhiễu.
- Mức độ làm mượt.
- Độ sắc nét.
- Khả năng giữ cạnh.
- Sai khác giữa ảnh gốc và ảnh kết quả.
- Thời gian xử lý.

Các thuật toán được thực nghiệm trên cùng dữ liệu
để thuận tiện cho việc so sánh.
