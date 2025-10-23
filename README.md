Running program instruction:
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