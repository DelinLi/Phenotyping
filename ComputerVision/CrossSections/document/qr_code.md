## Install qrtools 
	 sudo apt-get install python-qrtools

## You may have error on below:
<pre>
	File "/usr/lib/python2.7/dist-packages/qrtools.py", line 181, in decode raw = pil.tostring()
  File "/usr/lib/python2.7/dist-packages/PIL/Image.py", line 686, in tostring "Please call tobytes() instead.")

This could be fixed with conver 'tostring' to 'tobytes' in line 181. 
</pre>

## Test   
tested with figure format 'png' and 'jpg', figure only with QR code and "QR code + text + CrossSections"


### generate codes -- useless for this project  
install pyqrcode   
pip install pyqrcode   
