package main

import (
	"fmt"
	"math/rand"
	"strconv"
	"time"
)

func insertSort(input []int) []int {
	for j := 1; j < len(input); j++ {
		key := input[j]
		i := j - 1
		for (i > -1) && (input[i] > key) {
			input[i+1] = input[i]
			i = i - 1
		}
		input[i+1] = key
	}
	return input
}
func insertSortDecremental(input []int) []int {
	for j := 1; j < len(input); j++ {
		comparator := input[j]
		i := j - 1
		for (i > -1) && (input[i] < comparator) {
			input[i+1] = input[i]
			i = i - 1
		}
		input[i+1] = comparator
	}
	return input
}

func main() {
	startRandomValueTime := time.Now().Nanosecond()
	var max int = 500
	input := make([]int, max)

	for n := 0; n < max; n++ {
		input[n] = rand.Intn(1000)
	}
	endRandomValueTime := time.Now().Nanosecond()
	RandomValueDuration := int64(endRandomValueTime - startRandomValueTime)

	startSortTime := time.Now().Nanosecond()
	toProcess := make([]int, max)
	copy(toProcess, input)

	sortedInput := insertSort(toProcess)
	endSortTime := time.Now().Nanosecond()
	SortDuration := int64(endSortTime - startSortTime)
	fmt.Println("Sorted time: " + strconv.FormatInt(SortDuration, 10) + " nanoseconds")

	fmt.Println("Random time: " + strconv.FormatInt(RandomValueDuration, 10) + " nanoseconds")
	fmt.Print("Input array  ->")
	fmt.Println(input)
	fmt.Print("Output array ->")
	fmt.Println(sortedInput)
}
