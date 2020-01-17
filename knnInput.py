import random
import math
import matplotlib.pyplot as plot

# random sayı oluşturmak için kullanılır
def createRandom(point1, point2):
    randomValueHolder= 0;
    for i in range(10):
        randomValueHolder = random.randint(point1,point2)
    return randomValueHolder

#verilen x,y ikilileri arasındaki mesafeyi hesaplar.
def calculateDistanceForEach(pointList, createdPoint):
    distance = 0;
    distanceHolder = 0; 
    for i in range(len(pointList)):
         distance += math.pow((pointList[i] - createdPoint[i]),2)
    distanceHolder = math.sqrt(distance)
    return distanceHolder

# default tanımlamalar.
plot.axis([0,150, 0, 150])
bound = 15
listPointYellow = list();
listPointRed = list();
listPointBlue = list();
listPointMagenta = list();

# her bir renk için random x,y koordinatları oluşturur.
for i in range(bound):
    listPointYellow.append([createRandom(10,40),createRandom(25,55)])
    listPointRed.append([createRandom(10,40),createRandom(95,125)])
    listPointBlue.append([createRandom(90,120),createRandom(25,55)])
    listPointMagenta.append([createRandom(90,120),createRandom(95,125)])

# her bir renk için oluşturulmuş olan koordinatları plota çevirir.
for i in range(bound):
    plot.plot(listPointYellow[i][0], listPointYellow[i][1], 'yo')
    plot.plot(listPointRed[i][0], listPointRed[i][1], 'ro')
    plot.plot(listPointBlue[i][0], listPointBlue[i][1], 'bo')
    plot.plot(listPointMagenta[i][0], listPointMagenta[i][1], 'mo')
    
# kullanıcıdan x,y koordinatları ve KNN'deki k değişkenini ister. Verilen değerlere göre noktayı oluşturur.    
x = int(input("x: "))
y = int(input("y: "))
k = int(input("k: "))

randomPoint = list()
randomPoint = [x,y]
plot.plot(randomPoint[0],randomPoint[1],'ko')

distanceAllYellow= list()
distanceAllRed = list()
distanceAllBlue = list() 
distanceAllMagenta = list()

# oluşturulan noktanın her farklı renk dataları için mesafesini hesaplar.
for i in range(bound):
    distanceAllYellow.append(calculateDistanceForEach(listPointYellow[i],randomPoint))
    distanceAllRed.append(calculateDistanceForEach(listPointRed[i],randomPoint))
    distanceAllBlue.append(calculateDistanceForEach(listPointBlue[i],randomPoint))
    distanceAllMagenta.append(calculateDistanceForEach(listPointMagenta[i],randomPoint))

distanceHolder = list();

# bu mesafeleri tek bir listeye atar.
for i in range(bound):
        distanceHolder.append([calculateDistanceForEach(listPointYellow[i],randomPoint),'sarı'])
        distanceHolder.append([calculateDistanceForEach(listPointRed[i],randomPoint),'kırmızı'])
        distanceHolder.append([calculateDistanceForEach(listPointBlue[i],randomPoint),'mavi'])
        distanceHolder.append([calculateDistanceForEach(listPointMagenta[i],randomPoint),'mor'])

# alınan k değişkeni kadar minimum mesafe döndürür.
listTempDistanceHolder = distanceHolder
listKNN = list()
for i in range(k):
    listKNN.append(min(listTempDistanceHolder))
    listTempDistanceHolder.remove(min(listTempDistanceHolder))

# grubu belirlemek için renkler listeye alınır.    
listMaxFrequency = list();
for i in range(len(listKNN)):
    listMaxFrequency.append(listKNN[i][1])

# tekrarlar hesaplanıp ait olduğu grup ekrana bastırılır.
for i in range(k):
    print("Uzaklık: %s br \t renk: %s" % (listKNN[i][0], listKNN[i][1]))
resultKNN = max(listMaxFrequency, key = listMaxFrequency.count) 
print("\n\nAit Olduğu Grup(EN ÇOK TEKRAR): ", resultKNN)

