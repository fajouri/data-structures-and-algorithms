// S02 lab: recursive traces and binary search.
// Build: g++ -std=c++17 -O2 -Wall -Wextra -pedantic lab.cpp -o lab
#include <cassert>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

long long factorial(int n) {
    if (n < 0) {
        throw std::invalid_argument("n must be non-negative");
    }
    if (n <= 1) {
        return 1;
    }
    return static_cast<long long>(n) * factorial(n - 1);
}

// Return any matching index or -1. Preconditions: values is sorted ascending.
int binary_search(const std::vector<int>& values, int target) {
    int lo = 0;
    int hi = static_cast<int>(values.size()); // half-open interval [lo, hi)
    while (lo < hi) {
        const int mid = lo + (hi - lo) / 2;
        if (values[mid] == target) {
            return mid;
        }
        if (values[mid] < target) {
            lo = mid + 1;
        } else {
            hi = mid;
        }
    }
    return -1;
}

int binary_search_recursive(const std::vector<int>& values, int target,
                            int lo, int hi) {
    if (lo >= hi) {
        return -1;
    }
    const int mid = lo + (hi - lo) / 2;
    if (values[mid] == target) {
        return mid;
    }
    if (values[mid] < target) {
        return binary_search_recursive(values, target, mid + 1, hi);
    }
    return binary_search_recursive(values, target, lo, mid);
}

int binary_search_recursive(const std::vector<int>& values, int target) {
    return binary_search_recursive(values, target, 0,
                                   static_cast<int>(values.size()));
}

void self_check() {
    assert(factorial(0) == 1);
    assert(factorial(1) == 1);
    assert(factorial(5) == 120);

    const std::vector<int> values{1, 3, 4, 6, 8, 10, 14, 17};
    const std::vector<std::pair<int, int>> cases{
        {10, 5}, {1, 0}, {17, 7}, {2, -1}, {7, -1}, {20, -1}};
    for (const auto& test : cases) {
        assert(binary_search(values, test.first) == test.second);
        assert(binary_search_recursive(values, test.first) == test.second);
    }

    const std::vector<int> empty;
    assert(binary_search(empty, 4) == -1);
    assert(binary_search_recursive(empty, 4) == -1);
    const std::vector<int> singleton{7};
    assert(binary_search(singleton, 7) == 0);
    assert(binary_search(singleton, 2) == -1);

    const std::vector<int> duplicates{2, 2, 2, 5, 5, 9};
    const int idx1 = binary_search(duplicates, 5);
    const int idx2 = binary_search_recursive(duplicates, 5);
    assert(idx1 >= 0 && duplicates[idx1] == 5);
    assert(idx2 >= 0 && duplicates[idx2] == 5);

    std::cout << "Self-check passed.\n";
}

void demo() {
    std::cout << "factorial(5): " << factorial(5) << '\n';
    const std::vector<int> values{2, 4, 7, 9, 13, 18, 21};
    for (int target : {13, 8, 2, 21}) {
        std::cout << "target=" << target
                  << " -> index=" << binary_search(values, target) << '\n';
    }
    std::cout << "Analyse by hand: T(n)=T(n-1)+Theta(1)\n";
    std::cout << "Analyse by hand: T(n)=2T(n/2)+Theta(n)\n";
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " --self-check|--demo\n";
        return 2;
    }
    const std::string option = argv[1];
    if (option == "--self-check") {
        self_check();
    } else if (option == "--demo") {
        demo();
    } else {
        std::cerr << "Unknown option: " << option << '\n';
        return 2;
    }
    return 0;
}
