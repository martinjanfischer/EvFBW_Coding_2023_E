#include <iostream>

using namespace std;

/*
 * Benutzung:
 * struct node* anfang = new node;
 * struct node* ende = new node;
 * anfang->next = ende; ende->next = ende;
 */

struct node
{
	int key;
	struct node* next;
};

void main()
{
	int N, M;
	cin >> N >> M;

	// Erzeuge eine ringf�rmige Liste mit N knoten
	struct node* t = new node;
	t->key = 1;
	struct node* x = t;
	for (int i = 2; i <= N; i++)
	{
		t->next = new node;
		t = t->next;
		t->key = i;
	}
	t->next = x;

	// Wiederhole den Durchlauf von N knoten
	// bis nichts mehr �brig ist
	while (t != t->next)
	{
		// �berspringe M knoten
		for (int i = 1; i < M; i++)
			t = t->next;

		// Drucke knoten M
		cout << t->next->key << ' ';

		// L�sche n�chsten knoten aus dem Ring
		// und beginne von vorn beim �bern�chsten
		x = t->next;
		t->next = x->next;
		delete x;
	}
	cout << t->key << '\n';
}
