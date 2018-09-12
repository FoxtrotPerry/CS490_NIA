Caleb Perry 9/10/2018

Commands to run:
g++ assignment1.cpp;./a.out

Captain's Log:

- Random start was initiated with a random 32 bit float with 15 bits of randomness.
- Initial step used was 0.1f and was totally randomly selected in terms of direction.
    - In terms of value, however, the value 0.1f was arbitrarily selected based off
      of multiple prior test results.
- Localized Random Search was used so an adaptive step was not implemented, therefore,
  the algorithm decided it was done when fitness was found to be worse at each step around it.
  At which point, all subsequent steps are not taken and the best fit is chosen to be printed.

Best scores:
- Dimensions:
    - 1:
      - 1000:
          Dimension 0 Value: -0.0163256
          Best Found Fit: 0.825145
      - 10000:
          Dimension 0 Value: -0.000546716
          Best Found Fit: 0.840924
      - 100000:
          Dimension 0 Value: -0.00204911
          Best Found Fit: 0.839422
    - 2:
      - 1000:
          Dimension 0 Value: -9.92832
          Dimension 1 Value: 0.997425
          Best Found Fit: 0.837502
      - 10000: 
          Dimension 0 Value: -0.146018
          Dimension 1 Value: 1
          Best Found Fit: 0.841471
      - 100000: 
          Dimension 0 Value: -7.58496
          Dimension 1 Value: 0.999906
          Best Found Fit: 0.841326
    - 3:
      - 1000:
          Dimension 0 Value: -7.15062
          Dimension 1 Value: -4.69607
          Dimension 2 Value: -1.43663
          Best Found Fit: 0.317497
      - 10000:
          Dimmension 0 Value: 3.24833
          Dimmension 1 Value: -4.33838
          Dimmension 2 Value: -2.92684
          Best Found Fit: -0.17006
      - 100000:
          Dimmension 0 Value: -0.635942
          Dimmension 1 Value: -1.66938
          Dimmension 2 Value: -2.94998
          Best Found Fit: -0.288795
    - 5:
      - 1000:
          Dimmension 0 Value: 5.09371
          Dimmension 1 Value: -5.17814
          Dimmension 2 Value: 0.226811
          Dimmension 3 Value: -2.56202
          Dimmension 4 Value: -0.000152115
          Best Found Fit: -0.000152115
      - 10000:
          Dimmension 0 Value: -3.30808
          Dimmension 1 Value: 4.57803
          Dimmension 2 Value: -5.23067
          Dimmension 3 Value: -1.64314
          Dimmension 4 Value: 1.66898
          Best Found Fit: -0.673491
      - 100000:
          Dimmension 0 Value: -3.76726
          Dimmension 1 Value: -0.0619425
          Dimmension 2 Value: 2.27025
          Dimmension 3 Value: -1.10529
          Dimmension 4 Value: -1.10553
          Best Found Fit: -0.108496
    - 8:
      - 1000:
          Dimension 0 Value: -0.183916
          Dimension 1 Value: 5.71001
          Dimension 2 Value: -5.31142
          Dimension 3 Value: 0.466235
          Dimension 4 Value: 3.48064
          Dimension 5 Value: 1.8966
          Dimension 6 Value: 3.70292
          Dimension 7 Value: 3.00389
          Best Found Fit: 0.995909
      - 10000:
          Dimension 0 Value: -6.16763
          Dimension 1 Value: 4.28755
          Dimension 2 Value: -9.45623
          Dimension 3 Value: 2.73025
          Dimension 4 Value: -3.50062
          Dimension 5 Value: 3.89479
          Dimension 6 Value: 3.8298
          Dimension 7 Value: 2.98395
          Best Found Fit: 0.983412
      - 100000:
          Dimension 0 Value: -4.17228
          Dimension 1 Value: -6.15327
          Dimension 2 Value: -8.53545
          Dimension 3 Value: -1.14595
          Dimension 4 Value: 1.14692
          Dimension 5 Value: -6.0063
          Dimension 6 Value: -1.75468
          Dimension 7 Value: 2.98013
          Best Found Fit: 0.979968
    - 13:
      - 1000:
          Dimension 0 Value: -7.50647
          Dimension 1 Value: -7.48479
          Dimension 2 Value: -5.83003
          Dimension 3 Value: 0.370457
          Dimension 4 Value: -6.99663
          Dimension 5 Value: -6.75203
          Dimension 6 Value: -4.08101
          Dimension 7 Value: 2.94944
          Dimension 8 Value: -6.47379
          Dimension 9 Value: 1.35781
          Dimension 10 Value: -10.4604
          Dimension 11 Value: 0.867955
          Dimension 12 Value: 1.18444
          Best Found Fit: -0.21089
      - 10000:
          Dimension 0 Value: 4.14888
          Dimension 1 Value: -4.52774
          Dimension 2 Value: -5.34418
          Dimension 3 Value: -10.65
          Dimension 4 Value: -6.38688
          Dimension 5 Value: 1.81586
          Dimension 6 Value: -7.33109
          Dimension 7 Value: -6.65704
          Dimension 8 Value: 0.31365
          Dimension 9 Value: 4.45202
          Dimension 10 Value: -9.76612
          Dimension 11 Value: -2.64935
          Dimension 12 Value: 1.18584
          Best Found Fit: -0.193255
      - 100000:
          Dimension 0 Value: -8.33231
          Dimension 1 Value: 3.39737
          Dimension 2 Value: 4.64958
          Dimension 3 Value: -4.97582
          Dimension 4 Value: 1.8376
          Dimension 5 Value: -9.43748
          Dimension 6 Value: -0.139233
          Dimension 7 Value: 4.93678
          Dimension 8 Value: 2.9294
          Dimension 9 Value: 5.11117
          Dimension 10 Value: 3.25617
          Dimension 11 Value: -1.50132
          Dimension 12 Value: 1.18645
          Best Found Fit: -0.189172

  
