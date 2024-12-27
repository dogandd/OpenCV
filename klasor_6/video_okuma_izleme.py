import cv2

# videoyu bilgisayarın kamerasından alacaksak 0 başka cihazdan alıcaksak ona göre numaralandırılır 1 2 3 şeklinde devam eder
# yüklü bir video için videonun adresi girilir
cap = cv2.VideoCapture("D:\\Videolar\\antalya.mp4")

# videoları bir bütün olarak okuyamadığı için while döngüsüyle tek tek kareleri inceleriz
while True:
    # read iki değer döndürür biri dogru okumasına bağlı true/false diğeri frameleri dödürür
    ret , frame = cap.read()
    # video bittiği zaman döngüden çıksın diye break eklendi
    if ret == 0:
        break
    # flip fonksiyonunda görüntüyü y eksenine göre ters almak için 1 değeri girildi
    frame = cv2.flip(frame , 1)
    cv2.imshow("Webcam", frame)
    # q tuşuna basınca ekranı kapatması için aşağıdaki if yapısı kullanıldı
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

cap.release() 
cv2.destroyAllWindows()