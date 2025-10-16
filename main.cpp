/*
    긍정, 책임

    MST를 만들어라. 근데 2개.
    MST를 2개 만들 수 있는 경우의 수들 중에서 가장 비용이 가장 케이스? 말도 안됨
*/
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

struct Edge {
    int u, v, weight;
    Edge(int u, int v, int weight) : u(u), v(v), weight(weight) {}

    bool operator<(const Edge& other) const { // 해당 struct에 한정되는 오버라이딩이므로 걱정 ㄴㄴ
        return weight > other.weight;
    }
};

class UnionFind {
private:
    vector<int> parent, rank;

public:
    UnionFind(int n) {
        parent.resize(n+1);
        rank.resize(n+1, 0);
        for (int i = 1; i <= n; ++i) parent[i] = i; // 일단 나 자신으로 초기화
    }

    int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }

    bool unite(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);

        if (rootX != rootY) {
            if (rank[rootX] > rank[rootY]) parent[rootY] = rootX;
            else if (rank[rootX] < rank[rootY]) parent[rootX] = rootY;
            else {
                parent[rootY] = rootX;
                rank[rootX]++;
            }
            return true;
        }
        else return false;  // 이미 같은 집합에 있는 경우
    }
};

int main() {
    int n, m;
    int mx = -1;
    cin >> n >> m;
    
    if (n == 2){
        cout << 0;
        return 0;
    }
    
    
    priority_queue<Edge> pq;

    for (int i = 0; i < m; ++i) {
        int u, v, w;
        cin >> u >> v >> w;
        pq.push(Edge(u, v, w));
    }

    UnionFind uf(n);

    int mstWeight = 0;
    int edgesUsed = 0;

    while (!pq.empty() && edgesUsed < n - 1) {
        Edge e = pq.top(); pq.pop();

        if (uf.unite(e.u, e.v)) {
            mstWeight += e.weight;
            edgesUsed++;
            mx = max(mx,e.weight);
        }
    }

    // 최소 신장 트리의 가중치 출력
    cout << mstWeight-mx;  // 최소 신장 트리의 총 가중치

    return 0;
}
