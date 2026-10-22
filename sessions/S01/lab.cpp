// S01 C++17 analogue. Compile with:
// g++ -std=c++17 -O2 -Wall -Wextra -pedantic lab.cpp -o lab
// Run ./lab --self-check or ./lab --benchmark (lab.exe on Windows).
// These are demonstrations, not answers to exercises.md.

#include <algorithm>
#include <cassert>
#include <chrono>
#include <cstddef>
#include <iostream>
#include <string>
#include <vector>

int linear_search(const std::vector<int>& values, int target) {
    for (std::size_t i = 0; i < values.size(); ++i) {
        if (values[i] == target) {
            return static_cast<int>(i);
        }
    }
    return -1;
}

bool has_duplicate(const std::vector<int>& values) {
    for (std::size_t i = 0; i < values.size(); ++i) {
        for (std::size_t j = i + 1; j < values.size(); ++j) {
            if (values[i] == values[j]) {
                return true;
            }
        }
    }
    return false;
}

std::size_t search_comparisons(const std::vector<int>& values, int target) {
    std::size_t checks = 0;
    for (int value : values) {
        ++checks;
        if (value == target) {
            return checks;
        }
    }
    return checks;
}

std::size_t duplicate_comparisons(const std::vector<int>& values) {
    std::size_t checks = 0;
    for (std::size_t i = 0; i < values.size(); ++i) {
        for (std::size_t j = i + 1; j < values.size(); ++j) {
            ++checks;
            if (values[i] == values[j]) {
                return checks;
            }
        }
    }
    return checks;
}

void self_check() {
    assert(linear_search({}, 4) == -1);
    assert(search_comparisons({}, 4) == 0);
    assert(linear_search({4}, 4) == 0);
    assert(linear_search({4}, 9) == -1);
    assert(linear_search({9, 4, 4, 1}, 4) == 1);
    assert(search_comparisons({9, 4, 4, 1}, 4) == 2);
    assert(linear_search({9, 4, 4, 1}, 7) == -1);
    assert(search_comparisons({9, 4, 4, 1}, 7) == 4);
    assert(!has_duplicate({}));
    assert(!has_duplicate({4}));
    assert(has_duplicate({4, 4}));
    assert(!has_duplicate({3, 8, 5}));
    assert(duplicate_comparisons({3, 8, 5}) == 3);
    assert(has_duplicate({3, 8, 5, 8}));
    assert(duplicate_comparisons({3, 8, 5, 8}) == 5);
    std::cout << "C++ self-checks passed (search and duplicate edge cases).\n";
}

template <typename F>
long long median_ns(F call) {
    volatile int sink = call();
    std::vector<long long> observations;
    observations.reserve(11);
    for (int repetition = 0; repetition < 11; ++repetition) {
        auto start = std::chrono::steady_clock::now();
        sink = call();
        auto end = std::chrono::steady_clock::now();
        observations.push_back(std::chrono::duration_cast<std::chrono::nanoseconds>(end - start).count());
    }
    (void)sink;
    std::sort(observations.begin(), observations.end());
    return observations[observations.size() / 2];
}

void benchmark() {
    std::cout << "C++ standard: " << __cplusplus << " (record compiler, flags and hardware separately)\n";
    std::cout << "Timer: steady_clock; 1 warm-up; median of 11 calls; deterministic inputs\n";
    std::cout << "n, absent_search_comparisons, search_median_ns, distinct_pair_comparisons, pair_median_ns\n";
    for (int size : {16, 64, 256, 512}) {
        std::vector<int> values;
        values.reserve(static_cast<std::size_t>(size));
        for (int i = 0; i < size; ++i) {
            values.push_back(i);
        }
        auto search_time = median_ns([&] { return linear_search(values, -1); });
        auto pair_time = median_ns([&] { return static_cast<int>(has_duplicate(values)); });
        std::cout << size << ", " << search_comparisons(values, -1) << ", " << search_time
                  << ", " << duplicate_comparisons(values) << ", " << pair_time << '\n';
    }
    std::cout << "Interpret within this compiled program only; small timings can be noisy.\n";
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cout << "Use --self-check or --benchmark\n";
        return 0;
    }
    const std::string option = argv[1];
    if (option == "--self-check") {
        self_check();
    } else if (option == "--benchmark") {
        benchmark();
    } else {
        std::cerr << "Unknown option\n";
        return 2;
    }
}
