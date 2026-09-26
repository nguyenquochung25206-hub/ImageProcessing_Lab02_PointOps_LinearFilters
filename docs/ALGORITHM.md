## 1. Tổng quan

Project thực hiện các kỹ thuật xử lý ảnh gồm:

- Point Operations
- Linear Filters
- Advanced Processing
- Metrics
- Visualization

---

## 2. Point Operations

### 2.1. Brightness

Điều chỉnh độ sáng bằng cách cộng hoặc trừ giá trị `β`:

```text
I'(x,y) = I(x,y) + β

Giá trị pixel được giới hạn trong khoảng 0–255.
File:
src/point_operations/brightness.py

2.2. Contrast
Điều chỉnh độ tương phản:
I'(x,y) = α × I(x,y)

- α > 1: tăng tương phản.
- 0 < α < 1: giảm tương phản.
File:
src/point_operations/contrast.py

2.3. Negative
Đảo ngược giá trị pixel:
I'(x,y) = 255 - I(x,y)

File:
src/point_operations/negative.py

2.4. Threshold
Chuyển ảnh thành ảnh nhị phân dựa trên ngưỡng T:
I'(x,y) = 255 nếu I(x,y) >= T
           0   nếu I(x,y) < T

File:
src/point_operations/threshold.py

3. Linear Filters
3.1. Mean Filter
Tính trung bình các pixel trong vùng lân cận.
Với kernel k × k:
K(i,j) = 1 / (k × k)

Tác dụng:
- Làm mượt ảnh.
- Giảm nhiễu.
Hạn chế:
- Có thể làm mờ biên và chi tiết.
File:
src/linear_filters/mean_filter.py

3.2. Gaussian Filter
Sử dụng hàm Gaussian để tạo kernel:
G(x,y) = 1/(2πσ²) × exp(-(x²+y²)/(2σ²))

Pixel gần tâm kernel có trọng số lớn hơn.
Tác dụng:
- Làm mượt ảnh.
- Giảm nhiễu.
- Hỗ trợ xử lý trước khi phát hiện biên.
File:
src/linear_filters/gaussian_filter.py

3.3. Sharpening
Làm tăng độ sắc nét và làm nổi bật biên.
Ví dụ kernel:
[ 0 -1  0 ]
[-1  5 -1 ]
[ 0 -1  0 ]

Tác dụng:
- Tăng độ rõ chi tiết.
- Làm nổi bật biên.
Hạn chế:
- Có thể làm nhiễu rõ hơn.
File:
src/linear_filters/sharpening.py

4. Advanced Processing
4.1. Edge Detection
Phát hiện các vùng có sự thay đổi cường độ mạnh.
Pipeline Canny:
Input
  ↓
Grayscale
  ↓
Gaussian Blur
  ↓
Gradient
  ↓
Non-Maximum Suppression
  ↓
Double Threshold
  ↓
Hysteresis
  ↓
Edges

File:
src/advanced/edge_detection.py

4.2. Custom Kernel
Áp dụng kernel do người dùng định nghĩa bằng phép convolution:
I'(x,y) = ΣΣ K(i,j) × I(x-i,y-j)

File:
src/advanced/custom_kernel.py

4.3. Nonlinear Filter
Median Filter
Thay pixel trung tâm bằng giá trị median của vùng lân cận.
Ví dụ:
[10, 20, 200, 30, 40]
→ [10, 20, 30, 40, 200]
→ Median = 30

Phù hợp để giảm nhiễu salt-and-pepper.
File:
src/advanced/nonlinear_filter.py

4.4. Filter Comparison
So sánh kết quả của nhiều bộ lọc trên cùng một ảnh:
Original
   ├── Mean
   ├── Gaussian
   ├── Median
   └── Sharpening

File:
src/advanced/filter_comparison.py

5. Metrics
5.1. MSE
Đo sai số bình phương trung bình:
MSE = 1/N × Σ(I - K)²

MSE càng nhỏ, sai số càng nhỏ.
5.2. MAE
Đo sai số tuyệt đối trung bình:
MAE = 1/N × Σ|I - K|

5.3. PSNR
Đánh giá chất lượng ảnh dựa trên MSE:
PSNR = 10 × log10(MAX² / MSE)

Với ảnh 8-bit:
MAX = 255

Nếu MSE = 0, hai ảnh giống nhau hoàn toàn.
File:
src/utils/metrics.py

6. Visualization
Module visualization hỗ trợ:
- Hiển thị ảnh gốc.
- Hiển thị ảnh sau xử lý.
- So sánh nhiều kết quả.
- Hiển thị histogram khi cần.
File:
src/utils/visualization.py

7. Pipeline tổng quát
Input Image
     ↓
Image I/O
     ↓
Point Operations
     │
     ├── Brightness
     ├── Contrast
     ├── Negative
     └── Threshold
     ↓
Linear Filters
     │
     ├── Mean
     ├── Gaussian
     └── Sharpening
     ↓
Advanced
     │
     ├── Edge Detection
     ├── Custom Kernel
     ├── Nonlinear Filter
     └── Filter Comparison
     ↓
Metrics / Visualization
     ↓
Output

8. So sánh phương pháp
Phương pháp	Mục đích	Hạn chế
Brightness	Điều chỉnh sáng	Không xử lý nhiễu
Contrast	Điều chỉnh tương phản	Có thể mất chi tiết
Negative	Đảo ảnh	Biến đổi cơ bản
Threshold	Nhị phân hóa	Phụ thuộc ngưỡng
Mean	Làm mượt	Làm mờ biên
Gaussian	Làm mượt	Có thể mất chi tiết
Sharpening	Làm sắc nét	Có thể khuếch đại nhiễu
Median	Giảm nhiễu	Có thể mất chi tiết
Edge Detection	Phát hiện biên	Nhạy với nhiễu
Custom Kernel	Xử lý tùy chỉnh	Phụ thuộc kernel