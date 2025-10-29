#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

const int MAXN = 1000;
static int N_;  // 전체 도시 수

static vector<pair<int,int>> adj[MAXN];

void init(int N, int K, int sCity[], int eCity[], int mLimit[]) {
    N_ = N;

    for (int i = 0; i < N_; ++i)
        adj[i].clear();

    for (int i = 0; i < K; ++i) {
        int u = sCity[i];
        int v = eCity[i];
        int w = mLimit[i];
        adj[u].push_back({v, w});
    }
}

void add(int sCity, int eCity, int mLimit) {
    adj[sCity].push_back({eCity, mLimit});
}


int calculate(int sCity, int eCity) {
    const int INF = 1e9;
    static int dist[MAXN];
    fill(dist, dist + N_, 0);
	bool reached = false;

    priority_queue<pair<int,int>> pq;
    dist[sCity] = INF;
    pq.push({dist[sCity], sCity});

    while (!pq.empty()) {
        auto [curCap, u] = pq.top();
        pq.pop();

        if (curCap < dist[u]) continue;
        if (u == eCity){
			reached = true;
			break;
		}

        for (auto &[v, w] : adj[u]) {
            int cand = min(curCap, w);
            if (cand > dist[v]) {
                dist[v] = cand;
                pq.push({cand, v});
            }
        }
    }

    if(!reached) return -1;
	else return dist[eCity];
}
