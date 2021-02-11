# Huffman-Encoder-And-Decoder
Algorithm that compresses input text with Huffman encoding and decodes back.

## Açıklama [TR]

İstenilen metne göre dinamik bir huffman kodlama şeması oluşturmayı hedefleyen bu kodun algoritma akışı yüzeysel olarak şu şekilde ilerlemektedir:<br>
Kullanıcıdan girdi alınır, büyük harflerin hepsi küçük harflere dönüştürülür.<br>
Girdi mesajında kullanılan her bir harf bir kereliğine char_list listesine yazılır. Bu listedeki karakterlerin kullanım sayısını belirtecek şekilde bir charCount listesi bu liste ile hizalanır, aynı dönüşümleri geçirir.<br>
Karar matrisi denilen yapıyı oluşturmak için, iki boyutlu bir charList2 listesi oluşturulur. İlk etapta tüm karakterler bu listenin ilk sırasına (row 0) hizalanır.<br> Matrisin sondan önceki iki sütunu (column), (her for döngüsünde bubble sorting algoritması ile charList2 ve charCount listeleri büyükten küçüğe sıralandığı için) her zaman en küçük tekrar sayısına sahip olan karakterleri barındırır. Bu iki sütundaki karakterler toplanıp charList2 listesinin bir solundaki sütuna yukarıdan aşağı sıralanacak şekilde tekrar yazılır ve charCount listesindeki değerleri de yine charList2 listesine izdüşecek şekilde toplanır ve hizalanır. charList2 listesinde tek bir sütun kalana kadar bu işlem devam eder. Bütün karakterler ilk sütuna toplandığında karar matrisi işlemleri bitmiş olur.<br>
Karakterlerin charList2 içerisinde toplanması işleminden önce encodeChar listesinde karakterler, ve encodeValue listesinde ise bunlara izdüşecek ve karar matrisi hesaplaması sırasında yerleştirilmiş 0 ve 1 bitlerinden oluşan değerleri bulunacaktır. charList2 listesi her döngüde işleme sokulurken işleme sokulacak en küçük iki sütundan sağdaki sütundaki karakterlere 0 biti eklenir, soldaki sütundaki karakterlere ise 1 değeri eklenir. Karar matrisi işlemi bitene kadar bu işlem devam eder ve en sonunda her bir karakterin kendine özel dengelenmiş, huffman şifreleme ile sıkıştırılmış bit değerleri ortaya çıkar.
