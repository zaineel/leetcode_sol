int mid_(int x, int y)
{
    return (x + y) / 2;
}

int searchInsert(int *nums, int numsSize, int target)
{
    int left, right;
    left = 0;
    right = numsSize - 1;
    while (left <= right)
    {
        int mid = mid_(left, right);
        if (nums[mid] == target)
        {
            return mid;
        }
        else if (nums[mid] < target)
        {
            left = mid + 1;
        }
        else
        {
            right = mid - 1;
        }
    }
    return left;