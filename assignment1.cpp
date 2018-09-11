#include <iostream>
#include <cmath>
#include <memory>
#include <cstdlib>
#include <ctime>

float fitness(int n, const std::unique_ptr<float[]>& x);
float LRS(int iterations, int n);
void step(const std::unique_ptr<float[]>& start_pos, int n, const std::unique_ptr<float[]>& next_step);

int main() {
    srand (static_cast <unsigned> (time(NULL)));
    const int dimmensions[] = {1,2,3,5,8,13};
    for (int i = 0; i < 6; i++) {
        LRS(1000,dimmensions[i]);
        LRS(10000,dimmensions[i]);
        LRS(100000,dimmensions[i]);
    }
    return 0;
}

float LRS(int iterations, int n) {
    // n = dimmensions, iterations = amount of times to 
    std::unique_ptr<float[]> rand_locations = std::make_unique<float[]> (n);
    for (int i = 0; i < n;i++) {
        rand_locations[i] = ((static_cast <float> (rand()) / static_cast <float> (RAND_MAX))*16)-8;
    }
    float bestFit = fitness(n, rand_locations);
    std::unique_ptr<float[]> next_step = std::make_unique<float[]> (n);
    for (int i = 0;i < iterations; i++) {
        step(rand_locations, n, next_step);
        float new_fit = fitness(n, next_step);
        if(new_fit > bestFit) {
            bestFit = new_fit;
            for (int i = 0; i < n; i++) {
                rand_locations[i] = next_step[i];
            }
        }
    }
    for (int i = 0; i < n; i++) {
        std::cout<<"Dimmension " << i <<" Value: "<< rand_locations[i] << std::endl;
    }
    std::cout<<"Best Found Fit: " << bestFit << std::endl;
}

void step(const std::unique_ptr<float[]>& start_pos, int n, const std::unique_ptr<float[]>& next_step) {
    const float step_size = 0.1f;
    for(int i = 0;i < n; i++) {
        float rand_delta = ((static_cast <float> (rand()) / static_cast <float> (RAND_MAX))*step_size)-step_size;
        next_step[i] = start_pos[i] + rand_delta;
    }
}

float fitness(int n, const std::unique_ptr<float[]>& x) {
    // n = dimmensions, x = point to test for fitness
    float sigma_1 = 0.0;
    float sigma_2 = 0.0;
    for (int i = 0;i < n;i++) {
        sigma_1 = pow((x[i] + pow(-1,i)*(i%4)),2);
    }
    sigma_1 = -sqrt(sigma_1);
    for (int i = 0;i < n; i++) {
        sigma_2 = pow(x[i],i);
    }
    sigma_2 = sin(sigma_2);
    float answer = sigma_1 + sigma_2;
    return answer;
}
