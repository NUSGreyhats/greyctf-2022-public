#include <iostream>
using namespace std;

template <typename T>
class Vector {
private:
    T *begin, *end, *cap;
public:
    Vector(int sz) {
        begin = end = new T[sz];
        cap = begin + sz;
    }

    void push_back(T val) {
        if (end == cap) {
            reallocate();
        }
        *end = val;
        end++;
    }

    void reallocate() {
        auto sz = cap - begin;
        auto nsz = sz * 2;
        auto nbegin = new T[nsz];
        auto ncap = nbegin + nsz;
        for (auto it = begin; it != end; it++) {
            nbegin[it - begin] = *it;
        }
        begin = nbegin;
        cap = ncap;
    }

    void for_each() {
        for (auto it = begin; it != end; it++) {
            cout << *it;
        }
    }
};

int main() {
    auto v = new Vector<int>(4);
    v->push_back(0);
    v->push_back(1);
    v->push_back(2);
    v->push_back(3);
    v->push_back(4);
    v->for_each();
}
