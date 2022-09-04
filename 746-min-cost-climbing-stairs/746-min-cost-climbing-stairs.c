

int minCostClimbingStairs(int* cost, int costSize){
    int a = 0,b = 0;
    for(int i=2; i <= costSize; ++i) {
        int v1 = a + cost[i-2];
        int v2 = b + cost[i-1];
        a = b;
        b = v1 < v2 ? v1 : v2;
    }
    return b;

}