#include <iostream>
#include <vector>
#include <queue>
#include <limits>
using namespace std;

using ll = long long;
struct Edge { int to; ll w; };

int main() {
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    int N, M; 
    cin >> N >> M;
    vector<vector<Edge>> adj(N + 1);
    for (int i = 0; i < M; ++i) {
        int A, B; ll C;
        cin >> A >> B >> C;
        adj[A].push_back({B, C});
        adj[B].push_back({A, C});
    }
    int s, t; 
    cin >> s >> t;

    vector<ll> dist(N + 1, 0);
    priority_queue<pair<ll,int>> pq;
    dist[s] = numeric_limits<ll>::max();

    pq.push({dist[s], s});

    while (!pq.empty()) {
        auto [cap, v] = pq.top(); pq.pop();
        if (cap < dist[v]) continue;
        if (v == t) break;

        for (const auto& e : adj[v]) {
            ll ncap = min(cap, e.w);
            if (ncap > dist[e.to]) {
                dist[e.to] = ncap;
                pq.push({ncap, e.to});
            }
        }
    }

    cout << dist[t] << '\n';
    return 0;
}
