#include <iostream>
#include <vector>

//#define _GLIBCXX_USE_C99 1

using namespace std;


vector<int> twoSum(vector<int>& nums, int target) {
        for (int i = 0; i < nums.size(); i++)
            for (int j = 0; j < nums.size(); j++)
                if (i != j)
                    if (nums[i] + nums[j] == target) {
                        vector<int> indices;
                        indices.push_back(i);
                        indices.push_back(j);
                        return indices;
                    }
}

int main() {
	std::cout << "test" << endl;
        vector<int> nums;
        nums.push_back(5);
        nums.push_back(2);
        nums.push_back(4);
        nums.push_back(3);
        nums.push_back(6);

        int target = 10;

        vector<int> ret = twoSum(nums, target);

        int a = ret.back();
        ret.pop_back();
        int b = ret.back();
        ret.pop_back();

        cout << "First element at: " << a << endl;
        cout << "Second element at: " << b << endl;

    return 0;
}