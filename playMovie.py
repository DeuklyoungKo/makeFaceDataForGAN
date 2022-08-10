import cv2

cap = cv2.VideoCapture('mov/suzy.mp4')
print("start")

#동영상 정보 
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
fps = cap.get(cv2.CAP_PROP_FPS)

print('가로: ', str(width))
print('세로: ', str(height))
print('총 프레임수: ', str(count))
print('FPS: ' + str(fps))


#동영상 출력 - 실행시 큰 창으로 출력 
while(cap.isOpened()):
    ret, frame = cap.read() #동영상 정보 읽어오기 -read
    if ret:
    #frame은 이미지 정보이므로 imshow 로 읽어들일 수 있음
        cv2.imshow('frame', frame)  
    if cv2.waitKey(17) & 0xFF == ord('q'):   # waitKey(1) : 1frame을 1밀리초 보여줌, exit = 'q'
        break
        
cap.release()
cv2.destroyAllWindows()