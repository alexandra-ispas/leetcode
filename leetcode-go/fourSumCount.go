func fourSumCount(nums1 []int, nums2 []int, nums3 []int, nums4 []int) int {
    var counter int

    cd := make(map[int]int)

    for _, e3 := range nums3 {
        for _, e4 := range nums4 {
            cd[e3+e4] = cd[e3+e4] + 1
        }
    }

    for _, e1 := range nums1 {
        for _, e2 := range nums2 {
            lookupKey := (e1+e2) * (-1)
            counter += cd[lookupKey]
        }
    }

    return counter
}
