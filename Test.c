#include <stdio.h>

int main() {
    int n;
    
    // 输入三角形的行数
    printf("请输入行数：");
    scanf("%d", &n);
    
    // 打印等腰三角形
    for (int i = 1; i <= n; i++) {
        // 打印空格
        for (int j = 1; j <= n - i; j++) {
            printf(" ");
        }
        
        // 打印星号
        for (int j = 1; j <= 2 * i - 1; j++) {
            printf("*");
        }
        
        // 换行
        printf("\n");
    }
    
    return 0;
}
