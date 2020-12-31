import pyautogui
import PySimpleGUI as sg
import cv2
import numpy

def main():
  sg.theme('White')

  layout=[[sg.Text('Camera',size=(40,1),justification='center',font='Helvetica 20')],
      [sg.Image(filename='',key='image')],
      [sg.Button('Record',size=(10,1),font='Arial 14'),
       sg.Button('Stop',size=(10,1),font='Arial 14'),
       sg.Button('Exit',size=(10,1),font='Arial 14'),
       sg.Button('Screenshot',size=(10,1),font='Arial 14')]]

  window=sg.Window('Camera application',layout,location=(800,400))

  cap=cv2.VideoCapture(0)
  recording=False

  while True:
    event,values=window.read(timeout=20)
    if event=='Exit' or event==sg.WIN_CLOSED:
      return

    elif event=='Record':
      recording=True
    elif event=='Screenshot':
      myScreenshot=pyautogui.screenshot()
      myScreenshot.save(r'shot.png')

    elif event=='Stop':
      recording=False
      img=np.full((480,640),255)
      imgbytes=cv2.imencode('.png',img)[1].tobytes()
      window['image'].update(data=imgbytes)

    if recording:
      ret,frame=cap.read()
      imgbytes=cv2.imencode('.png',frame)[1].tobytes()
      window['image'].update(data=imgbytes)
main()
