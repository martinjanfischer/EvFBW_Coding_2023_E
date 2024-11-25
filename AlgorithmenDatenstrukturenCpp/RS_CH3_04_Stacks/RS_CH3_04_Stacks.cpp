#include <iostream>

typedef int itemType;

class Stack
{
private:
	itemType* stack;
	int p;
public:
	Stack(int max = 100)
	{
		stack = new itemType[max]; p = 0;
	}
	~Stack()
	{
		delete stack;
	}
	inline void push(itemType v)
	{
		stack[p++] = v;
	}
	inline itemType pop()
	{
		return stack[--p];
	}
	inline int empty()
	{
		return !p;
	}
};

using namespace std;

void Multiplikation_Postfix_UPN()
{
	Stack acc(50);

	char c;
	while (cin.get(c))
	{
		int x = 0;

		while (c == ' ')
			cin.get(c);

		if (c == '+')
			x = acc.pop() + acc.pop();

		if (c == '*')
			x = acc.pop() * acc.pop();

		while (c >= '0' && c <= '9')
		{
			x = 10 * x + (c - '0');
			cin.get(c);
		}
		acc.push(x);
	}
	cout << acc.pop() << '\n';
}

void Multiplikation_Infix()
{
	Stack save(50);
	char c;
	while (cin.get(c))
	{
		if (c == ')')
			cout.put(save.pop());

		if (c == '+')
			save.push(c);

		if (c == '*')
			save.push(c);

		while (c >= '0' && c <= '9')
		{
			cout.put(c); cin.get(c);
		}

		if (c != '(')
			cout << ' ';
	}
	cout << '\n';
}

void main()
{
	Multiplikation_Postfix_UPN();
	Multiplikation_Infix();
}