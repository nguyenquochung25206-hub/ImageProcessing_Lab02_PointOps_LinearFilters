# RESULTS.md

# KẾT QUẢ THỰC NGHIỆM

## 1. Tổng quan

File này ghi nhận kết quả xử lý ảnh của project
ImageProcessing_Lab02_PointOps_LinearFilters.

Các nhóm thuật toán được thực nghiệm:

- Point Operations
- Linear Filters
- Advanced Processing
- Image Quality Metrics

---

## 2. Point Operations

### 2.1. Brightness

**Mục tiêu:** thay đổi độ sáng của ảnh.

| Tham số | Giá trị |
|---|---|
| Input | Ảnh đầu vào |
| Operation | Brightness |
| Beta | Theo cấu hình thực nghiệm |
| Output | Ảnh sau khi thay đổi độ sáng |

Kết quả quan sát:

- Beta dương làm ảnh sáng hơn.
- Beta âm làm ảnh tối hơn.
- Giá trị pixel được giới hạn trong khoảng 0–255.

---

### 2.2. Contrast

**Mục tiêu:** thay đổi độ tương phản.

| Tham số | Giá trị |
|---|---|
| Input | Ảnh đầu vào |
| Operation | Contrast |
| Alpha | Theo cấu hình thực nghiệm |
| Output | Ảnh sau khi thay đổi tương phản |

Kết quả quan sát:

- Alpha lớn hơn 1 làm tăng tương phản.
- Alpha nằm giữa 0 và 1 làm giảm tương phản.
- Giá trị pixel được giới hạn trong khoảng 0–255.

---

### 2.3. Negative

**Mục tiêu:** tạo ảnh âm bản.

| Tham số | Giá trị |
|---|---|
| Input | Ảnh đầu vào |
| Operation | Negative |
| Output | Ảnh âm bản |

Kết quả quan sát:

- Pixel sáng trở thành tối.
- Pixel tối trở thành sáng.
- Ảnh kết quả giữ nguyên kích thước ảnh đầu vào.

---

### 2.4. Threshold

**Mục tiêu:** chuyển ảnh thành ảnh nhị phân.

| Tham số | Giá trị |
|---|---|
| Input | Ảnh đầu vào |
| Operation | Threshold |
| Threshold | Theo cấu hình thực nghiệm |
| Output | Ảnh nhị phân |

Kết quả quan sát:

- Pixel dưới ngưỡng được đưa về 0.
- Pixel từ ngưỡng trở lên được đưa về 255.
- Kết quả gồm hai mức cường độ chính.

---

## 3. Linear Filters

### 3.1. Mean Filter

**Mục tiêu:** làm mượt và giảm nhiễu.

Kết quả quan sát:

- Các thay đổi nhỏ giữa các pixel được làm mượt.
- Nhiễu có thể được giảm.
- Các cạnh và chi tiết có thể bị làm mờ.

---

### 3.2. Gaussian Filter

**Mục tiêu:** làm mượt ảnh và giảm nhiễu.

Kết quả quan sát:

- Ảnh được làm mượt.
- Nhiễu được giảm.
- Mức độ làm mượt phụ thuộc vào kernel và sigma.
- Các chi tiết nhỏ có thể bị giảm sau khi lọc.

---

### 3.3. Sharpening

**Mục tiêu:** tăng độ sắc nét.

Kết quả quan sát:

- Các cạnh được làm nổi bật.
- Chi tiết ảnh trở nên rõ hơn.
- Việc tăng sharpening quá mức có thể làm xuất hiện các vùng biên mạnh.

---

## 4. Advanced Processing

### 4.1. Edge Detection

**Mục tiêu:** phát hiện các cạnh trong ảnh.

Kết quả quan sát:

- Các vùng có thay đổi cường độ lớn được phát hiện.
- Kết quả biểu diễn cấu trúc cạnh của ảnh.
- Chất lượng kết quả phụ thuộc vào bước tiền xử lý
  và các tham số của thuật toán.

---

### 4.2. Custom Kernel

**Mục tiêu:** áp dụng kernel tùy chỉnh.

Kết quả phụ thuộc vào kernel được sử dụng.

Một kernel khác nhau có thể tạo ra:

- Hiệu ứng làm mờ.
- Tăng độ sắc nét.
- Phát hiện cạnh.
- Các hiệu ứng xử lý ảnh khác.

---

### 4.3. Nonlinear Filter

Các phương pháp được sử dụng:

- Median Filter.
- Bilateral Filter.

Kết quả quan sát:

**Median Filter**
- Có khả năng giảm nhiễu.
- Có thể giữ lại cấu trúc cạnh tốt hơn một số bộ lọc trung bình.

**Bilateral Filter**
- Làm mượt ảnh.
- Có khả năng bảo toàn cạnh trong quá trình lọc.

---

## 5. Filter Comparison

Các bộ lọc được so sánh dựa trên:

- Mức độ làm mượt.
- Khả năng giảm nhiễu.
- Khả năng giữ chi tiết.
- Độ rõ của cạnh.
- Thời gian xử lý.
- MSE.
- MAE.
- PSNR.

Bảng kết quả thực nghiệm:

| Method | MSE | MAE | PSNR | Time |
|---|---:|---:|---:|---:|
| Mean Filter | Chưa đo | Chưa đo | Chưa đo | Chưa đo |
| Gaussian Filter | Chưa đo | Chưa đo | Chưa đo | Chưa đo |
| Sharpening | Chưa đo | Chưa đo | Chưa đo | Chưa đo |
| Median Filter | Chưa đo | Chưa đo | Chưa đo | Chưa đo |
| Bilateral Filter | Chưa đo | Chưa đo | Chưa đo | Chưa đo |

Các giá trị trong bảng sẽ được cập nhật sau khi
chạy thực nghiệm thực tế.

---

## 6. Metrics

Project sử dụng:

### MSE

Dùng để đo sai số bình phương trung bình giữa
ảnh tham chiếu và ảnh kết quả.

Giá trị càng nhỏ thể hiện sai khác càng thấp.

### MAE

Dùng để đo sai số tuyệt đối trung bình.

Giá trị càng nhỏ thể hiện sai khác càng thấp.

### PSNR

Dùng để đánh giá mức độ tương đồng giữa ảnh
tham chiếu và ảnh kết quả dựa trên MSE.

Giá trị PSNR được tính từ MSE.

---

## 7. Kiểm thử

Các test đã xây dựng cho những module chính:

```text
test_brightness.py
test_contrast.py
test_threshold.py
test_mean_filter.py
test_gaussian_filter.py
test_sharpening.py
