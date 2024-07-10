double averageWaitingTime(int **customers, int customersSize, int *customersColSize)
{
    int currentTime = 0;
    long totalWaitingTime = 0;
    int waitingTime = 0;

    for (int i = 0; i < customersSize; i++)
    {
        int arrivalTime = customers[i][0];
        int processingTime = customers[i][1];

        if (currentTime < arrivalTime)
        {
            currentTime = arrivalTime;
        }
        waitingTime = (currentTime + processingTime) - arrivalTime;
        totalWaitingTime += waitingTime;
        currentTime += processingTime;
    }
    return (double)totalWaitingTime / customersSize;
    ;
}