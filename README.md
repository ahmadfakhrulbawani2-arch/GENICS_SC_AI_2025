Running program instruction (Windows 8 or newer only):
0. Make a virtual environment (venv) & Library Setup:
    - Open your Command Prompt or terminal
    - Open the directory you want to create the venv
    - Write: py -m venv .venv
    - Then write: 
                    venv\Scripts\activate
                    
    You can also use VSCode terminal but I recommend use the default terminal you have.
    For library we use OpenCV:
    - Connect your device to internet
    - Open your Command Prompt
    - Open your system folder (i.e C:\ partition)
    - Write: 
                    py -m pip install opencv-python

    - Wait the installation process, this will take a while
    You can also install in another directory, but I recommend it in system partition.

1. Copy paste everything in main.py
2. If you want to change or customize the program, You can customize according to my comment line
3. Copy everything in training-code.xml. It's open source you can find all version here: https://github.com/opencv/opencv/tree/master/data/haarcascades
4. Change The reference of training-code.xml (if you save in the same folder of main.py you can leave it as is).
5. To run open VSCode Terminal or your default terminal. Make sure you open the main.py folder! Then write: 
                    py main.py

In case if you get this error:

[ WARN:0@5.441] global cap_msmf.cpp:488 `anonymous-namespace'::SourceReaderCB::OnReadSample videoio(MSMF): async ReadSample() call is failed with error status: -1072875772
[ WARN:1@5.441] global cap_msmf.cpp:1795 CvCapture_MSMF::grabFrame videoio(MSMF): can't grab frame. Error: -1072875772
Traceback (most recent call last):
  File "D:\AI - PROJECT GWEH\GENICS_SC_AI_2025\main.py", line 40, in <module>
    main()
    ~~~~^^
  File "D:\AI - PROJECT GWEH\GENICS_SC_AI_2025\main.py", line 33, in main
    drawer_box(frame)
    ~~~~~~~~~~^^^^^^^
  File "D:\AI - PROJECT GWEH\GENICS_SC_AI_2025\main.py", line 12, in drawer_box
    for x, y, w, h in face_detection(frame):
                      ~~~~~~~~~~~~~~^^^^^^^
  File "D:\AI - PROJECT GWEH\GENICS_SC_AI_2025\main.py", line 7, in face_detection
    optimize_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
cv2.error: OpenCV(4.12.0) D:\a\opencv-python\opencv-python\opencv\modules\imgproc\src\color.cpp:199: error: (-215:Assertion failed) !_src.empty() in function 'cv::cvtColor'

Don't worry it means your device default camera is used in other device. (Make sure your device have / connected to camera)