/*
    긍정, 책임
*/

#include <iostream>
#include <string>
using namespace std;

class MyUnorderedSet {
private:
    static const int TABLE_SIZE = 23; // x가 1~20임

    struct Node{
        int key;
        Node* next;
        Node(int k, Node* n = nullptr) : key(k), next(n) {};
    };

    Node* table[TABLE_SIZE];

    int hash(int key) const {
        return (key % TABLE_SIZE + TABLE_SIZE) % TABLE_SIZE;
    }

public:
    MyUnorderedSet(){
        for(int i=0; i<TABLE_SIZE; ++i) table[i] = nullptr;
    }

    ~MyUnorderedSet(){
        for(int i=0; i<TABLE_SIZE; ++i){
            Node* curr = table[i];
            while (curr){
                Node* temp = curr;
                curr = curr -> next;
                delete temp;
            }
        }
    }

    bool check(int key) const {
        int h = hash(key);
        Node* curr = table[h];
        while (curr){
            if (curr->key == key) return true; // 찾았으면 잇다 하고, 
            curr = curr -> next; // 못 찾았으면 다음으로 넘어가기
        }
        return false; // curr이 false라는 것은 끝까지 갔다는 것
    }

    void add (int key){
        if (check(key)) return; // 중복 방지
        int h = hash(key);
        table[h] = new Node(key, table[h]);
    }

    void remove(int key){
        int h = hash(key);
        Node* curr = table[h];
        Node* prev = nullptr;
        while (curr){
            if (curr -> key == key){
                if(prev) prev -> next = curr -> next;
                else table[h] = curr -> next;
                delete curr;
                return;
            }
        }
    }

    void toggle(int key){
        if (check(key)) remove(key);
        else add(key);
    }

    void all() {
        for(int i=1; i<=20; ++i) add(i);
    }

    void empty() {
        for (int i=1; i<=20; ++i) remove(i);
    }

};

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL); // 연산 수가 MAX 3'000'000개
    int M,x;
    string cmd;
    cin >> M;

    MyUnorderedSet st;

    for (int i=0; i<M; ++i){
        cin >> cmd;
        if (cmd == "add"){
            cin >> x;
            st.add(x);
        }
        else if (cmd == "remove"){
            cin >> x;
            st.remove(x);
        }
        else if (cmd == "check"){
            cin >> x;
            if(st.check(x)) cout << "1\n";
            else cout << "0\n";
        }
        else if (cmd == "toggle"){
            cin >> x;
            st.toggle(x);
        }
        else if (cmd == "all"){
            st.all();
        }
        else if (cmd == "empty"){
            st.empty();
        }

    }

    return 0;
}