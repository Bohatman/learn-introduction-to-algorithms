package main

import (
	"fmt"
	"math"
)

func mergeSubroutine(A []int, p, r int) {
	fmt.Println("Input is", A, "with arguments p=", p, "r=", r)
	if p < r {
		q := (p + r) / 2
		mergeSubroutine(A, p, q)
		mergeSubroutine(A, q+1, r)
		merge(A, p, q, r)
		fmt.Println()
	}
}

func merge(A []int, p, q, r int) {
	fmt.Println("Input is", A, "with arguments p=", p, "q=", q, "r=", r)
	n1 := q - p + 1 // 4
	n2 := r - q     // 4
	L := make([]int, n1+1)
	R := make([]int, n2+1)
	for i := 0; i < n1; i++ {
		L[i] = A[p+i]
	}
	for j := 0; j < n2; j++ {
		R[j] = A[q+1+j]
	}
	L[n1] = math.MaxInt64
	R[n2] = math.MaxInt64
	fmt.Println("L is", L)
	fmt.Println("R is", R)
	j := 0
	i := 0
	for k := p; k < r+1; k++ {
		if L[i] <= R[j] {
			A[k] = L[i]
			i++
		} else {
			A[k] = R[j]
			j++
		}
	}
	fmt.Println("Result is", A)
}

func main() {
	//         0  1  2  3  4  5  6  7
	A := []int{0, 1, 1, 2, 2, 3, 3, 4, 3, 4, 123, 4123, 4123, 22, 12, 334, 1123}
	merge(A, 12, 12, 13)
	// mergeSubroutine(A, 0, len(A)-1)
}
