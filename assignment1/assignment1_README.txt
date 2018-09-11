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
      - 1000: 0.899324
      - 10000: 0.839681
      - 100000: 0.910023
    - 2:
      - 1000: 0.899563
      - 10000: 0.953453
      - 100000: 0.982341
    - 3:
      - 1000: 0.928021
      - 10000: 0.942871
      - 100000: 0.964578
    - 5:
      - 1000: 0.932453
      - 10000: 0.986578
      - 100000: 0.92101
    - 8:
      - 1000: 0.998764
      - 10000: 0.986589
      - 100000: 0.998985
    - 13:
      - 1000: 0.925478
      - 10000:0.932333
      - 100000: 0.981033
  
