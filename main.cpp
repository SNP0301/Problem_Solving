/*
    긍정, 책임
    유클리드 호제법
*/
#include <iostream>
using namespace std;

int gcd(int A, int B) {
	int res = A % B;
	while (res != 0) {
		A = B;
		B = res;
		res = A % B;
	}
	return B;
}

int lcm(int A, int B) {
	return ((A * B) / gcd(A, B));
}

int main() {
	int A, B;
	cin >> A >> B;
	cout << gcd(A, B) << "\n" << lcm(A, B);
}