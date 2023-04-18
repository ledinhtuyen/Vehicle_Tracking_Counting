import cv2

# Mở video
video = cv2.VideoCapture('video_test/test4.mp4')

# Lấy kích thước khung hình gốc
fps = int(video.get(cv2.CAP_PROP_FPS))
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Khởi tạo VideoWriter để ghi video mới
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('video_test/test4_360p.mp4', fourcc, fps, (640, 360))

# Đọc từng khung hình của video gốc và resize về kích thước mới
while True:
    ret, frame = video.read()
    if not ret:
        break
    
    resized_frame = cv2.resize(frame, (640, 360))
    
    # Ghi khung hình đã được resize vào video mới
    out.write(resized_frame)

# Giải phóng tài nguyên
video.release()
out.release()
cv2.destroyAllWindows()