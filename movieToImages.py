import cv2

fileName = 'suzy'

cap = cv2.VideoCapture('mov/'+fileName+'.mp4')
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


num = 0 

while(cap.isOpened()):
    ret, frame = cap.read() 
    if ret:
        # cv2.imshow('frame', frame)
        #이미지의 각 이름을 자동으로 지정
        path = 'snapshot/'+fileName+'_' + str(num) + '.jpg'
        print("path",path)
        cv2.imwrite(path, frame) #영상 -> 이미지로 저장 
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
    num += 1
        
cap.release()
cv2.destroyAllWindows()