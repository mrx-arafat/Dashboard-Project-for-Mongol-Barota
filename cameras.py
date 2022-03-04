import cv2

def stream_cam_1():
    cam = cv2.VideoCapture(0)
    while 1 :
        try:
            check,frame = cam.read()
            if(check):
                imgencode = cv2.imencode('.jpg',frame)[1]
                strinData = imgencode.tostring()
                yield (b'--frame\r\n'b'Content-Type: text/plain\r\n\r\n'+strinData+b'\r\n')
        except:
            cam.release()
            break
    return 'Closed'

def stream_cam_1():
    cam = cv2.VideoCapture(0)
    while 1 :
        try:
            check,frame = cam.read()
            if(check):
                imgencode = cv2.imencode('.jpg',frame)[1]
                strinData = imgencode.tostring()
                yield (b'--frame\r\n'b'Content-Type: text/plain\r\n\r\n'+strinData+b'\r\n')
        except:
            cam.release()
            break
    return 'Closed'
        