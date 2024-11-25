#include <iostream>

typedef int itemType;

class Stack
{
public:
    Stack(int max);
    ~Stack();
    void push(itemType v);
    itemType pop();
    int empty();
private:
    struct node
    {
        itemType key;
        struct node* next;
    };
    struct node* head;
    struct node* z;
};

Stack::Stack(int max)
{
    head = new node;
    z = new node;
    head->next = z;
    z->next = z;
}

Stack::~Stack()
{
    struct node* t = head;
    while (t != z)
    {
        head = t;
        t = t->next;
        delete head;
    }
}

void Stack::push(itemType v)
{
    struct node* t = new node;
    t->key = v;
    t->next = head->next;
    head->next = t;
}

itemType Stack::pop()
{
    itemType x;
    struct node* t = head->next;
    head->next = t->next;
    x = t->key;
    delete t;
    return x;
}

int Stack::empty()
{
    return head->next == z;
}

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

int main()
{
	Multiplikation_Postfix_UPN();
	Multiplikation_Infix();
	return 0;
}
