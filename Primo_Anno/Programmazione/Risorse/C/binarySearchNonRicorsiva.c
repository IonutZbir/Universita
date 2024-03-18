int binary_search(float entry, float *arr, int len_arr){
    if (len_arr == 0){
        return 0;
    }
    int start = 0;
    int mid;
    int end = len_arr;
    while (start <= end){
        mid = (start + end) / 2;
        if (arr[mid] == entry){
            return 1;
        } else if (entry > arr[mid]){
            start = mid + 1;
        } else if (entry < arr[mid]){
            end = mid - 1;
        }
    }
    return -1;
}
