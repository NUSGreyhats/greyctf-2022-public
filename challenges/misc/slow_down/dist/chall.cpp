/* g++-6 chall.cpp -o chall */
#include <iostream>
#include <unordered_map>
#include <ctime>
#include <string>
using namespace std;

#define LIMIT 25000

string flag = "<REDACTED>";


int main() {
    // Ignore these two lines
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long count = 0;
    // id => price
    unordered_map<long long, int> map;

    cout << "Blazinn fazz hashmapp price tracker" << endl;
    cout << "I'll give you something nice if it's too slow" << endl;

    double time = 0;
    int op = LIMIT;
    long long sum;
    while (op--) {
        int action; cin >> action;

        clock_t begin;

        switch (action) {

            case 0:
                long long id; int amount;
                cin >> id >> amount;
                if (count == LIMIT) {
                    cout << "This is too much..." << endl;
                    break;
                }
                count++;

                begin = clock();
                map[id] = amount;
                time += (double) (clock() - begin) / CLOCKS_PER_SEC;

                break;

            case 1:
                sum = 0;

                begin = clock();
                for (auto &item : map) {
                    sum += item.second;
                }
                time += (double) (clock() - begin) / CLOCKS_PER_SEC;

                cout << "The total amount is " << sum << endl;

                break;

            case 2:
                cout << "The total time is " << time << endl;
        }

        if (time > 5.0) {
            cout << flag << endl;
            return 1;
        }
    }
}


