RESULTS.md
KẾT QUẢ THỰC NGHIỆM
1. Thông tin chung
Tên project: ImageProcessing_Lab02_PointOps_LinearFilters
Mục tiêu: Thực hiện và kiểm thử các phép xử lý điểm ảnh, bộ lọc
tuyến tính và một số chức năng xử lý ảnh nâng cao.
Các nhóm chức năng hiện có trong project:
- Point Operations
- Linear Filters
- Advanced Processing
- Filter Comparison
- Validation
- Metrics
- Visualization
2. Point Operations
Project hiện có các phép xử lý điểm ảnh:
  Chức năng    File                                   Trạng thái
  Brightness   src/point_operations/brightness.py   Đã triển khai
  Contrast     src/point_operations/contrast.py     Đã triển khai
  Negative     src/point_operations/negative.py     Đã triển khai
  Threshold    src/point_operations/threshold.py    Đã triển khai
Kết quả kiểm thử
Các chức năng Brightness, Contrast, Negative và Threshold đều đã được
kiểm thử.
Kết quả hiện tại:
- Brightness: PASS
- Contrast: PASS
- Negative: PASS
- Threshold: PASS
3. Linear Filters
Project hiện có:
  Bộ lọc                  File                                      Trạng thái
  Mean Filter             src/linear_filters/mean_filter.py       Đã triển khai
  Gaussian Filter         src/linear_filters/gaussian_filter.py   Đã triển khai
  Sharpening              src/linear_filters/sharpening.py        Đã triển khai
Kết quả kiểm thử
Các nội dung được kiểm tra gồm:
- Kích thước ảnh đầu ra
- Kiểu dữ liệu đầu ra
- Khả năng làm mượt ảnh
- Xử lý ảnh có giá trị không đổi
- Khả năng thay đổi ảnh đối với sharpening
Kết quả:
- Mean Filter: PASS
- Gaussian Filter: PASS
- Sharpening: PASS
4. Tổng kết kiểm thử hiện tại
Lệnh kiểm thử đã sử dụng:
python -m pytest src/tests -v
Kết quả thực tế:
28 passed in 0.30s
Tổng cộng:
  Chỉ số           Kết quả
  Tổng số test          28
  PASS                  28
  FAIL                   0
  Tỷ lệ PASS          100%
Các test đã PASS gồm:
- 4 test Brightness
- 4 test Contrast
- 4 test Gaussian Filter
- 4 test Mean Filter
- 4 test Negative
- 4 test Sharpening
- 4 test Threshold
5. Filter Comparison
File:
src/advanced/filter_comparison.py
Hiện đã có các chức năng:
- apply_all_filters()
- compare_blur_filters()
- compare_edge_filters()
- calculate_mean_intensity()
- calculate_std()
- generate_comparison_metrics()
- print_comparison()
- compare_filters()
apply_all_filters() thực hiện so sánh các kết quả:
- Mean
- Gaussian
- Sharpening
- Sobel
- Prewitt
Các hàm comparison cũng hỗ trợ tính:
- Mean intensity
- Standard deviation
Lưu ý: Phần Filter Comparison đã có implementation nhưng tại thời
điểm lập báo cáo chưa có kết quả kiểm thử riêng được xác nhận trong log
pytest 28 test ở trên. Vì vậy không ghi số liệu thực nghiệm chưa được
chạy.
6. Metrics
Project có module:
src/utils/metrics.py
Các chỉ số được triển khai:
- MSE (Mean Squared Error)
- MAE (Mean Absolute Error)
- PSNR (Peak Signal-to-Noise Ratio)
Các chỉ số này được sử dụng để đánh giá sự khác biệt giữa hai ảnh.
Chưa ghi giá trị MSE, MAE hoặc PSNR cụ thể vì chưa có kết quả thực
nghiệm được xác nhận trong log hiện tại.
7. Validation
Project có module:
src/utils/validation.py
Các nội dung kiểm tra gồm:
- Kiểm tra ảnh có phải numpy.ndarray
- Kiểm tra ảnh rỗng
- Kiểm tra số chiều của ảnh
- Kiểm tra kích thước kernel
- Kiểm tra threshold trong khoảng 0--255
- Kiểm tra sigma
- Kiểm tra hai ảnh có cùng kích thước
8. Advanced Processing
Project có các module:
src/advanced/
├── edge_detection.py
├── custom_kernel.py
├── filter_comparison.py
└── nonlinear_filter.py
Các chức năng nâng cao gồm:
- Edge Detection
- Custom Kernel
- Filter Comparison
- Nonlinear Filter
Các module này là phần mở rộng của project sau Point Operations và
Linear Filters.
Chưa ghi kết quả định lượng cho các thuật toán Advanced nếu chưa có
kết quả chạy thực tế.
9. Output
Project hiện đã chạy được src.main và tạo ra các output:
negative.jpg
brightness_plus.jpg
contrast_high.jpg
threshold.jpg
gaussian_blur.jpg
mean_blur.jpg
sharpen.jpg
Các output trên tương ứng với những chức năng cơ bản đã được tích hợp
trong main.py.
10. Nhận xét
Kết quả kiểm thử hiện tại cho thấy các chức năng Point Operations và
Linear Filters cơ bản đang hoạt động ổn định với bộ test hiện có.
Đặc biệt, toàn bộ 28 test hiện tại đều PASS:
28 passed in 0.30s
Phần Advanced đã có mã nguồn triển khai, trong đó filter_comparison.py
đã hỗ trợ chạy nhiều bộ lọc và tạo bảng chỉ số so sánh. Phần này cần
được kiểm thử riêng trước khi kết luận về kết quả thực nghiệm.
11. Hạn chế
- Chưa có đầy đủ số liệu thực nghiệm cho tất cả thuật toán Advanced.
- Chưa có bảng MSE, MAE, PSNR và thời gian xử lý được đo trên cùng một
  tập ảnh.
- Kết quả định lượng chưa được điền nếu chưa thực sự chạy chương
  trình.
- Một số output directory cần được tổ chức lại để thống nhất với cấu
  trúc project mong muốn.
12. Kết luận
Project đã hoàn thành và kiểm thử thành công phần Point Operations và
Linear Filters cơ bản.
Kết quả kiểm thử hiện tại:
28/28 tests PASS
100% PASS
Phần Advanced và Filter Comparison đã có implementation và là phần tiếp
theo cần kiểm thử, tích hợp vào pipeline chính và bổ sung kết quả thực
nghiệm thực tế.
