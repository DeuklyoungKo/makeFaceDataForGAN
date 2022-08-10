import cv2
import os
from PIL import Image


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)



def videoToImages(fileName):

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

    createFolder('.\\snapshot\\'+fileName)

    num = 0
    cnt = 0
    skipNum = 10
    while(cnt < count):
        ret, frame = cap.read()

        if cnt % skipNum == 0:

            if ret:
                # cv2.imshow('frame', frame)
                #이미지의 각 이름을 자동으로 지정
                path = 'snapshot/'+fileName+'/' + str(num) + '.jpg'
                print("path",path)
                cv2.imwrite(path, frame) #영상 -> 이미지로 저장 
                if cv2.waitKey(1) & 0xFF == ord('q'): 
                    break
            num += 1

        cnt += 1

    cap.release()
    cv2.destroyAllWindows()
    return num


## 얼굴 영역 별도 파일로 저장
def saveFaceImgaes(num):

    cnt = 1
    cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") # 정면 얼굴 인식 모델
    createFolder('.\\face\\'+fileName)
    for i in range(num):
        print(i)

        imageUrl = 'snapshot/'+fileName+'/' + str(i) + '.jpg'

        #검출하기
        img = cv2.imread(imageUrl) #읽기
        imagePIL = Image.open(imageUrl)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #흑백변환 
        face_list = cascade.detectMultiScale(gray, minNeighbors=5, minSize = (20,20)) #얼굴검출
        print("face_list:",face_list)

        for (x, y, w, h) in face_list:
            color = (0, 0, 225) #색 - red 
            pen_w = 3 #선굵기 
            cv2.rectangle(img, (x, y), (x+w, y+h), color, thickness = pen_w) #정면얼굴에 사각형을 그려!
            
            padding_x = 0.5*w
            padding_Y = 0.5*h

            # 이미지 자르기 crop함수 이용 ex. crop(left,up, rigth, down)
            croppedImage=imagePIL.crop((x-padding_x, y-padding_Y, x+w+padding_x, y+h+padding_Y))
            # croppedImage.show()

            croppedImage.save('./face/'+fileName+'/'+str(cnt)+'.png')
            cnt +=1

        cv2.waitKey(1000)
        cv2.destroyAllWindows()



# fileName = 'suzy'
# fileName = 'jihyun'
fileName = 'taehee'
imgCount = videoToImages(fileName)
saveFaceImgaes(imgCount)
