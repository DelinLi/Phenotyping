### installation on OS
1. Opencv along with OpenCV contrib [source](https://www.webuildinternet.com/2016/05/30/installing-opencv-contrib-on-osx/)
<pre>
pip3 install opencv-contrib-python
</pre>
<pre>
git clone https://github.com/Itseez/opencv.git --depth=1
git clone https://github.com/Itseez/opencv_contrib --depth=1
cd opencv
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
      -D CMAKE_INSTALL_PREFIX=/usr/local \
      -D PYTHON_DEFAULT_EXECUTABLE=python3 \
      -D WITH_TBB=ON \
      -D BUILD_NEW_PYTHON_SUPPORT=ON \
      -D WITH_V4L=ON \
      -D WITH_OPENGL=ON \
      -D INSTALL_C_EXAMPLES=OFF \
      -D OPENCV_ENABLE_NONFREE=ON \
      -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules
make -j4
sudo make install
</pre>
