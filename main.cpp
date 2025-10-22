/*
    긍정, 책임
*/
#include <iostream>
#include <vector>

using namespace std;

int N, M, K;
vector<long long> A, seg;

long long build(int idx, int l, int r){
    if(l == r) return seg[idx] = A[l]; // 어차피 l == r이 true임
    int mid = (l + r) / 2;
    return seg[idx] = build(idx*2, l, mid) + build(idx*2+1, mid+1, r);
}

long long query(int idx, int l, int r, int ql, int qr){
    if (qr < l || r < ql) return 0;
    if (ql <= l && r <= qr) return seg[idx];
    int mid = (l + r) / 2;
    return query(idx*2, l, mid, ql, qr) + query(idx*2+1, mid+1, r, ql, qr);
}

void update(int idx, int l, int r, int pos, long long val){
    if(l == r){
        seg[idx] = val;
        return;
    }
    int mid = (l + r) / 2;
    if(pos <= mid) update (idx*2, l, mid, pos, val);
    else update(idx*2+1, mid+1, r, pos, val);
    seg[idx] = seg[idx*2] + seg[idx*2+1];
}


int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    long long num;
    cin >> N >> M >> K;
    A.assign(N+1,0);
    for(int n=1; n<=N; ++n){
        cin >> num;
        A[n] = num;
    }
    seg.assign(4*(N+1),0);
    build(1,1,N);

    for(int i=0; i<M+K; ++i){
        int a;
        long long b,c;
        cin >> a >> b >> c;
        if(a == 1){
            update(1,1,N,(int)b,c);
        }
        else{
            cout << query(1,1,N,(int)b, (int)c) << "\n";
        }
    }

    return 0;
}