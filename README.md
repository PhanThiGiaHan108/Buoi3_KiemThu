# Python Bài Tập Kiểm Thử

Dự án này gồm các hàm Python đơn giản và bộ kiểm thử bằng `pytest` để xác thực cả dữ liệu hợp lệ và không hợp lệ.

## Cấu trúc thư mục

- `src/`: chứa các hàm xử lý
- `tests/`: chứa các file kiểm thử bằng `pytest`
- `testcases/`: mô tả dữ liệu kiểm thử hợp lệ và không hợp lệ
- `results/`: chứa kết quả chạy kiểm thử

## Các chức năng chính

- Chu vi hình chữ nhật
- Diện tích hình chữ nhật
- Giải phương trình bậc 2
- Tính số ngày trong tháng
- Kiểm tra số nguyên tố
- Tính tổng xen kẽ
- Tìm UCLN
- Tính tổng giai thừa

## Yêu cầu

- Python 3.x
- `pytest`

Cài `pytest` nếu máy chưa có:

```powershell
python -m pip install pytest
```

## Cách chạy kiểm thử

Chạy toàn bộ test:

```powershell
python -m pytest
```

Chạy và lưu kết quả ra file:

```powershell
python -m pytest > results/output.txt
```

Chạy từng file test:

```powershell
python -m pytest tests/test_valid.py
python -m pytest tests/test_invalid.py
```

## Kết quả mong đợi

Nếu mọi thứ đúng, `pytest` sẽ báo tất cả test đều pass, ví dụ:

```text
16 passed
```
