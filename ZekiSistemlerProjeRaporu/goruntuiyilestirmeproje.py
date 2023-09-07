import numpy as np
import cv2
from matplotlib.image import imread

goruntu=cv2.imread("goruntu adi.jpg").copy() #görüntüyü mutable yapmak için copy()
#iyileştirmek istediğiniz görüntüyü programın olduğu klasöre ekleyip, görüntünün adını "goruntu adi.jpg" kısmına uzantısıyla birlikte yazmanız gerekiyor.
#program çalıştığında görüntünün iyileştirilmiş hali klasörde "son goruntu.jpg" adıyla oluşacak.
cv2.imwrite("goruntu.jpg", goruntu)

genislik=int(goruntu.shape[1]*3)
yukseklik=int(goruntu.shape[0]*3)
boyut=(genislik,yukseklik)
resized=cv2.resize(goruntu,boyut,interpolation = cv2.INTER_AREA) #görüntünün çözünürlüğü 3 katına çıktı

cv2.imwrite("resized.jpg", resized)
imgout=np.asfarray(resized) #elemanlar float oldu
cv2.imwrite("resized2.jpg", resized)

satirsayisi=imgout.shape[0]-1 #satır ve sütundaki son elamanlar
sutunsayisi=imgout.shape[1]-1  

def iyilestir(satir,sutun):
    
   for x in range(sutunsayisi):
      
      if sutun+3>sutunsayisi:
         break
      
      else:
         imgout[satir,sutun+1]=imgout[satir,sutun]*0.666 +imgout[satir,sutun+3]*0.333
         
         imgout[satir,sutun+2]=imgout[satir,sutun]*0.333 +imgout[satir,sutun+3]*0.666
         
         imgout[satir+1,sutun]=imgout[satir,sutun]*0.666 +imgout[satir+3,sutun]*0.333
         
         imgout[satir+2,sutun]=imgout[satir,sutun]*0.333 +imgout[satir+3,sutun]*0.666
         
         imgout[satir+1,sutun+1]=imgout[satir,sutun]*0.362 +imgout[satir,sutun+3]*0.229+imgout[satir+3,sutun]*0.229 +imgout[satir+3,sutun+3]*0.181
         
         imgout[satir+1,sutun+2]=imgout[satir,sutun+3]*0.362 +imgout[satir,sutun]*0.229+imgout[satir+3,sutun+3]*0.229 +imgout[satir+3,sutun]*0.181
         
         imgout[satir+2,sutun+1]=imgout[satir+3,sutun]*0.362 +imgout[satir,sutun]*0.229+imgout[satir+3,sutun+3]*0.229 +imgout[satir,sutun+3]*0.181
         
         imgout[satir+2,sutun+2]=imgout[satir+3,sutun+3]*0.362 +imgout[satir+3,sutun]*0.229+imgout[satir,sutun+3]*0.229 +imgout[satir,sutun]*0.181
      
         sutun=sutun+3
   
for i in range(0,satirsayisi,3):
   
   if i+3>=satirsayisi:
      break
   
   else:
      iyilestir(i,0)

print(imgout.shape)
img=cv2.imwrite("son goruntu.jpg", imgout)