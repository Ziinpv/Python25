### README: Giới thiệu môn học Python và các ứng dụng mẫu

---

## **Giới thiệu môn học Python**
Python là một ngôn ngữ lập trình đa năng, dễ học và mạnh mẽ, được sử dụng rộng rãi trong nhiều lĩnh vực như phát triển web, phân tích dữ liệu, trí tuệ nhân tạo, tự động hóa và nhiều hơn nữa. Môn học này giúp bạn làm quen với các khái niệm cơ bản và nâng cao của Python, đồng thời thực hành thông qua các dự án thực tế.

---

## **Ứng dụng To-Do List sử dụng Tkinter**

### **Giới thiệu**
Ứng dụng To-Do List là một công cụ quản lý công việc đơn giản, giúp người dùng ghi chú, theo dõi và hoàn thành các nhiệm vụ hàng ngày. Ứng dụng này được xây dựng bằng thư viện Tkinter của Python, cung cấp giao diện đồ họa dễ sử dụng.

### **Tính năng chính**
- Thêm công việc mới.
- Đánh dấu công việc đã hoàn thành.
- Xóa công việc khỏi danh sách.
- Lưu danh sách công việc vào file để sử dụng sau.

### **Cách sử dụng**
1. Chạy chương trình bằng lệnh:
   ```bash
   python todo_list.py
   ```
2. Nhập công việc vào ô và nhấn "Add" để thêm vào danh sách.
3. Nhấn "Complete" để đánh dấu công việc đã hoàn thành.
4. Nhấn "Delete" để xóa công việc khỏi danh sách.

---

## **Ứng dụng Tự động tải video từ YouTube sử dụng yt-dlp + Tkinter**

### **Giới thiệu**
Ứng dụng này cho phép người dùng tải video từ YouTube một cách tự động và dễ dàng. Nó sử dụng thư viện `yt-dlp` để tải video và `Tkinter` để tạo giao diện người dùng thân thiện.

### **Tính năng chính**
- Tải video từ URL YouTube.
- Hỗ trợ tải video ở nhiều định dạng (MP4, MP3, v.v.).
- Hiển thị tiến trình tải video.

### **Hướng dẫn cài đặt**
1. Cài đặt các thư viện cần thiết:
   ```bash
   pip install yt-dlp tkinter
   ```
2. Cài đặt `ffmpeg` (cần thiết để chuyển đổi định dạng):
   - Tải `ffmpeg` từ trang chủ: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html).
   - Giải nén và thêm đường dẫn đến thư mục chứa `ffmpeg` vào biến môi trường `PATH`.

### **Cách sử dụng**
1. Chạy chương trình bằng lệnh:
   ```bash
   python youtube_downloader.py
   ```
2. Nhập URL video YouTube vào ô và chọn định dạng tải (MP4 hoặc MP3).
3. Nhấn "Download" để bắt đầu tải video.
4. Tiến trình tải sẽ được hiển thị trong cửa sổ chương trình.

---

## **Hướng dẫn chi tiết**

### **Cài đặt ffmpeg**
1. Truy cập trang chủ [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html) và tải phiên bản phù hợp với hệ điều hành của bạn.
2. Giải nén file tải về.
3. Thêm đường dẫn đến thư mục chứa `ffmpeg` vào biến môi trường `PATH`:
   - **Windows**:
     - Mở "System Properties" > "Environment Variables".
     - Tìm biến `Path` trong phần "System variables" và thêm đường dẫn đến thư mục chứa `ffmpeg`.
   - **macOS/Linux**:
     - Mở terminal và thêm dòng sau vào file `~/.bashrc` hoặc `~/.zshrc`:
       ```bash
       export PATH="$PATH:/đường/dẫn/đến/ffmpeg"
       ```
     - Chạy lệnh `source ~/.bashrc` hoặc `source ~/.zshrc` để áp dụng thay đổi.

### **Cài đặt yt-dlp**
- Cài đặt `yt-dlp` bằng lệnh:
  ```bash
  pip install yt-dlp
  ```

---

## **Kết luận**
Các ứng dụng trên là ví dụ minh họa về cách sử dụng Python để xây dựng các công cụ hữu ích trong cuộc sống hàng ngày. Qua môn học này, bạn sẽ nắm vững kiến thức lập trình Python và có thể tự mình phát triển các ứng dụng tương tự hoặc phức tạp hơn.

Chúc bạn học tập và làm việc hiệu quả với Python! 🚀
