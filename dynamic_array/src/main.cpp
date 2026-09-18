#include <cstdlib>
#include <iostream>

using namespace std;

int main() {
    int* ptr = (int*)malloc(2*sizeof(int));
    if (ptr == nullptr) {
        cout << "Mem alloc failed\n";
        return 1;
    }

    *ptr = 25;
    ptr[1] = 33;
    ptr[100] = 33;
    cout << *ptr << "\n";
    cout << ptr[1] << "\n";
    cout << ptr[100] << "\n";


    free(ptr);
    return 0;
}
