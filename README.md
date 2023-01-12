# Collatz-C
> Das Collatz-Problem, auch als (3n+1)-Vermutung bezeichnet, ist ein ungelöstes mathematisches Problem, das 1937 von Lothar Collatz gestellt wurde. 

> Es hat Verbindungen zur Zahlentheorie, zur Theorie dynamischer Systeme und Ergodentheorie und zur Theorie der Berechenbarkeit in der Informatik.

> Das Problem gilt als notorisch schwierig, obwohl es einfach zu formulieren ist. Jeffrey Lagarias, der als Experte für das Problem gilt, zitiert eine mündliche Mitteilung von Paul Erdős, der es als „absolut hoffnungslos“ bezeichnete.[1] 

[Collatz-Wikipedia](https://de.wikipedia.org/wiki/Collatz-Problem)

## Overview

Investigation of the Collatz problem for regularities. The paper was written in German and has gross syntax errors in some sentence formation, since the written paper was mostly edited in the library after 10 pm during the exam period.

The [paper](qwertz.pdf) was written in latex and is in the same project

## Additional scripts

### SieveCollatz.py

The file SieveCollatz.py works similar to the Sieve of Eratosthenes.
Here all numbers are filtered on the basis of the elaborated realizations, in the same way as with the sieve of the Eratosthenes


<b>Sieve of Eratosthenes</b><br>
![df](https://upload.wikimedia.org/wikipedia/commons/5/5e/Animation_Sieb_des_Eratosthenes_%C3%9Cberarbeitet.gif)
<br><br>
<b>Sieve Collatz</b><br>

```
[]
  1   2   3   4   5   6   7   8   9  10 
 11  12  13  14  15  16  17  18  19  20 
 21  22  23  24  25  26  27  28  29  30 
 31  32  33  34  35  36  37  38  39  40 
 41  42  43  44  45  46  47  48  49  50 
 51  52  53  54  55  56  57  58  59  60 
 61  62  63  64  65  66  67  68  69  70 
 71  72  73  74  75  76  77  78  79  80 
 81  82  83  84  85  86  87  88  89  90 
 91  92  93  94  95  96  97  98  99  100 

[1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 64.0, 128.0]
          3       5   6   7       9  10 
 11  12  13  14  15      17  18  19  20 
 21  22  23  24  25  26  27  28  29  30 
 31      33  34  35  36  37  38  39  40 
 41  42  43  44  45  46  47  48  49  50 
 51  52  53  54  55  56  57  58  59  60 
 61  62  63      65  66  67  68  69  70 
 71  72  73  74  75  76  77  78  79  80 
 81  82  83  84  85  86  87  88  89  90 
 91  92  93  94  95  96  97  98  99  100 

[5.0, 10.0, 20.0, 40.0, 80.0, 160.0, 320.0, 640.0]
          3           6   7       9     
 11  12  13  14  15      17  18  19     
 21  22  23  24  25  26  27  28  29  30 
 31      33  34  35  36  37  38  39     
 41  42  43  44  45  46  47  48  49  50 
 51  52  53  54  55  56  57  58  59  60 
 61  62  63      65  66  67  68  69  70 
 71  72  73  74  75  76  77  78  79     
 81  82  83  84  85  86  87  88  89  90 
 91  92  93  94  95  96  97  98  99  100 

[...] #Cutout for good reasons

[267605.0, 535210.0, 1070420.0, 2140840.0, 4281680.0, 8563360.0, 17126720.0, 34253440.0]
                                        
                 15                     
         23              27          30 
 31              35              39     
 41      43          46  47             
 51          54  55      57      59  60 
 61  62  63              67          70 
 71      73      75          78  79     
 81  82  83          86  87      89     
 91  92  93  94  95      97      99     

```

### TraceCollatz.py

Determines the shortest path to any selected number 

<b>37</b><br>
[37, 37.0, 112.0, 7.0, 22.0, 11.0, 34.0, 17.0, 52.0, 13.0, 40.0, 5.0, 16.0]<br>

<b>3</b><br>
[3, 3.0, 10.0, 5.0, 16.0]<br>

<b>7</b><br>
[7, 7.0, 22.0, 11.0, 34.0, 17.0, 52.0, 13.0, 40.0, 5.0, 16.0]<br>

<b>20</b><br>
[20, 5.0, 16.0]<br>

<b>30</b><br>
[30, 15.0, 46.0, 23.0, 70.0, 35.0, 106.0, 53.0, 160.0, 5.0, 16.0]<br>

### NewCollatz.py

The file NewCollatz.py, works on the last proven state of knowledge us every series that can be calculated with the function f<sup>-1</sup>(n). Here our script terminates after a certain valence, currently defined in the paper are 50.

```
0 []
0 [1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 64.0, 128.0]
1 [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
1 [5.0, 10.0, 20.0, 40.0, 80.0, 160.0, 320.0, 640.0]
1 [21.0, 42.0, 84.0, 168.0, 336.0, 672.0, 1344.0, 2688.0]
1 [85.0, 170.0, 340.0, 680.0, 1360.0, 2720.0, 5440.0, 10880.0]
1 [341.0, 682.0, 1364.0, 2728.0, 5456.0, 10912.0, 21824.0, 43648.0]
2 [3.0, 6.0, 12.0, 24.0, 48.0, 96.0, 192.0, 384.0]
2 [13.0, 26.0, 52.0, 104.0, 208.0, 416.0, 832.0, 1664.0]
2 [53.0, 106.0, 212.0, 424.0, 848.0, 1696.0, 3392.0, 6784.0]
2 [213.0, 426.0, 852.0, 1704.0, 3408.0, 6816.0, 13632.0, 27264.0]
3 [17.0, 34.0, 68.0, 136.0, 272.0, 544.0, 1088.0, 2176.0]
3 [69.0, 138.0, 276.0, 552.0, 1104.0, 2208.0, 4416.0, 8832.0]
3 [277.0, 554.0, 1108.0, 2216.0, 4432.0, 8864.0, 17728.0, 35456.0]
4 [11.0, 22.0, 44.0, 88.0, 176.0, 352.0, 704.0, 1408.0]
4 [45.0, 90.0, 180.0, 360.0, 720.0, 1440.0, 2880.0, 5760.0]
4 [181.0, 362.0, 724.0, 1448.0, 2896.0, 5792.0, 11584.0, 23168.0]
5 [7.0, 14.0, 28.0, 56.0, 112.0, 224.0, 448.0, 896.0]
5 [29.0, 58.0, 116.0, 232.0, 464.0, 928.0, 1856.0, 3712.0]
5 [117.0, 234.0, 468.0, 936.0, 1872.0, 3744.0, 7488.0, 14976.0]
5 [469.0, 938.0, 1876.0, 3752.0, 7504.0, 15008.0, 30016.0, 60032.0]
6 [9.0, 18.0, 36.0, 72.0, 144.0, 288.0, 576.0, 1152.0]
6 [19.0, 38.0, 76.0, 152.0, 304.0, 608.0, 1216.0, 2432.0]
6 [37.0, 74.0, 148.0, 296.0, 592.0, 1184.0, 2368.0, 4736.0]
6 [77.0, 154.0, 308.0, 616.0, 1232.0, 2464.0, 4928.0, 9856.0]
6 [149.0, 298.0, 596.0, 1192.0, 2384.0, 4768.0, 9536.0, 19072.0]
6 [309.0, 618.0, 1236.0, 2472.0, 4944.0, 9888.0, 19776.0, 39552.0]
7 [25.0, 50.0, 100.0, 200.0, 400.0, 800.0, 1600.0, 3200.0]
7 [49.0, 98.0, 196.0, 392.0, 784.0, 1568.0, 3136.0, 6272.0]
7 [101.0, 202.0, 404.0, 808.0, 1616.0, 3232.0, 6464.0, 12928.0]
7 [197.0, 394.0, 788.0, 1576.0, 3152.0, 6304.0, 12608.0, 25216.0]
7 [405.0, 810.0, 1620.0, 3240.0, 6480.0, 12960.0, 25920.0, 51840.0]
8 [33.0, 66.0, 132.0, 264.0, 528.0, 1056.0, 2112.0, 4224.0]
8 [65.0, 130.0, 260.0, 520.0, 1040.0, 2080.0, 4160.0, 8320.0]
8 [133.0, 266.0, 532.0, 1064.0, 2128.0, 4256.0, 8512.0, 17024.0]
8 [261.0, 522.0, 1044.0, 2088.0, 4176.0, 8352.0, 16704.0, 33408.0]
```

---
![Image](CharlesGiraud.jpg)
