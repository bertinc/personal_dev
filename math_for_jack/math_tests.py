import math

def main():
    nums = [8.2, 10.1, 2.6, 4.8, 2.4, 5.6, 7.0, 3.3]
    standard_deviation(nums)

def standard_deviation(nums):
    precision = 2
    mean = 0
    for num in nums:
        mean += num
    mean = round(mean / len(nums), precision)
    print(f'Mean: {mean}')
    diffs = []
    for num in nums:
        diffs.append(round(mean - num, precision))
    print(f'Diffs: {diffs}')
    diffs_sq = []
    for diff in diffs:
        diffs_sq.append(round(diff ** 2, precision))
    print(f'Diffs Squared: {diffs_sq}')
    diffs_added = 0
    for diff_sq in diffs_sq:
        diffs_added += diff_sq
    diffs_added = round(diffs_added / len(nums), precision)
    print(f'Just before rooted: {diffs_added}')
    sqroot = round(math.sqrt(diffs_added), precision)
    print(f'Standard Deviation: {sqroot}')

if __name__ == '__main__':
    main()