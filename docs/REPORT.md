# REPORT.md

# BÁO CÁO PROJECT XỬ LÝ ẢNH

## 1. Thông tin dự án

**Tên dự án:** ImageProcessing_Lab02_PointOps_LinearFilters

**Ngôn ngữ:** Python

**Thư viện chính:**
- OpenCV
- NumPy
- Matplotlib
- Pytest

**Mục tiêu:**  
Xây dựng chương trình xử lý ảnh gồm các phép biến đổi điểm,
bộ lọc tuyến tính và một số kỹ thuật xử lý ảnh nâng cao.

---

## 2. Mục tiêu

Project tập trung vào các nội dung:

- Thay đổi độ sáng của ảnh.
- Thay đổi độ tương phản.
- Tạo ảnh âm bản.
- Phân ngưỡng ảnh.
- Làm mượt ảnh bằng Mean Filter.
- Làm mượt ảnh bằng Gaussian Filter.
- Tăng độ sắc nét bằng Sharpening.
- Phát hiện cạnh.
- Áp dụng Custom Kernel.
- Xử lý nhiễu bằng bộ lọc phi tuyến.
- So sánh kết quả của các phương pháp.
- Đánh giá kết quả bằng MSE, MAE và PSNR.

---

## 3. Cấu trúc chương trình

Project được chia thành các nhóm chức năng:

```text
src/
├── point_operations/
├── linear_filters/
├── advanced/
├── utils/
└── main.py

Point Operations
brightness.py
contrast.py
negative.py
threshold.py

Linear Filters
mean_filter.py
gaussian_filter.py
sharpening.py

Advanced
edge_detection.py
custom_kernel.py
filter_comparison.py
nonlinear_filter.py

Utilities
metrics.py
validation.py
visualization.py

4. Point Operations
4.1. Brightness
Brightness được sử dụng để thay đổi độ sáng của ảnh.
Giá trị beta được cộng vào từng pixel.
I' = I + beta

Nếu beta dương, ảnh sáng hơn.
Nếu beta âm, ảnh tối hơn.
Kết quả được giới hạn trong khoảng [0,255].
4.2. Contrast
Contrast được sử dụng để thay đổi độ tương phản.
Pixel được nhân với hệ số alpha.
I' = alpha × I

alpha > 1 làm tăng tương phản.
0 < alpha < 1 làm giảm tương phản.
4.3. Negative
Negative tạo ảnh âm bản bằng phép biến đổi:
I' = 255 - I

Các vùng sáng trở thành tối và ngược lại.
4.4. Threshold
Threshold chuyển ảnh thành ảnh nhị phân dựa trên ngưỡng T.
I' = 0       nếu I < T
I' = 255     nếu I >= T

Kết quả chỉ có hai mức cường độ là 0 và 255.
5. Linear Filters
5.1. Mean Filter
Mean Filter sử dụng giá trị trung bình của các pixel
trong vùng lân cận.
Mục đích chính:
- Làm mượt ảnh.
- Giảm nhiễu.
- Làm giảm các biến đổi cường độ nhỏ.
Nhược điểm là có thể làm mờ cạnh và chi tiết.
5.2. Gaussian Filter
Gaussian Filter sử dụng Gaussian Kernel để làm mượt ảnh.
Mục đích:
- Giảm nhiễu.
- Làm mượt ảnh.
- Chuẩn bị ảnh cho các bước xử lý tiếp theo.
Tham số sigma ảnh hưởng đến mức độ làm mượt.
5.3. Sharpening
Sharpening làm nổi bật sự thay đổi cường độ giữa các pixel.
Mục đích:
- Tăng độ sắc nét.
- Làm rõ chi tiết.
- Làm nổi bật cạnh.
6. Advanced Processing
6.1. Edge Detection
Edge Detection xác định các vùng có sự thay đổi cường độ
pixel lớn.
Quy trình tổng quát:
Input
 ↓
Grayscale
 ↓
Noise Reduction
 ↓
Gradient
 ↓
Edge Detection
 ↓
Output

Kết quả là ảnh biểu diễn các cạnh được phát hiện.
6.2. Custom Kernel
Custom Kernel cho phép áp dụng một kernel do người dùng
định nghĩa lên ảnh.
Kernel được thực hiện thông qua phép convolution.
Có thể sử dụng cho nhiều mục đích như:
- Làm mờ.
- Làm sắc nét.
- Phát hiện cạnh.
- Tạo hiệu ứng xử lý ảnh.
6.3. Nonlinear Filter
Project sử dụng các phương pháp lọc phi tuyến như:
- Median Filter.
- Bilateral Filter.
Median Filter phù hợp với việc giảm nhiễu
nhưng vẫn giữ được cấu trúc cạnh tốt hơn một số
bộ lọc trung bình.
Bilateral Filter thực hiện làm mượt trong khi cố gắng
giữ lại các cạnh.
6.4. Filter Comparison
Module Filter Comparison được sử dụng để so sánh
các phương pháp xử lý ảnh.
Các tiêu chí có thể xem xét:
- Mức độ làm mượt.
- Khả năng giảm nhiễu.
- Khả năng giữ chi tiết.
- Độ rõ của cạnh.
- Thời gian xử lý.
- MSE.
- MAE.
- PSNR.
7. Metrics
Project sử dụng ba chỉ số chính.
MSE
MSE = mean((I1 - I2)^2)

MSE càng nhỏ thì sai khác giữa hai ảnh càng thấp.
MAE
MAE = mean(|I1 - I2|)

MAE biểu diễn sai số tuyệt đối trung bình.
PSNR
PSNR = 10 × log10(MAX^2 / MSE)

Với ảnh 8-bit:
MAX = 255

Nếu MSE bằng 0 thì PSNR được xem là vô hạn.
8. Validation
Module validation.py thực hiện kiểm tra dữ liệu
trước khi xử lý.
Các chức năng gồm:
validate_image()
validate_kernel_size()
validate_threshold()
validate_sigma()
validate_same_shape()

Mục đích là hạn chế lỗi do dữ liệu đầu vào không hợp lệ.
9. Testing
Project sử dụng Pytest để kiểm tra các module.
Các test đã xây dựng cho những chức năng chính:
test_brightness.py
test_contrast.py
test_threshold.py
test_mean_filter.py
test_gaussian_filter.py
test_sharpening.py

Các test tập trung kiểm tra:
- Kết quả thuật toán.
- Kích thước output.
- Kiểu dữ liệu output.
- Các trường hợp biên.
- Tính ổn định của kết quả.
Chạy test bằng:
pytest -v

10. Input và Output
Ảnh đầu vào được sử dụng làm dữ liệu cho các
thuật toán xử lý.
Kết quả được lưu vào thư mục output theo từng nhóm
chức năng.
data/
├── input/
└── output/

Output có thể được phân loại:
output/
├── point_operations/
├── linear_filters/
└── advanced/
