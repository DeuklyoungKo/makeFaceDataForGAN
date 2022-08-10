import cv2

#준비
# cascade_file = 'haarcascade_frontalface_alt.xml'
cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") # 정면 얼굴 인식 모델

#검출하기
img = cv2.imread('img/face.jpg') #읽기
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #흑백변환 
face_list = cascade.detectMultiScale(gray, minSize = (50,50)) #얼굴검출

for (x, y, w, h) in face_list:
    color = (0, 0, 225) #색 - red 
    pen_w = 3 #선굵기 
    cv2.rectangle(img, (x, y), (x+w, y+h), color, thickness = pen_w) #정면얼굴에 사각형을 그려!
    
cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.imshow('img', img)
cv2.imwrite('./img/temp.jpg', img) #img 에 사각형 얼굴인식 한것을 'temp' 라는 이름으로 이미지 저장
cv2.waitKey(1000)
cv2.destroyAllWindows()