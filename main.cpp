/*
    긍정, 책임

    {start, end, 거리} 저장해두고 MST 완성하기
*/
#include <iostream>
#include <queue>
#include <cmath>
#include <vector>
#include <iomanip>

using namespace std;


const static int MAXN = 100;

struct DSU {
    vector <int> parent, rankv; // 매크로 충돌 에반데;; 이름 바꿔야하나
    DSU(int n=0) {if (n) init(n);}

    void init(int n){
        parent.resize(n);
        rankv.assign(n,0);
        for(int i=0; i<n; ++i){
            parent[i] = i;
        }
    }

    int find(int x){
        if(parent[x] == x) return x;
        else{
            return parent[x] = find(parent[x]);
        }
    }

    bool unite(int a, int b){
        int ra = find(a);
        int rb = find(b);

        if(ra == rb) return false;
        if(rankv[ra] < rankv[rb]) swap(ra, rb);
        parent[rb] = ra;
        if(rankv[ra] == rankv[rb]) ++rankv[ra];
        return true;
    }
};

struct star {
    float x;
    float y;
    star() : x(0), y(0) {}
    star(float x_, float y_) : x(x_), y(y_) {}
};

star starArr[MAXN];

using Edge = tuple<int,int,float>;
priority_queue<Edge,vector<Edge>,greater<Edge>> pq;

float getDistance(star A, star B){
    return (float)(A.x-B.x)*(A.x-B.x)+(A.y-B.y)*(A.y-B.y);
}


int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    float N,x,y;
    DSU dsu;

    cin >> N;
    for(int i=0; i<N; ++i){
        cin >> x >> y;
        starArr[i] = star(x,y);
        for(int j=0; j<i; ++j){
            float curDistance = getDistance(starArr[i],starArr[j]);
            pq.push({curDistance,i,j});
        }
    }

    dsu.init(N);
    int picked = 0;
    double answer = 0.0;

    while(!pq.empty() && picked < N-1){
        Edge cur = pq.top(); pq.pop();
        float w = get<0>(cur);
        int u = get<1>(cur);
        int v = get<2>(cur);
        if(dsu.unite(u,v)){
            answer += sqrt(w);
            ++picked;
        }
    }
    
    // for(const star& s: stars){
    //     cout << fixed << setprecision(2) << s.x << "\n";
    // }

    /*
    while(!pq.empty()){
        tuple<int,int,float> cur = pq.top(); pq.pop();
        cout << fixed << setprecision(2) << get<0>(cur) << ", " << get<1>(cur) << ", " << get<2>(cur) << "\n";
    }
    */
   cout << fixed << setprecision(2) << answer;


    return 0;
}