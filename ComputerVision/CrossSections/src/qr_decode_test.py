#fig="../figures/QR.jpg"
fig="../figures/qr_nosise.png"
import qrtools
qr=qrtools.QR()
qr.decode(fig)
print qr.data
