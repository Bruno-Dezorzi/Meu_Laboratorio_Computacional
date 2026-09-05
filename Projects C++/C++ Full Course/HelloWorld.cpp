#include <iostream>

namespace first{
    int x = 1;
}

namespace second {
    int x = 2;
}

void test_first(){
    using namespace first;

    std::cout << x << std::endl;
}

void test_second(){
    using namespace second;

    std::cout << x << std::endl;
}

int main(){

    std::cout << first::x << std::endl;
    std::cout << second::x << std::endl;

    std::cout << "Testando com funções que possuem using namespace dentro delas" << std::endl;
    
    test_first();
    test_second();

    return 0;
}