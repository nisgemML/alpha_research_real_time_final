#include <iostream>
#include <chrono>
#include <thread>

class ExecutionEngine {
public:
    void execute_order(std::string side, double price) {
        auto start = std::chrono::high_resolution_clock::now();

        // simulate latency
        std::this_thread::sleep_for(std::chrono::microseconds(500));

        double executed_price = price * 1.0001; // slippage

        auto end = std::chrono::high_resolution_clock::now();
        std::cout << side << " executed at " << executed_price << std::endl;
        std::cout << "Latency: " << std::chrono::duration_cast<std::chrono::microseconds>(end - start).count() << " us\n";
    }
};
