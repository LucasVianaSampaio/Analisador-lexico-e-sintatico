int sum(int n) {
    int i;
    int s = 0;
    for (i = 0; i < n; i = i + 1) {
        s = s + i;
    }
    return s;
}

int main() {
    int x = sum(5);
    return 0;
}
