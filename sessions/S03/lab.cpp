// S03 lab: vector operations, dynamic-array accounting and singly linked list.
// Build: g++ -std=c++17 -O2 -Wall -Wextra -pedantic lab.cpp -o lab
#include <cassert>
#include <iostream>
#include <memory>
#include <stdexcept>
#include <string>
#include <vector>

struct Node {
    int value;
    std::unique_ptr<Node> next;
    explicit Node(int v) : value(v), next(nullptr) {}
};

class SinglyLinkedList {
public:
    void append(int value) {
        auto node = std::make_unique<Node>(value);
        Node* raw = node.get();
        if (!head_) head_ = std::move(node);
        else tail_->next = std::move(node);
        tail_ = raw;
        ++size_;
    }

    void prepend(int value) {
        auto node = std::make_unique<Node>(value);
        if (!head_) tail_ = node.get();
        node->next = std::move(head_);
        head_ = std::move(node);
        ++size_;
    }

    Node* find(int value) const {
        for (Node* p = head_.get(); p; p = p->next.get())
            if (p->value == value) return p;
        return nullptr;
    }

    void insert_after(Node* predecessor, int value) {
        if (!contains(predecessor))
            throw std::invalid_argument("predecessor is not in this list");
        auto node = std::make_unique<Node>(value);
        Node* raw = node.get();
        node->next = std::move(predecessor->next);
        predecessor->next = std::move(node);
        if (tail_ == predecessor) tail_ = raw;
        ++size_;
    }

    bool remove_first(int value) {
        std::unique_ptr<Node>* link = &head_;
        Node* previous = nullptr;
        while (*link && (*link)->value != value) {
            previous = link->get();
            link = &((*link)->next);
        }
        if (!*link) return false;
        bool was_tail = tail_ == link->get();
        *link = std::move((*link)->next);
        --size_;
        if (was_tail) tail_ = previous;
        if (!head_) tail_ = nullptr;
        return true;
    }

    std::vector<int> to_vector() const {
        std::vector<int> out;
        for (Node* p = head_.get(); p; p = p->next.get()) out.push_back(p->value);
        return out;
    }

    bool invariant_holds() const {
        std::size_t count = 0;
        Node* last = nullptr;
        for (Node* p = head_.get(); p; p = p->next.get()) { ++count; last = p; }
        return count == size_ && last == tail_ &&
               ((size_ == 0) == (head_ == nullptr)) &&
               ((size_ == 0) == (tail_ == nullptr));
    }

private:
    bool contains(Node* node) const {
        for (Node* p = head_.get(); p; p = p->next.get()) if (p == node) return true;
        return false;
    }
    std::unique_ptr<Node> head_;
    Node* tail_ = nullptr; // non-owning pointer to the final node
    std::size_t size_ = 0;
};

std::size_t simulate_doubling_appends(std::size_t count) {
    std::size_t size = 0, capacity = 1, copies = 0;
    for (std::size_t i = 0; i < count; ++i) {
        if (size == capacity) { copies += size; capacity *= 2; }
        ++size;
    }
    return copies;
}

void self_check() {
    std::vector<int> values{10, 20, 30, 40};
    values.insert(values.begin() + 2, 25);
    assert((values == std::vector<int>{10, 20, 25, 30, 40}));
    SinglyLinkedList list;
    assert(list.invariant_holds());
    list.append(20); list.prepend(10); list.append(30);
    Node* predecessor = list.find(10);
    assert(predecessor != nullptr);
    list.insert_after(predecessor, 15);
    assert((list.to_vector() == std::vector<int>{10, 15, 20, 30}));
    assert(list.invariant_holds());
    assert(list.remove_first(20));
    assert(!list.remove_first(999));
    for (int value : {10, 15, 30}) {
        assert(list.remove_first(value));
        assert(list.invariant_holds());
    }
    assert(list.to_vector().empty());
    assert(simulate_doubling_appends(9) == 15);
    std::cout << "Self-check passed.\n";
}

void demo() {
    std::vector<int> values{10, 20, 30, 40};
    values.insert(values.begin() + 2, 25);
    std::cout << "vector after insert:";
    for (int value : values) std::cout << ' ' << value;
    std::cout << "\nCopies for 9 appends with doubling: "
              << simulate_doubling_appends(9) << '\n';
    SinglyLinkedList list;
    for (int value : {10, 20, 30}) list.append(value);
    Node* predecessor = list.find(10);
    assert(predecessor);
    list.insert_after(predecessor, 15);
    std::cout << "linked list after insertion:";
    for (int value : list.to_vector()) std::cout << ' ' << value;
    std::cout << '\n';
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " --self-check|--demo\n";
        return 2;
    }
    const std::string option = argv[1];
    if (option == "--self-check") self_check();
    else if (option == "--demo") demo();
    else { std::cerr << "Unknown option: " << option << '\n'; return 2; }
}
