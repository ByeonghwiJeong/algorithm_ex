#include <bits/stdc++.h>
using namespace std;
int ret_a = 1;
void a(){
	ret_a = 2;
	cout << ret_a << "\n";
	return;
}
double b(){
	return 1.233;
}
int main(){
	a();
	double ret_b = b();
	char a = 'a';
	string b = "wow fantastic";
	string c = "wow";
	c += " ";
	c += "fantastic";
	cout << ret_b << "\n";
	cout << a << "\n";
	cout << b << "\n";
	cout << c << "\n";
	cout << c.size() << "\n";	
	return 0;
}
// a��� �Լ��� ret�� �ٲٰ� 
// ���� X >>> void ���
// return �ϴ� ���� Ÿ�Կ� ���߾
// void, string, double, int, bool ... ���� 
